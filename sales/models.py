from django.db import models
from product.models import Product
from nodes.models import Nodes
from django.contrib.auth.models import User
import datetime


class Bill(models.Model):

    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    total = models.IntegerField( null=True)
    subtotal = models.IntegerField( null=True)
    node =models.ForeignKey(Nodes, null=True, blank=True, on_delete=models.CASCADE)
    date = models.DateField(("Date"), default=datetime.date.today)

    def save_data(self,user,node):
            newBill = Bill(user=user, node=node)
            newBill.save()

class ItemBill(models.Model):

    Product = models.ForeignKey(Product, null=True, blank=True, on_delete=models.CASCADE)
    bill = models.ForeignKey(Bill, null=True, blank=True, on_delete=models.CASCADE)
    value = models.IntegerField()
    quantity = models.IntegerField()
    date = models.DateField(("Date"), default=datetime.date.today)

    def save_data(self,Product,bill,value,cant,date):
            newItemBill = ItemBill(Product=Product, bill=bill,value=value, quantity=quantity)
            newItemBill.save()