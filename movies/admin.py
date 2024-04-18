from django.contrib import admin

# Register your models here.
from . models import Customer,Sale,Product,Supplier,SaleProduct,Sale


admin.site.register(Customer)
admin.site.register(Product)
admin.site.register(Sale)
#admin.site.register(SaleInvoice)
admin.site.register(Supplier)
admin.site.register(SaleProduct)
                
