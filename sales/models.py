from django.db import models
from product.models import Product
from django.contrib.auth.models import User


class Bill(models.Model):

    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    total = models.CharField(max_length=40)
    subtotal = models.TextField()
    date = models. IntegerField()

class ItemBill(models.Model):

    Product = models.ForeignKey(Product, null=True, blank=True, on_delete=models.CASCADE)
    bill = models.ForeignKey(Bill, null=True, blank=True, on_delete=models.CASCADE)
    value = models.CharField(max_length=40)
    cant = models.TextField()
    date = models. IntegerField()

