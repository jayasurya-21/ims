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

from django.urls import path,include
from . import views

urlpatterns = [

    path('', views.base,name='base'),
    
    path('sale_new/', views.sale_new, name='sale_new'),
    
    path('product_add/', views.product_add, name='product_add'),
    path('product_list/', views.product_list, name='product_list'),
    path('product_edit/<pk>', views.product_edit, name='product_edit'),
    path('product_del/<pk>', views.product_del, name='product_del'),
    
    path('supplier_add/', views.supplier_add, name='supplier_add'),
    path('supplier_view', views.supplier_view, name='supplier_view'),
    path('supplier_del/<pk>', views.supplier_del, name='supplier_del'),
    path('supplier_edit/<pk>', views.supplier_edit, name='supplier_edit'),

    path('customer_add/', views.customer_add, name='customer_add'),
    path('customer_view/', views.customer_view, name='customer_view'),
    path('customer_del/<pk>', views.customer_del, name='customer_del'),
    path('customer_edit/<pk>', views.customer_edit, name='customer_edit'),






  
]
