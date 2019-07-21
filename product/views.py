from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.urls import reverse
from product.forms import newProduct, ImageForm
from django.contrib import messages
from product.models import Product, Image
from nodes.models import Nodes, Node_father
from django.views.generic import ListView,CreateView, UpdateView, DeleteView

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
                    productId = Product.objects.last().id
                    print(productId)
                    product = Product.objects.filter(id = productId)
                    product.node_id = value
                    print(Product.objects.filter(node_id=3))
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

def viewDetaillProduct(request, id):

		product = Product.objects.get(id=id)
		context = {'product':product}
		return render(request,'products/view_product.html',context)