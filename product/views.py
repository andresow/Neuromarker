from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return render(request, 'products/index.html')

def products(request):
    return render(request, 'products/products.html')

def checkout(request):
    return render(request, 'products/checkout.html')

def productPage(request):
    return render(request, 'products/product-page.html')
    