from django.conf.urls import url, include
from nodes.views import *
from django.contrib.auth.decorators import login_required

urlpatterns = [
    url(r'products/index.html', index,  name='index'),
    url(r'nodes/create_node.html', createNode, name='create_node'),
    
]

