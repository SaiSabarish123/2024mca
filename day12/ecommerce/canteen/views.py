from django.shortcuts import render, redirect, get_object_or_404
from .models import Menu, Category
from .forms import MenuForm
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
import qrcode
import io
import base64

# Show menu grouped by category

def home(request):
    return render(request,'home.html')
def master(request):
    return render(request,'master.html')
def menu_list(request):
    categories = Category.objects.prefetch_related('menus')
    return render(request, 'menu_list.html', {'categories': categories})


# Admin: Add new menu item
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


# Add item to cart
def add_to_cart(request, menu_id):
    if request.method == 'POST':
        qty = int(request.POST.get('quantity', 1))
        cart = request.session.get('cart', {})
        cart[str(menu_id)] = cart.get(str(menu_id), 0) + qty
        request.session['cart'] = cart
    return redirect('view_cart')


# View cart, update/delete items, generate QR
def view_cart(request):
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

    # ✅ Correct UPI and QR generation
    upi_id = "9676569212@ybl"  # Replace with your real UPI ID
    upi_url = f"upi://pay?pa={upi_id}&pn=MotherTheresaCanteen&am={total}&cu=INR"

    qr = qrcode.make(upi_url)
    buffer = io.BytesIO()
    qr.save(buffer, format='PNG')
    qr_img_base64 = base64.b64encode(buffer.getvalue()).decode()

    return render(request, 'bill.html', {
        'items': items,
        'total': total,
        'upi_url': upi_url,
        'qr_img_base64': qr_img_base64,
    })

# Menu item detail
def menu_detail(request, pk):
    menu = get_object_or_404(Menu, pk=pk)
    return render(request, 'menu_detail.html', {'menu': menu})


# Admin: Delete menu item
@staff_member_required
def delete_menu_item(request, pk):
    menu = get_object_or_404(Menu, pk=pk)
    menu.delete()
    return redirect('menu_list')


# Signup
def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('menu_list')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})


# Login
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)

            # Check 'remember me' box
            if not request.POST.get('remember_me'):
                request.session.set_expiry(0)  # Session expires on browser close

            return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

# Logout
def logout_view(request):
    logout(request)
    return redirect('login')


# Protected profile/dashboard view
