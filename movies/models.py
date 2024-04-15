from datetime import date
from django.db import models
      


class Customer(models.Model):
    GENDER_CHOICES = [
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other'),
    ]

    cus_name = models.CharField(max_length=100,null=True)
    cus_add = models.TextField(null=True)
    cus_email = models.EmailField(blank=True,)
    cus_email = models.EmailField(blank=True,)
    cus_mob = models.CharField(max_length=15,null=True)
    cus_gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    cus_gstno= models.CharField(max_length=15,null=True)
    cus_due= models.CharField(max_length=15,null=True)
        

    def __str__(self):
        return self.cus_name
 

class Product(models.Model):
    
    product_name = models.CharField(max_length=100,null=True)
    category = models.CharField(max_length=100,null=True)
    brand = models.CharField(max_length=100,null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2,null=True)
    unit = models.CharField(max_length=20,null=True)
    quantity = models.IntegerField(null=True)
    hsn = models.CharField(max_length=20,null=True)
    description = models.TextField(null=True)
    tax = models.DecimalField(max_digits=5, decimal_places=2,null=True)
    discount_type = models.DecimalField(max_digits=5, decimal_places=2,null=True)
    min_qty = models.IntegerField(null=True)
    product_date = models.DateField(default=date.today)
    exp_date = models.DateField(null=True)

    def __str__(self):
        return self.product_name
      
      
class Supplier(models.Model):
    sup_name = models.CharField(max_length=100,null=True)
    sup_add = models.TextField(null=True)
    sup_category = models.CharField(max_length=100,null=True)
    sup_gstno = models.CharField(max_length=20, blank=True, null=True)
    sup_email = models.EmailField(null=True)
    sup_cpn = models.CharField(max_length=100, blank=True, null=True)
    sup_mob = models.CharField(max_length=15,null=True)

    def __str__(self):
        return self.sup_name
      
class Login(models.Model):
    username = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.username

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
