from django.conf import settings
from django.db import models
from django.contrib.auth.models import User, AbstractUser

class CustomUser(AbstractUser):
    ROLE_CHOICES = (
        ('customer', 'Customer'),
        ('admin', 'Admin'),
    )
    first_name = models.CharField(max_length=30, verbose_name='Имя')
    last_name = models.CharField(max_length=30, verbose_name='Фамилия')
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='customer', verbose_name='Роль')

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.role})"

class Product(models.Model):
    name = models.CharField(max_length=100)
    article = models.CharField(max_length=50, verbose_name='Артикул')
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='products/', blank=True, null=True)

    def __str__(self):
        return self.name

class Cart(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.user.username} - {self.product.name}"

