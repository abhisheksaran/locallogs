"""localLogs URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include
from .views import products, buyer, seller 

urlpatterns = [
    path('', products.home, name='home'),

    path('seller/',include(([
        path('',seller.ItemsListView.as_view(), name='items_list'),
        path('items/add/',seller.ItemsAddView.as_view(), name='item_add'),
    ],'products'),namespace='seller')),

    path('buyer/',include(([
        path('',buyer.ItemsListView.as_view(), name='items_list'),
        path('cart/',buyer.OrdersListView.as_view(), name='orders_list'),
        path('cart/add/<int:pk>/',buyer.AddInCart, name='add_in_cart'),
    ],'products'),namespace='buyer')),
]
