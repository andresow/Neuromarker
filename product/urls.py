from django.conf.urls import url, include
from product.views import *


urlpatterns = [

    url(r'products/index.html', index),
    url(r'products/products.html', products),
    url(r'products/checkout.html', checkout),
    url(r'products/product-page.html', checkout),


]