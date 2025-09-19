from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import BookForm
from .models import Book
from cart.models import Cart, CartItem

# Create your views here.
def book_list(request):
    query = request.GET.get("q")
    if query:
        books = Book.objects.filter(title__icontains=query)
    else:
        books = Book.objects.all()
    return render(request, "books/book_list.html", {"books": books})

def book_detail(request, pk):
    book = get_object_or_404(Book, pk=pk)
    return render(request, "books/book_detail.html", {"book": book})

@login_required
def add_book(request):
    if not request.user.is_staff:  # only staff can add
        return redirect("book_list")

    if request.method == "POST":
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("book_list")
    else:
        form = BookForm()

    return render(request, "books/add_book.html", {"form": form})

@login_required
def add_to_cart(request, book_id):
    profile = request.user.profile
    cart, _ = Cart.objects.get_or_create(profile=profile, defaults={"total_amount": 0})
    book = get_object_or_404(Book, id=book_id)
    cart_item, created = CartItem.objects.get_or_create(cart=cart, book=book)
    if not created:
        cart_item.quantity += 1
    else:
        cart_item.quantity = 1
    cart_item.save()
    return redirect("book_detail", pk=book.id)