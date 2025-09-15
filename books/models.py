from django.db import models

# Create your models here.

class Book(models.Model):
    GENRE_CHOICES = [
        ('FIC', 'Fiction'),
        ('NF', 'Non-Fiction'),
        ('MYS', 'Mystery'),
        ('ROM', 'Romance'),
        ('SCI', 'Science Fiction'),
        ('FAN', 'Fantasy'),
        ('BIO', 'Biography'),
        ('HIS', 'History'),
        ('EDU', 'Educational')
    ]

    image = models.ImageField(upload_to='book_images/', blank=True, null=True)
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    genre = models.CharField(max_length=50, choices=GENRE_CHOICES, default="FIC")
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return f"{self.title} - ${self.price}"