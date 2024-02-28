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
    path('add_customer/', views.add_customer, name='add_customer'),
    path('add_product/', views.add_product, name='add_product'),
    path('add_supplier/', views.add_supplier, name='add_supplier'),
    path('add_user/', views.add_user, name='add_user'),
    path('new_sale/', views.new_sale, name='new_sale'),
  
]
