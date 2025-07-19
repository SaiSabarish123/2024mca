from django.shortcuts import render, redirect, get_object_or_404
from .models import Menu, Category
from .forms import MenuForm
from django.contrib.admin.views.decorators import staff_member_required
import qrcode
import io
import base64
def menu_list(request):
    categories = Category.objects.prefetch_related('menus')
    return render(request, 'menu_list.html', {'categories': categories})

@staff_member_required
def add_menu_item(request):
    if request.method == 'POST':
        form = MenuForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('menu_list')
    else:
        form = MenuForm()
    return render(request, 'add_menu.html', {'form': form})

def add_to_cart(request, menu_id):
    if request.method == 'POST':
        qty = int(request.POST.get('quantity', 1))
        cart = request.session.get('cart', {})
        cart[str(menu_id)] = cart.get(str(menu_id), 0) + qty
        request.session['cart'] = cart
    return redirect('view_cart')


def view_cart(request):
    import qrcode, io, base64

    cart = request.session.get('cart', {})

    if request.method == 'POST':
        action = request.POST.get('action')
        item_id = request.POST.get('item_id')

        if action == 'delete' and item_id:
            cart.pop(item_id, None)
            request.session['cart'] = cart
            return redirect('view_cart')

        elif action == 'update' and item_id:
            try:
                qty = int(request.POST.get('quantity', 1))
                if qty > 0:
                    cart[item_id] = qty
                else:
                    cart.pop(item_id, None)
                request.session['cart'] = cart
            except ValueError:
                pass
            return redirect('view_cart')

        elif 'clear_cart' in request.POST:
            request.session['cart'] = {}
            return redirect('view_cart')

    items = []
    total = 0
    for item_id, qty in cart.items():
        menu = get_object_or_404(Menu, pk=item_id)
        subtotal = qty * menu.price
        items.append({
            'menu': menu,
            'quantity': qty,
            'subtotal': subtotal,
        })
        total += subtotal

    # QR code
    qr_data = "\n".join([f"{i['menu'].name} x{i['quantity']} = ₹{i['subtotal']}" for i in items])
    qr_data += f"\nTotal = ₹{total}"
    qr = qrcode.make(qr_data)
    buffer = io.BytesIO()
    qr.save(buffer, format='PNG')
    qr_img_b64 = base64.b64encode(buffer.getvalue()).decode()

    return render(request, 'bill.html', {
        'items': items,
        'total': total,
        'qr_img': qr_img_b64
    })

    
def menu_detail(request, pk):
    menu = get_object_or_404(Menu, pk=pk)
    return render(request, 'menu_detail.html', {'menu': menu})

@staff_member_required
def delete_menu_item(request, pk):
    menu = get_object_or_404(Menu, pk=pk)
    menu.delete()
    return redirect('menu_list')


