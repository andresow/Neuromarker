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
    if request.user.is_active:
        if request.is_ajax:
            if request.method == 'GET':
                active_cart = Cart.getActiveCart(request, request.user) #MIRAR LO DEL REQUESTUSER
                productIn = request.GET.get('productIn')
                cantidadIn = int(request.GET.get('cantidadIn'))
                product = Product.objects.get(id=productIn)
                funciona = False     
                if product.quantity >= cantidadIn:
                    print(product.quantity)       
                    try:
                        item_cart = ItemCart.objects.get(cart=active_cart, Product=product)
                        funciona = True
                        exist= True
                    except ItemCart.DoesNotExist:
                        item_cart = None
                        exist = False
                    if item_cart==None:
                        funciona = True
                        item_cart = ItemCart.objects.create(Product=product,cart=active_cart,value=product.value, quantity=cantidadIn)
                    else:
                        item_cart.quantity = cantidadIn +item_cart.quantity
                        item_cart.save()
                    item_cart = item_cart_serializer(item_cart, product.name, str(product.picture))
                    active_cart.total += product.value
                    active_cart.items += cantidadIn
                    active_cart.save()
                context = {'id_cart':active_cart.id,'total_sale':active_cart.total, 'item_cart':item_cart, 'items':active_cart.items, 'exist':exist, 'success':funciona}
                print(context)
                return HttpResponse(json.dumps(context,cls=DjangoJSONEncoder), content_type = "application/json")
    else:
        context = {'success':False}
        return HttpResponse(json.dumps(context, cls=DjangoJSONEncoder), content_type="application/json")
    

def login(request):
    return render(request,'auth/login.html')

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


def checkAvailability(request):
    active_cart = Cart.getActiveCart(request, request.user)
    items_cart = ItemCart.objects.all().filter(cart=active_cart)
    for item_cart in items_cart:
        if item_cart.quantity > item_cart.Product.quantity:
            item_cart.delete()
            return False
    return True

def finishSale(request):
    if request.is_ajax:
        if request.method == 'GET':
            if checkAvailability(request):
                active_cart = Cart.getActiveCart(request, request.user)
                bill = Bill.objects.create(user=request.user, total=active_cart.total, subtotal=active_cart.subtotal)
                items_bill = ItemCart.objects.all().filter(cart=active_cart)
                items_bill = [ addItemsBill(item_bill, bill) for item_bill in items_bill ]
                bill.save()
                active_cart.total = 0
                active_cart.subtotal = 0
                active_cart.items = 0
                active_cart.save()
                bill = bill_serializer(bill)
                context = {'success':True,'bill':bill, 'items_bill':items_bill}
                return HttpResponse(json.dumps(context,cls=DjangoJSONEncoder), content_type = "application/json")
            else:
                return HttpResponse(json.dumps({'success':False},cls=DjangoJSONEncoder), content_type = "application/json")         
        

def addItemsBill(itemCart, billIn):
    itemBill = ItemBill.objects.create(Product=itemCart.Product, bill=billIn, value=itemCart.value, quantity=itemCart.quantity)
    itemBill.save()
    itemCart.delete()
    total = itemBill.value * itemBill.quantity
    node = Nodes.objects.get(id=itemCart.Product.node.id)
    node.saldo = node.saldo + total
    node.save()
    product = Product.objects.get(id=itemCart.Product.id)
    product.quantity = product.quantity - itemCart.quantity
    product.save()
    return {'id': itemBill.id, 'id_product':itemBill.Product.id, 'name': itemBill.Product.name, 'value': itemBill.value, 'quantity': itemBill.quantity, 'total': total}

def bill_serializer(billIn):
    return {'id':billIn.id, 'total':billIn.total, 'subtotal':billIn.subtotal, 'date':str(billIn.date)}