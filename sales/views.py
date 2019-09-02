from django.shortcuts import render
from nodes.models import Nodes, Comission
from product.models import Product
from sales.models import Bill, ItemBill, Cart, ItemCart
from django.contrib.auth.models import User

from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.core.serializers.json import DjangoJSONEncoder
from django.core import serializers
from django.core.serializers import serialize
import json
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required(login_url='/login/')
def createSalesCode(request, ide):
    if request.method == "POST": #os request.GET()
        codePost = request.POST['codeSale']
        codeLen = len(codePost)
        code = codePost[codeLen-1]
        node = Nodes.objects.get(id=int(code))
        product = Product.objects.get(id=ide)
        comission=node.percentage_commission * product.value
        user = User.objects.get(id=request.user.id)
        Bill.objects.create(user=user)
        bill = Bill.objects.all().last()
        ItemBill.objects.create(Product=product,bill=bill,value=product.value, quantity=request.POST['quantity'])
        bill.node_id = node.id 
        bill.total = int(product.value) * int(request.POST['quantity'])
        bill.save()
        moreComittion(node.id)
        valueComission = (int(node.percentage_commission)/100)*int(product.value)
        Comission.objects.create(value_commision=valueComission, type_payment='CODIGO', type_commission='REFERIDO', current_balance=comission,node=node.user)       
        comission = Comission.objects.all().last()
        comission.node_id = node.id 
        comission.save() 
        return render(request, "products/index.html")
    product = Product.objects.get(id=ide) 
    context = {'product':product}
    return render(request,'products/view_product.html',context)


def moreComittion(idSeller):
    count = Bill.objects.all().filter(node_id=idSeller).count()
    node = Nodes.objects.get(id=idSeller)
    if count == 30:
        node.percentage_commission = node.percentage_commission + 3
        node.save()
    if count == 60:
        node.percentage_commission = node.percentage_commission + 3
        node.save()
    if count == 90:
        node.percentage_commission = node.percentage_commission + 3
        node.save()
    if count == 100:
        node.percentage_commission = node.percentage_commission + 1
        node.save()

#def getShoppingCart(request):
 #   if request.is_ajax:
  #      if request.method == 'GET':

def getShoppingCart(request):
    cart = Cart.getActiveCart(request,request.user)
    items_cart = ItemCart.objects.filter(cart=cart)
    return {'cart':cart, 'items_cart':items_cart}

def addProductShoppingCart(request):
    if request.is_ajax:
        if request.method == 'GET':
            active_cart = Cart.getActiveCart(request, request.user) #MIRAR LO DEL REQUESTUSER
            productIn = request.GET.get('productIn')
            product = Product.objects.get(id=productIn)            
            try:
                item_cart = ItemCart.objects.get(cart=active_cart, Product=product)
                exist= True
            except ItemCart.DoesNotExist:
                item_cart = None
                exist = False
            if item_cart==None:
                item_cart = ItemCart.objects.create(Product=product,cart=active_cart,value=product.value, quantity=1)
            else:
                item_cart.quantity = 1 +item_cart.quantity
                item_cart.save()
            item_cart = item_cart_serializer(item_cart, product.name, str(product.picture))
            active_cart.total += product.value
            active_cart.items += 1
            active_cart.save()
            context = {'id_cart':active_cart.id,'total_sale':active_cart.total, 'item_cart':item_cart, 'items':active_cart.items, 'exist':exist}
            print(context)
            return HttpResponse(json.dumps(context,cls=DjangoJSONEncoder), content_type = "application/json")

def item_cart_serializer(item_cart, name_product, picture_product):
    return {'id': item_cart.id, 'id_product':item_cart.Product.id, 'name': name_product, 'value': item_cart.value, 'quantity': item_cart.quantity, 'picture':picture_product}

def deleteProductShoppingCart(request):
    if request.is_ajax:
        if request.method == 'GET':
            active_cart = Cart.getActiveCart(request, request.user)
            product_delete = request.GET.get('product_delete')
            product = Product.objects.get(id=product_delete)
            item_out = ItemCart.objects.get(Product=product, cart=active_cart)
            minus_total = item_out.quantity * item_out.value
            active_cart.total = active_cart.total - minus_total
            active_cart.items -= item_out.quantity
            active_cart.save()
            item_out.delete()
            return HttpResponse(json.dumps({"total":active_cart.total, 'items':active_cart.items, 'id_product':product_delete},cls=DjangoJSONEncoder), content_type = "application/json")