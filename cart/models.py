from django.db import models
from books.models import Book
from accounts.models import Profile
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

# Create your models here.

class Cart(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    total_amount = models.DecimalField(max_digits=6, decimal_places=2, default=0)
    
    def __str__(self):
        return f"{self.profile} - ${self.total_amount}"

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name="items")
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    
    @property
    def subtotal(self):
        return self.book.price * self.quantity
    
    def __str__(self):
        return f"{self.book.title} - {self.quantity}"
    
class Order(models.Model):
    customer = models.ForeignKey(Profile, on_delete=models.CASCADE,)
    total_amount = models.DecimalField(max_digits=6, decimal_places=2)
    date = models.DateField(auto_now_add=True)
    def __str__(self):
        return f"{self.customer} - ${self.total_amount} - {self.date}"
    
@receiver(post_save, sender=CartItem)
@receiver(post_delete, sender=CartItem)
def update_cart_total(sender, instance, **kwargs):
    cart = instance.cart
    total = sum(item.subtotal for item in cart.items.all())
    cart.total_amount = total
    cart.save()