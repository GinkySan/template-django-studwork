from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

from .forms import RegistrationForm, ProductForm
from .models import Product, Cart

def product_list(request):
    products = Product.objects.all()
    return render(request, 'shop/product_list.html', {'products': products})

@login_required
def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    cart, created = Cart.objects.get_or_create(user=request.user, product=product)
    if not created:
        cart.quantity += 1
        cart.save()
    return redirect('product_list')

@login_required
def view_cart(request):
    cart_items = Cart.objects.filter(user=request.user)
    return render(request, 'shop/cart.html', {'cart_items': cart_items})

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            new_user = form.save(commit=False)
            new_user.set_password(form.cleaned_data['password'])
            new_user.save()
            return redirect('login')
    else:
        form = RegistrationForm()
    return render(request, 'registration/register.html', {'form': form})

@login_required
def profile(request):
    return render(request, 'registration/profile.html')

def home(request):
    return render(request, 'shop/home.html')

def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    return redirect('home')

@login_required
def remove_from_cart(request, item_id):
    item = get_object_or_404(Cart, id=item_id)
    if item.user == request.user:
        item.delete()
    return redirect('view_cart')