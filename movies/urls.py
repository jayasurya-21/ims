"""
URL configuration for movie_manager project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.create,name='create'),
    path('list/', views.list,name='list'),
    path('edit/', views.edit,name='edit'),
    path('home/', views.home,name='home'),
    path('customer_add/', views.customer_add, name='customer_add'),
    path('customer_view/', views.customer_view, name='customer_view'),
    path('add_product/', views.add_product, name='add_product'),
    path('add_user/', views.add_user, name='add_user'),
    path('new_sale/', views.new_sale, name='new_sale'),
    path('inventory/', views.inventory, name='inventory'),
    path('supplier_add/', views.supplier_add, name='supplier_add'),
    path('supplier_del/', views.supplier_del, name='supplier_del'),
    path('supplier_edit/', views.supplier_edit, name='supplier_edit'),
    path('supplier_view/', views.supplier_view, name='supplier_view'),






  
]
