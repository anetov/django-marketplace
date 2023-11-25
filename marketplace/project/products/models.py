from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Client(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    sales = models.IntegerField(default=0)
    purchases = models.IntegerField(default=0)


class Category(models.Model):
    name_cat = models.CharField(max_length=100)
    
    class Meta:
        ordering = ('name_cat',)
        verbose_name_plural = 'Категории'
    
    def __str__(self):
        return self.name_cat


class Product(models.Model):
    name_prod = models.CharField(max_length=100)
    description = models.TextField()
    price = models.IntegerField()
    is_sold = models.BooleanField(default=False)
    creater_date = models.DateField(auto_now_add=True)
    created_by = models.ForeignKey(User, related_name='products',  on_delete=models.CASCADE)
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='products/images', null=True)
    
    class Meta:
        verbose_name_plural = 'Товары'
    
    def __str__(self):
        return self.name_prod

class Basket(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
