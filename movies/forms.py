from django import forms
from django.forms import ModelForm
from .models import Product,Customer,Supplier,Sale
  
class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'

class SupplierForm(forms.ModelForm):
    class Meta:
        model = Supplier
        fields = '__all__'


class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields ='__all__'
        

        