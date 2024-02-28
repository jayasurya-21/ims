from django.contrib import admin

# Register your models here.
from . models import MovieInfo,Director,Customer,Sale,SalesInvoice,Product

admin.site.register(MovieInfo)
admin.site.register(Director)
admin.site.register(Customer)
admin.site.register(Product)
admin.site.register(Sale)
admin.site.register(SalesInvoice)
