from django.shortcuts import render
from books.models import Book

def home(request):
    featured_books   = Book.objects.filter(id__in=[1, 2, 3])
    best_sellers     = Book.objects.filter(id__in=[4, 5, 6])
    discounted_books = Book.objects.filter(id__in=[7, 8, 9])

    return render(request, "home/home.html", {
        "featured_books": featured_books,
        "best_sellers": best_sellers,
        "discounted_books": discounted_books,
    })