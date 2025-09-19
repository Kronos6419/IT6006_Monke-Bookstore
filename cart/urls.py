from django.urls import path
from . import views

urlpatterns = [
    path('', views.cart_detail, name='cart_detail'),
    path('update/<int:item_id>/', views.update_cart_item, name='update_cart_item'),
    path('place_order/', views.place_order, name='place_order'),
]