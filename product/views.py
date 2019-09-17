from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.urls import reverse
from product.forms import newProduct, ImageForm
from django.contrib import messages
from product.models import Product, Image
from nodes.models import Nodes, Node_father
from sales.models import Bill, ItemBill, Cart, ItemCart
from django.views.generic import ListView,CreateView, UpdateView, DeleteView
import json
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from django.core.serializers.json import DjangoJSONEncoder
from django.core import serializers
from django.core.serializers import serialize
import json

# Create your views here.

def index(request):
    return render(request, 'products/index.html')

def checkout(request):
    return render(request, 'products/checkout.html')

def carrito(request):
    cart = Cart.getActiveCart(request,request.user)
    items_cart = ItemCart.objects.filter(cart=cart)
    context = {'cart':cart, 'items_cart':items_cart}
    return render(request, 'products/carrito.html', context)
    
def productPage(request):
    return render(request, 'products/view_product.html')

@login_required(login_url='/login/')
def createProduct(request):
    if request.method == 'POST':
        if Nodes.objects.filter(user_id=request.user.id).exists() == True:         
            if Node_father.objects.filter(node_id=Nodes.objects.get(user_id=request.user.id).id).exists() == True:
                form = newProduct(request.POST)
                if form.is_valid():
                    form.save()
                    value = Node_father.objects.get(node_id=Nodes.objects.get(user_id=request.user.id).id).node_id
                    product = Product.objects.get(id=Product.objects.last().id)
                    product.node_id = value
                    product.save()         
                    messages.success(request,"Producto creado exitosamente")
                    return HttpResponseRedirect(reverse('product_image', args=[Product.objects.last().id]))
                else:
                    return render(request,'base/notification.html')   
            else:
                notification = "No eres tienda, registrate en Neuromarker y empieza a crear tu red de tiendas."
                nodo = "nodo"
                context = {'notification':notification,'nodo':nodo }
                return render(request,'base/notification.html',context)
        else:
                notification = "No eres vendedor, registrate como vendedor en Neuromarker y asociate a una tienda."
                nodo = "vendedor"
                context = {'notification':notification,'nodo':nodo }
                return render(request,'base/notification.html',context)     
    else:
        if Nodes.objects.filter(user_id=request.user.id).exists() == True:         
            if Node_father.objects.filter(node_id=Nodes.objects.get(user_id=request.user.id).id).exists() == True:
                form = newProduct()
                context = {'form':form} 
            else:
                notification = "No eres tienda, registrate en Neuromarker y empieza a crear tu red de tiendas."
                nodo = "nodo"
                context = {'notification':notification,'nodo':nodo }
                return render(request,'base/notification.html',context)
        else:
                notification = "No eres vendedor, registrate como vendedor en Neuromarker y asociate a una tienda."
                nodo = "vendedor"
                context = {'notification':notification,'nodo':nodo }
                return render(request,'base/notification.html',context)   
    return render(request,'products/newProduct.html', context)


@login_required(login_url='/login/')
def uploadImage(request,id):
    if request.method == 'POST':
            form = ImageForm(request.POST, request.FILES)
            if form.is_valid():
                newdoc = Image(filename = request.POST['filename'],docfile = request.FILES['docfile'])
                newdoc.save(form)
                ruta=request.FILES.get('docfile').name
                object = Product()
                product = Product.objects.get(id=id)
                product.picture="./images/"+ruta
                product.save()         
                messages.success(request,'Imagen actualizada exitosamente')
            return HttpResponseRedirect(reverse('products_list'))
    else:
            product = Product.objects.get(id=id)
            form = ImageForm()
            context = {'product':product,'form':form}              
    return render(request, "products/image_product.html",context)


