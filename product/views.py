from django.shortcuts import render
from django.http import HttpResponse
from product.forms import newProduct
from product.models import Product

# Create your views here.

def index(request):
    return render(request, 'products/index.html')

def products(request):
    return render(request, 'products/products.html')

def checkout(request):
    return render(request, 'products/checkout.html')

def productPage(request):
    return render(request, 'products/product-page.html')

def createProduct(request):
    if request.method == 'POST':
        form = newProduct(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"Producto creado exitosamente")
        return HttpResponseRedirect(reverse('index'))
    else:
        form = newProduct()
        context = {'form':form} 
    return render(request,'products/newProduct.html', context)