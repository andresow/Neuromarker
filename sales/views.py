from django.shortcuts import render
from nodes.models import Nodes, Comission
from product.models import Product
from sales.models import Bill, ItemBill
from django.contrib.auth.models import User

from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.core.serializers.json import DjangoJSONEncoder
from django.core import serializers
from django.core.serializers import serialize
import json
from django.cotrib.auth.decorators import login_required

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


def addProductShoppingCart(request):
    if request.is_ajax:
        if request.method == 'GET':
            active_sale = Bill.getActiveSale(request, request.user) #MIRAR LO DEL REQUESTUSER
            productIn = request.GET.get('productIn')
            product = Product.objects.get(id=productIn)
            item_cart = ItemBill.objects.create(Product=product,bill=active_sale,value=product.value, quantity=1)
            item_cart = item_bill_serializer(item_cart, product.name, str(product.picture))
            active_sale.total += product.value
            active_sale.save()
            context = {'id_bill':active_sale.id,'total_sale':active_sale.total, 'item_cart':item_cart}
            print(context)
            return HttpResponse(json.dumps(context,cls=DjangoJSONEncoder), content_type = "application/json")

def item_bill_serializer(item_bill, name_product, picture_product):
    return {'id': item_bill.id, 'id_product':item_bill.Product.id, 'name': name_product, 'value': item_bill.value, 'quantity': item_bill.quantity, 'picture':picture_product}

def deleteProductShoppingCart(request):
    if request.is_ajax:
        if request.method == 'GET':
            active_sale = Bill.getActiveSale(request, request.user)
            product_delete = request.GET.get('product_delete')
            product = Product.objects.get(id=product_delete)
            item_out = ItemBill.objects.filter(Product=product, bill=active_sale)
            item_out.delete()
            return HttpResponse(json.dumps({"success":"true"},cls=DjangoJSONEncoder), content_type = "application/json")