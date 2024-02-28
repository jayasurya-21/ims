from django.db import models

# Create your models here.
class MovieInfo(models.Model):
    tittle=models.CharField(max_length=250)
    year=models.IntegerField(null=True)
    description=models.TextField()


class Director(models.Model):
  name=models.CharField(max_length=300)




class Customer(models.Model):
    GENDER_CHOICES = [
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other'),
    ]

    cus_name = models.CharField(max_length=100)
    cus_add = models.TextField()
    cus_email = models.EmailField(blank=True)
    cus_mob = models.CharField(max_length=15)
    cus_gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    cus_gstno = models.CharField(max_length=15, blank=True)
    cus_due = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def __str__(self):
        return self.cus_name
 
 
class Product(models.Model):
   
      product_date = models.DateField()
      product_name = models.CharField(max_length=100)
      category = models.CharField(max_length=100)
      brand = models.CharField(max_length=100)
      price = models.DecimalField(max_digits=10, decimal_places=2)
      unit = models.CharField(max_length=20)
      quantity = models.IntegerField()
      hsn = models.CharField(max_length=20)
      description = models.TextField()
      tax = models.DecimalField(max_digits=5, decimal_places=2)
      discount_type = models.DecimalField(max_digits=5, decimal_places=2)
      min_qty = models.IntegerField()
      exp_date = models.DateField()

def __str__(self):
        return self.product_name
      
      
      
      
class Supplier(models.Model):
    sup_name = models.CharField(max_length=100)
    sup_add = models.TextField()
    sup_category = models.CharField(max_length=100)
    sup_gstno = models.CharField(max_length=20, blank=True, null=True)
    sup_email = models.EmailField()
    sup_cpn = models.CharField(max_length=100, blank=True, null=True)
    sup_mob = models.CharField(max_length=15)

    def __str__(self):
        return self.sup_name
      
class Login(models.Model):
    username = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.username
      
      
from django.db import models

class Customer(models.Model):
    cus_name = models.CharField(max_length=100)
    cus_add = models.TextField()
    cus_email = models.EmailField()
    cus_mob = models.CharField(max_length=15)
    cus_gender = models.CharField(max_length=10)
    cus_gstno = models.CharField(max_length=20)

    def __str__(self):
        return self.cus_name

class Product(models.Model):
    # Define your Product model fields
    pass

class SalesInvoice(models.Model):
    sales_date = models.DateTimeField()
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    discount = models.DecimalField(max_digits=10, decimal_places=2)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)

    def __str__(self):
        return f"Invoice ID: {self.id}"

class Sale(models.Model):
    sales_invoice = models.ForeignKey(SalesInvoice, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Sale ID: {self.id}"
