from django.shortcuts import render,HttpResponse,redirect, get_object_or_404
from .models import Product, Customer, Sale, SalesInvoice,Supplier,Login
from datetime import datetime
from .forms import ProductForm , CustomerForm , SupplierForm
# Create your views here.

def base(request):
    return render(request, 'base.html')


def product_add(request):

    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = ProductForm()
    return render(request, 'product_add.html', {'form': form})



def product_edit(request, pk):
    instance_edit = get_object_or_404(Product,pk=pk)
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=instance_edit)
        if form.is_valid():
            form.save()
            return redirect('product_list')  # Redirect to the product list page after successful edit
    else:
        form = ProductForm(instance=instance_edit)
    return render(request, 'product_edit.html', {'form': form})
    


def product_del(request,pk):
    instance=Product.objects.get(pk=pk)
    instance.delete()
    products= Product.objects.all()
    return render(request,'product_list.html',{'products':products})


    

def sale_new(request):
    if request.method == 'POST':
        # Process form submission
        customer_id = request.POST.get('customerSelect')
        if customer_id:
            customer = Customer.objects.get(id=customer_id)
        else:
            # Process customer data
            cus_name = request.POST.get('cus_name')
            cus_add = request.POST.get('cus_add')
            cus_email = request.POST.get('cus_email')
            cus_mob = request.POST.get('cus_mob')
            cus_gender = request.POST.get('cus_gender')
            cus_gstno = request.POST.get('cus_gstno')

            # Create a new customer
            customer = Customer.objects.create(
                cus_name=cus_name,
                cus_add=cus_add,
                cus_email=cus_email,
                cus_mob=cus_mob,
                cus_gender=cus_gender,
                cus_gstno=cus_gstno
            )

        # Create a new sales invoice
        sales_invoice = SalesInvoice.objects.create(
            sales_date=datetime.now(),
            total_amount=request.POST.get('grand_total'),
            discount=request.POST.get('discount'),
            customer=customer
        )

        # Process sales product data
        for i in range(len(request.POST.getlist('product[]'))):
            product_id = request.POST.getlist('product[]')[i]
            quantity = request.POST.getlist('quantity[]')[i]
            price = request.POST.getlist('sales_price[]')[i]
            sale = Sale.objects.create(
                sales_invoice=sales_invoice,
                product=Product.objects.get(id=product_id),
                quantity=quantity,
                price=price
            )

        return render(request, 'sales_bill_temp.html', {'sales_invoice': sales_invoice})

    # If it's a GET request, just render the form
    products = Product.objects.all()
    customers = Customer.objects.all()
    return render(request, 'sale_new.html', {'products': products, 'customers': customers})


def product_list(request):
    products = Product.objects.all()
    return render(request, 'product_list.html', {'products': products})



def customer_view(request):
    customers = Customer.objects.all()
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
    instance_edit = get_object_or_404(Customer,pk=pk)
    if request.method == 'POST':
        form = CustomerForm(request.POST, instance=instance_edit)
        if form.is_valid():
            form.save()
            return redirect('customer_view')  # Redirect to the customer list page after successful edit
    else:
        form = CustomerForm(instance=instance_edit)
    return render(request, 'customer_edit.html', {'form': form})
    


def customer_del(request,pk):
    instance=Customer.objects.get(pk=pk)
    instance.delete()
    customers= Customer.objects.all()
    return render(request,'customer_view.html',{'customers':customers})


    




def supplier_view(request):
    suppliers = Supplier.objects.all()
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
    
    
def supplier_del(request,pk):
    instance=Supplier.objects.get(pk=pk)
    instance.delete()
    suppliers= Supplier.objects.all()
    return render(request,'supplier_view.html',{'suppliers': suppliers})
    
       
    
  

def invoice_details(request):
    # Check if salesInvoiceId exists in the session
    if 'salesInvoiceId' in request.session:
        # Retrieve salesInvoiceId from session
        sales_invoice_id = request.session['salesInvoiceId']
        
        # Fetch sales invoice details
        sales_invoice_details = SalesInvoice.objects.get(sales_invoice_id=sales_invoice_id)
        
        # Fetch customer details for the given sales invoice
        customer_details = Customer.objects.filter(sales_invoice__sales_invoice_id=sales_invoice_id).first()
        
        # Fetch sale details for the given sales invoice
        sale_details = Sale.objects.filter(sales_invoice_id=sales_invoice_id)
        
        # Render template with invoice details
        return render(request, 'invoice_details.html', {
            'sales_invoice_id': sales_invoice_id,
            'sales_invoice_details': sales_invoice_details,
            'customer_details': customer_details,
            'sale_details': sale_details
        })
    else:
        return HttpResponse("Sales Invoice ID not found in session.")