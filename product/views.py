from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.urls import reverse
from product.forms import newProduct, ImageForm
from django.contrib import messages
from product.models import Product, Image
from nodes.models import Nodes, Node_father
from django.views.generic import ListView,CreateView, UpdateView, DeleteView
import json
from django.views.decorators.csrf import csrf_exempt

from django.core.serializers.json import DjangoJSONEncoder
from django.core import serializers
from django.core.serializers import serialize
import json

# Create your views here.

def index(request):
    return render(request, 'products/index.html')

def checkout(request):
    return render(request, 'products/checkout.html')

def productPage(request):
    return render(request, 'products/view_product.html')

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
                print("Usted no es una tienda")
        else:
               print("Usted no es una tienda x2")     
    else:
        if Nodes.objects.filter(user_id=request.user.id).exists() == True:         
            if Node_father.objects.filter(node_id=Nodes.objects.get(user_id=1).id).exists() == True:
                form = newProduct()
                context = {'form':form} 
            else:
                print("Usted no es una tienda")
        else:
               print("Usted no es una tienda x2")  
    return render(request,'products/newProduct.html', context)


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
            return HttpResponseRedirect(reverse('index'))
    else:
            product = Product.objects.get(id=id)
            form = ImageForm()
            context = {'product':product,'form':form}              
    return render(request, "products/image_product.html",context)

def listProduct(request):

		product = Product.objects.all()
		context = {'products':product}
		return render(request,'products/list_products.html',context)

def listProducts(request):

    nodes = Nodes.objects.get(user_id=request.user.id)
    products = Product.objects.all().filter(node_id=nodes.id)
    print(nodes.id)
    context = {'products':products}
    print(products)
    return render(request,'products/list_my_product.html',context)

def viewDetaillProduct(request, id):

		product = Product.objects.get(id=id)
		context = {'product':product}
		return render(request,'products/view_product.html',context)


@csrf_exempt
def editQuantity(request, id):
    if request.method == "POST": #os request.GET()
        product = Product.objects.all().filter(id=id)
        for object in product:
            object.quantity = object.quantity + int(request.POST['recipient-name'])
            object.save()
        return render(request,'products/list_my_product.html')
    return render(request,'products/list_my_product.html')

def listProductsByCategory(request):
    if request.is_ajax:
        if request.method == 'GET':
            categoryIn = request.GET.get('categoryIn')
            print("funciona? : "+categoryIn)
            products = Product.objects.all().filter(category=categoryIn)
            products = [ product_serializer(product) for product in products]
            return HttpResponse(json.dumps(products,cls=DjangoJSONEncoder), content_type = "application/json")

def product_serializer(product):
    print(product.picture)
    return {'id': product.id, 'name': product.name, 'category': product.category, 'value': product.value, 'picture':str(product.picture)}