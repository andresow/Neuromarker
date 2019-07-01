from django.conf.urls import url, include
from product.views import index


urlpatterns = [

    url(r'products/index.html', index),
]