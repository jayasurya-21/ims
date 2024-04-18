from datetime import date
from django.db import models
from django.db import transaction
from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
class UserManager(BaseUserManager):
    def create_user(self, username, password=None, **extra_fields):
        if not username:
            raise ValueError('The Username field must be set')
        user = self.model(username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(username, password, **extra_fields)

class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=100, unique=True)
    name = models.CharField(max_length=100)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    groups = models.ManyToManyField(
        'auth.Group',
        related_name='custom_user_set',
        blank=True,
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
        verbose_name='groups',
    )

    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='custom_user_permissions',
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions',
    )

    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['name']

    def __str__(self):
        return self.username

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
    CATEGORY_CHOICES = [
        ('CE', 'Cement'),
        ('HA', 'Hardware'),
        ('PA', 'Paint'),
        ('SB', 'Steel Bars'),
        ('SI', 'Steel Items'),
        ('PV', 'PVC'),
        ('EL', 'Electrical'),
    ]
    UNIT_CHOICES = [
        ('NU', 'NUMBER'),
        ('KG', 'KILOGRAMS'),
        ('LT', 'LITRE'),
        ('MT', 'METER'),
        ('PC', 'PIECE'),
    ]

    product_name = models.CharField(max_length=100, null=True)
    category = models.CharField(max_length=2, choices=CATEGORY_CHOICES, null=True)
    brand = models.CharField(max_length=100, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    unit = models.CharField(max_length=20, choices=UNIT_CHOICES, null=True)
    quantity = models.IntegerField(null=True)
    hsn = models.CharField(max_length=20, null=True)
    description = models.TextField(null=True)
    product_date = models.DateField(default=date.today)
    exp_date = models.DateField(null=True)

    def __str__(self):
        return self.product_name

    def update_quantity(self, quantity_purchased):
        self.quantity += quantity_purchased
        self.save()
      
class Supplier(models.Model):
    sup_name = models.CharField(max_length=100, null=True)
    sup_add = models.TextField(null=True)
    sup_category = models.CharField(max_length=100, null=True)
    sup_gstno = models.CharField(max_length=20, blank=True, null=True)
    sup_email = models.EmailField(null=True)
    sup_cpn = models.CharField(max_length=100, blank=True, null=True)
    sup_mob = models.CharField(max_length=15, null=True)

    def __str__(self):
        return self.sup_name
      
class Login(models.Model):
    username = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.username

class Sale(models.Model):
    sale_date = models.DateField(default=timezone.now)
    invoice_number = models.CharField(max_length=20, unique=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)

    def __str__(self):
        return f"Sale {self.invoice_number}"

class SaleProduct(models.Model):
    sale = models.ForeignKey(Sale, on_delete=models.CASCADE, related_name='sale_products')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    sale_price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.product.product_name} - {self.quantity} x {self.sale_price}"
    
    
class Invoice(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)

class InvoiceItem(models.Model):
    invoice = models.ForeignKey(Invoice, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

