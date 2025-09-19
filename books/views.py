from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import BookForm
from .models import Book

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

def home(request):
    featured_books   = Book.objects.filter(id__in=[1, 2, 3])
    best_sellers     = Book.objects.filter(id__in=[4, 5, 6])
    discounted_books = Book.objects.filter(id__in=[7, 8, 9])

    return render(request, "home/home.html", {
        "featured_books": featured_books,
        "best_sellers": best_sellers,
        "discounted_books": discounted_books,
    })