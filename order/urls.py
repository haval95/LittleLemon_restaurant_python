from django.urls import path
from . import views

urlpatterns = [
    path("order/", views.Order, name="order_view"),
    path('add-to-cart/<int:item_id>/', views.add_to_cart, name='add_to_cart_view'),
    path('', views.Cart, name='cart_view'),
]
