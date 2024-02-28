from django.shortcuts import render
from . models import MovieInfo
#from . models import MovieForm
from .models import Customer
from .models import Product
from .models import Supplier
from .models import Login
from .models import Product, Customer, Sale, SalesInvoice
from datetime import datetime

# Create your views here.
def create(request):
    frm=MovieForm()
    if request.POST:
        tittle=request.POST.get('tittle')
        year=request.POST.get('year')
        description=request.POST.get('description')
        movie_obj=MovieInfo(tittle=tittle,year=year,description=description)
        movie_obj.save()
        
    return render(request,'create.html',{'frm':frm})

def list(request):
    movie_set=MovieInfo.objects.all       
    print(movie_set) 
    return render(request,'list.html',{'movies':movie_set})

def edit(request):
    return render(request,'edit.html')

def home(request):
    return render(request,'home.html')


def add_customer(request):
    if request.method == 'POST':
        cus_name = request.POST.get('cus_name')
        cus_add = request.POST.get('cus_add')
        cus_email = request.POST.get('cus_email')
        cus_mob = request.POST.get('cus_mob')
        cus_gender = request.POST.get('cus_gender')
        cus_gstno = request.POST.get('cus_gstno')
        cus_due = request.POST.get('cus_due')

        # Create a new customer object
        new_customer = Customer(
            cus_name=cus_name,
            cus_add=cus_add,
            cus_email=cus_email,
            cus_mob=cus_mob,
            cus_gender=cus_gender,
            cus_gstno=cus_gstno,
            cus_due=cus_due
        )
        # Save the new customer object
        new_customer.save()
        message = "Customer added successfully!"
        return render(request, 'add_customer.html', {'message': message})

    return render(request, 'add_customer.html')



def home(request):
    return render(request, 'home.html')



def add_product(request):
    if request.method == 'POST':
        # Process form submission
        product_date = request.POST.get('product_date')
        product_name = request.POST.get('product_name')
        category = request.POST.get('category')
        brand = request.POST.get('brand')
        price = request.POST.get('price')
        unit = request.POST.get('unit')
        quantity = request.POST.get('quantity')
        hsn = request.POST.get('hsn')
        description = request.POST.get('description')
        tax = request.POST.get('tax')
        discount_type = request.POST.get('discount_type')
        min_qty = request.POST.get('min_qty')
        exp_date = request.POST.get('exp_date')
        
        # Create the Product object and save it
        product = Product(
            product_date=product_date,
            product_name=product_name,
            category=category,
            brand=brand,
            price=price,
            unit=unit,
            quantity=quantity,
            hsn=hsn,
            description=description,
            tax=tax,
            discount_type=discount_type,
            min_qty=min_qty,
            exp_date=exp_date
        )
        product.save()
        
        # Optionally, you can redirect the user to a success page
        return render(request, 'product_added.html')

    # If it's a GET request, just render the form
    return render(request, 'add_product.html')





def add_supplier(request):
    if request.method == 'POST':
        # Process form submission
        sup_name = request.POST.get('sup_name')
        sup_add = request.POST.get('sup_add')
        sup_category = request.POST.get('sup_category')
        sup_gstno = request.POST.get('sup_gstno', '')
        sup_email = request.POST.get('sup_email')
        sup_cpn = request.POST.get('sup_cpn', '')
        sup_mob = request.POST.get('sup_mob')

        # Create the Supplier object and save it
        supplier = Supplier.objects.create(
            sup_name=sup_name,
            sup_add=sup_add,
            sup_category=sup_category,
            sup_gstno=sup_gstno,
            sup_email=sup_email,
            sup_cpn=sup_cpn,
            sup_mob=sup_mob
        )

        # Optionally, you can render a success template here
        return render(request, 'supplier_added.html')

    # If it's a GET request, just render the form
    return render(request, 'add_supplier.html')

def add_user(request):
    if request.method == 'POST':
        # Process form submission
        username = request.POST.get('username')
        name = request.POST.get('name')
        password = request.POST.get('password')

        # Create the Login object and save it
        login = Login(username=username, name=name, password=password)
        login.save()

        # Optionally, you can render a success template here
        return render(request, 'user_added.html')

    # If it's a GET request, just render the form
    return render(request, 'add_user.html')





def new_sale(request):
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
    return render(request, 'new_sale.html', {'products': products, 'customers': customers})
