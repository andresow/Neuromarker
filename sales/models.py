from django.db import models
from product.models import Product
from nodes.models import Nodes, Node_father
from django.contrib.auth.models import User
import datetime


class Bill(models.Model):

    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    total = models.IntegerField( null=True, default=0)
    subtotal = models.IntegerField( null=True, default=0)
    node =models.ForeignKey(Nodes, null=True, blank=True, on_delete=models.CASCADE, related_name="nodo_del_vendedor")
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

class Sending(models.Model):
    bill = models.ForeignKey(Bill, null=True, blank=True, on_delete=models.CASCADE)
    state = models.CharField(max_length=15)


class Cart(models.Model):
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    total = models.IntegerField( null=True, default=0)
    subtotal = models.IntegerField( null=True, default=0)
    date = models.DateField(("Date"), default=datetime.date.today)
    items = models.IntegerField(null = True, default=0)
    
    def save_data(self):
            newCart = Cart()
            newCart.save()

    @staticmethod
    def getActiveCart(request, id_cliente):
        if "active_cart" in request.session:
            return Cart.objects.get(id=request.session["active_cart"])
        else:
            cart = Cart.objects.create(user=id_cliente)
            request.session["items_bill"] = []
            request.session["total_bill"] = 0
            request.session["active_cart"] = cart.id
            return cart

class ItemCart(models.Model):

    Product = models.ForeignKey(Product, null=True, blank=True, on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, null=True, blank=True, on_delete=models.CASCADE)
    value = models.IntegerField()
    quantity = models.IntegerField()
    date = models.DateField(("Date"), default=datetime.date.today)

    def save_data(self,Product,cart,value,cant,date):
            newItemCart = ItemCart(Product=Product, cart=cart,value=value, quantity=quantity)
            newItemCart.save()