from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from .models import Product, Customer, Sale , Supplier, Login,SaleProduct
from .forms import ProductForm, CustomerForm, SupplierForm
from django.forms import formset_factory
from django.shortcuts import render
from .models import Supplier, Product
from django.http import HttpResponseBadRequest
from django.utils import timezone
import string
import random
from datetime import datetime
from django.utils import timezone
from django.contrib.auth import authenticate, login, logout

from django.contrib.auth.decorators import login_required

# Create your views here.
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('base')
        else:
            context = {'error': 'Invalid username or password'}
            return render(request, 'login.html', context)
    return render(request, 'login.html')

def logout_view(request):
    logout(request)
    return redirect('login')



@login_required
def base(request):
    products = Product.objects.all()
    count = products.count()
    customers = Customer.objects.all()
    ccount = customers.count()
    return render(request, 'base.html', {'count': count, 'ccount': ccount})

@login_required
def product_add(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = ProductForm()
    return render(request, 'product_add.html', {'form': form})

@login_required
def product_edit(request, pk):
    instance_edit = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=instance_edit)
        if form.is_valid():
            form.save()
            return redirect('product_list')  # Redirect to the product list page after successful edit
    else:
        form = ProductForm(instance=instance_edit)
    return render(request, 'product_edit.html', {'form': form})


@login_required
def product_del(request, pk):
    instance = Product.objects.get(pk=pk)
    instance.delete()
    products = Product.objects.all()
    return render(request, 'product_list.html', {'products': products})

@login_required
def sale_added(request):
    return render(request, 'sale_added.html')


@login_required
def product_list(request):
    search = request.GET.get('search', '')
    products = Product.objects.filter(product_name__icontains=search)
    return render(request, 'product_list.html', {'products': products})

def customer_view(request):
    search = request.GET.get('search', '')
    customers = Customer.objects.filter(cus_name__icontains=search)
    return render(request, 'customer_view.html', {'customers': customers})


def customer_add(request):
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('customer_view')
    else:
        form = CustomerForm()
    return render(request, 'customer_add.html', {'form': form})


def customer_edit(request, pk):
    instance_edit = get_object_or_404(Customer, pk=pk)
    if request.method == 'POST':
        form = CustomerForm(request.POST, instance=instance_edit)
        if form.is_valid():
            form.save()
            return redirect('customer_view')  # Redirect to the customer list page after successful edit
    else:
        form = CustomerForm(instance=instance_edit)
    return render(request, 'customer_edit.html', {'form': form})


def customer_del(request, pk):
    instance = Customer.objects.get(pk=pk)
    instance.delete()
    customers = Customer.objects.all()
    return render(request, 'customer_view.html', {'customers': customers})


def supplier_view(request):
    search = request.GET.get('search', '')
    suppliers = Supplier.objects.filter(sup_name__icontains=search)
    return render(request, 'supplier_view.html', {'suppliers': suppliers})


def supplier_add(request):
    if request.method == 'POST':
        form = SupplierForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('supplier_view')
    else:
        form = SupplierForm()
    return render(request, 'supplier_add.html', {'form': form})


def supplier_edit(request, pk):
    instance_edit = get_object_or_404(Supplier, pk=pk)
    if request.method == 'POST':
        form = SupplierForm(request.POST, instance=instance_edit)
        if form.is_valid():
            form.save()
            return redirect('supplier_view')  # Redirect to the supplier list page after successful edit
    else:
        form = SupplierForm(instance=instance_edit)
    return render(request, 'supplier_edit.html', {'form': form})
def supplier_del(request, pk):
    instance = Supplier.objects.get(pk=pk)
    instance.delete()
    suppliers = Supplier.objects.all()
    return render(request, 'supplier_view.html', {'suppliers': suppliers})


from django.db import transaction

def new_sale(request):
    if request.method == 'POST':
        if 'save_sale' in request.POST:
            # Handle the save sale logic
            customer_id = request.POST.get('customer')
            customer = Customer.objects.get(id=customer_id)

            sale = Sale.objects.create(
                customer=customer,
                sale_date=timezone.now().date(),  # Set the sale_date to the current date
                invoice_number=generate_unique_invoice_number()
            )

            total_amount = 0
            for i in range(1, int(request.POST.get('row_count', 1)) + 1):
                product_id = request.POST.get(f'product_{i}')
                sale_quantity = int(request.POST.get(f'sale_quantity_{i}'))
                sale_price = float(request.POST.get(f'sale_price_{i}'))
                selected = request.POST.get(f'selected_{i}', 'off')

                if selected == 'on':
                    product = Product.objects.get(id=product_id)
                    if product.quantity >= sale_quantity:
                        product.quantity -= sale_quantity
                        product.save()

                        SaleProduct.objects.create(
                            sale=sale,
                            product=product,
                            quantity=sale_quantity,
                            sale_price=sale_price
                        )
                        total_amount += sale_quantity * sale_price
                    else:
                        # Handle the case when the product quantity is not sufficient
                        return render(request, 'sale_new.html', {'error': 'Not enough product in stock', 'customers': Customer.objects.all(), 'products': Product.objects.all()})

            sale.total_amount = total_amount
            sale.save()
            return redirect('sale_detail', sale_id=sale.id)
        elif 'generate_invoice' in request.POST:
            # Handle the generate invoice logic
            return redirect('invoice_page', sale_id=sale.id)
    else:
        customers = Customer.objects.all()
        products = Product.objects.all()
        initial_product = products.first()
        return render(request, 'sale_new.html', {'customers': customers, 'products': products, 'initial_product': initial_product})    
    
def generate_unique_invoice_number():
    # Generate a random string of 5 characters
    random_string = ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))
    
    # Get the current date and time
    current_datetime = datetime.now().strftime('%Y%m%d%H%M%S')
    
    # Combine the random string and the current date/time to create the unique invoice number
    invoice_number = f"INV{current_datetime}{random_string}"
    
    return invoice_number


from .models import Product  # Import the Product model

from .models import Sale, SaleProduct  # Import the Sale and SaleProduct models

def sale_detail(request, sale_id):
    sale = get_object_or_404(Sale, id=sale_id)
    sale_products = SaleProduct.objects.filter(sale=sale)
    total_amount = sale.total_amount
    return render(request, 'sale_detail.html', {
        'sale': sale,
        'sale_products': sale_products,
        'customer': sale.customer,
        'total_amount': total_amount
    })
    
def invoice_page(request, sale_id):
    sale = get_object_or_404(Sale, id=sale_id)
    sale_products = SaleProduct.objects.filter(sale=sale)
    total_amount = sale.total_amount
    return render(request, 'sale_detail.html', {
        'sale': sale,
        'sale_products': sale_products,
        'total_amount': total_amount
    })
    
def sale_list(request):
    sales = Sale.objects.all().order_by('-sale_date')
    return render(request, 'sale_list.html', {'sales': sales})