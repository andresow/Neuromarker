from django.conf.urls import url, include
from product.views import *

urlpatterns = [

    url(r'products/index.html', index),
    url(r'products/list_products.html', listProduct, name='products_list'),
    url(r'products/checkout.html', checkout),
    url(r'products/newProduct.html', createProduct, name='product_create'),
    url(r'products/image_product.html/(?P<id>\d+)/$', uploadImage, name='product_image'),
    url(r'products/view_product.html/(?P<id>\d+)/', viewDetaillProduct, name='product_detaills'),
    url(r'products/list_my_products.html', listProducts, name='list_products'),
    url(r'products/more_quantity.html/(?P<id>\d+)/', editQuantity, name='edit_quantity'),

]