def listProduct(request):
    if request.user.is_active:
        cart = Cart.getActiveCart(request,request.user)
        items_cart = ItemCart.objects.filter(cart=cart)
        product = Product.objects.all()
        context = {'products':product, 'cart':cart, 'items_cart':items_cart} 
        return render(request,'products/list_products.html',context)
    else:
        product = Product.objects.all()
        context = {'products':product} 
        return render(request,'products/list_products.html',context)




@login_required(login_url='/login/')
def listProducts(request):

    if Node_father.objects.filter(node_id=Nodes.objects.get(user_id=request.user.id).id).exists() == True:
        nodes = Nodes.objects.get(user_id=request.user.id)
        products = Product.objects.all().filter(node_id=nodes.id)
        context = {'products':products}
        return render(request,'products/list_my_product.html',context)
    else:
        notification = "No eres tienda, registrate en Neuromarker y empieza a crear tu red de tiendas."
        nodo = "nodo"
        context = {'notification':notification,'nodo':nodo }
        return render(request,'base/notification.html',context)   



def viewDetaillProduct(request, id):
    if request.user.is_active:
        cart = Cart.getActiveCart(request,request.user)
        items_cart = ItemCart.objects.filter(cart=cart)
        product = Product.objects.get(id=id)
        print(product.restriction)
        if product.restriction  == True:
            print(request.user.id)
            if request.user.id is None:
                return render(request,'auth/login.html') 
            else:
                context = {'product':product, 'cart':cart, 'items_cart':items_cart}
                return render(request,'products/view_product.html',context)    
        else:
            context = {'product':product, 'cart':cart, 'items_cart':items_cart}
            return render(request,'products/view_product.html',context)
    else:
        product = Product.objects.get(id=id)
        print(product.restriction)
        if product.restriction  == True:
            print(request.user.id)
            if request.user.id is None:
                return render(request,'auth/login.html') 
            else:
                context = {'product':product}
                return render(request,'products/view_product.html',context)    
        else:
            context = {'product':product}
            return render(request,'products/view_product.html',context)


@login_required(login_url='/login/')
@csrf_exempt
def moreQuantity(request, ide):
    if request.method == "POST": #os request.GET()
        var = request.POST['mach2']
        product = Product.objects.all().filter(id=var)
        for object in product:
            object.quantity = object.quantity + int(request.POST['recipient-name'])
            object.save()
        return render(request,'products/list_my_product.html')
    return render(request,'products/list_my_product.html')

@login_required(login_url='/login/')
@csrf_exempt
def discountProduct(request, ide):
    if request.method == "POST": #os request.GET()
        var = request.POST['mach3']
        print(var)
        product = Product.objects.all().filter(id=var)
        for object in product:
            object.discount = int(request.POST['recipient-name'])
            object.save()
        return render(request,'products/list_my_product.html')
    return render(request,'products/list_my_product.html')

@login_required(login_url='/login/')
@csrf_exempt
def minusQuantity(request, ide):
    if request.method == "POST": #os request.GET()
        var = request.POST['mach']
        product = Product.objects.all().filter(id=var)
        for object in product:
            object.quantity = object.quantity - int(request.POST['recipient-name'])
            object.save()
        return render(request,'products/list_my_product.html')
    return render(request,'products/list_my_product.html')

def listProductsByCategory(request):
    if request.is_ajax:
        if request.method == 'GET':
            categoryIn = request.GET.get('categoryIn')
            products = Product.objects.all().filter(category=categoryIn)
            products = [ product_serializer(product) for product in products]
            return HttpResponse(json.dumps(products,cls=DjangoJSONEncoder), content_type = "application/json")

def listProductsJSON(request):
    if request.is_ajax:
        if request.method == 'GET':
            products = Product.objects.all()
            products = [ product_serializer(product) for product in products]
            return HttpResponse(json.dumps(products,cls=DjangoJSONEncoder), content_type = "application/json")

def product_serializer(product):
    return {'id': product.id, 'name': product.name, 'category': product.category, 'value': product.value, 'picture':str(product.picture)}