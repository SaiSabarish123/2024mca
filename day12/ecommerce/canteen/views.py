
from django.shortcuts import render, redirect, get_object_or_404
from .models import Menu, Category
from .forms import MenuForm
from django.contrib.admin.views.decorators import staff_member_required

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
    cart = request.session.get('cart', {})

    # Handle form POST actions
    if request.method == 'POST':
        if 'clear_cart' in request.POST:
            request.session['cart'] = {}  # clear cart
            return redirect('view_cart')
        else:
            # Update quantities
            for key, value in request.POST.items():
                if key.startswith('qty_'):
                    item_id = key.split('_')[1]
                    try:
                        qty = int(value)
                        if qty > 0:
                            cart[item_id] = qty
                        else:
                            cart.pop(item_id, None)  # remove if qty is 0
                    except ValueError:
                        continue
            request.session['cart'] = cart
            return redirect('view_cart')

    # Display cart contents
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

    return render(request, 'bill.html', {'items': items, 'total': total})


def menu_detail(request, pk):
    menu = get_object_or_404(Menu, pk=pk)
    return render(request, 'menu_detail.html', {'menu': menu})

@staff_member_required
def delete_menu_item(request, pk):
    menu = get_object_or_404(Menu, pk=pk)
    menu.delete()
    return redirect('menu_list')
