from django.shortcuts import render, redirect
from .models import Product, Detail, Customer
from .forms import ProductForm
from .forms import DetailForm
from .forms import CustomerForm

def index(request):
    return render(request, "index.html")


def product(request):
    products = Product.objects.order_by('product_name')

    return render(request, 'product.html', {'products': products})


def detail(request):
    details = Detail.objects.order_by('detail_name')

    return render(request, 'detail.html', {'details': details})

def customer(request):
    customers = Customer.objects.order_by('last_name')

    return render(request, 'customer.html', {'customers': customers})


def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/product/')
    else:
        form = ProductForm()

    return render(request, 'forms.html', {'form': form})


def add_detail(request):
    if request.method == 'POST':
        form = DetailForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/detail/')
    else:
        form = DetailForm()

    return render(request, 'forms.html', {'form': form})


def add_customer(request):
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            result = form.cleaned_data
            new = Customer(
                name=result['name'],
                last_name=result['last_name'],
                phone=result['phone'])
            new.save()
            return redirect('/customers/')
    else:
        form = CustomerForm()

        return render(request, 'forms.html', {'form': form})
