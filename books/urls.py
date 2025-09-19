from django.urls import path
from . import views

urlpatterns = [
    path("", views.book_list, name="book_list"),
    path("add/", views.add_book, name="add_book"),
    path("<int:pk>/", views.book_detail, name="book_detail"),
    path("add/<int:book_id>/", views.add_to_cart, name="add_to_cart")
]