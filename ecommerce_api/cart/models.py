from django.db import models
from products.models import Product
from users.models import User

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_cart")
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="product_cart")
    quantity = models.IntegerField(default=1)  

    def __str__(self):
        return f"{self.user.username} - {self.product.name} (x{self.quantity})"

