from django.conf.urls import url, include
from nodes.views import *
from django.contrib.auth.decorators import login_required

urlpatterns = [

    url(r'products/index.html', index,  name='index'),
    url(r'nodes/create_node.html', createNodeShop, name='create_node'),
    url(r'nodes/list_node.html', listNodes, name='list_node'),
    url(r'nodes/list_comission.html/(?P<id>\d+)/', editComission, name='edit_comission'),
    url(r'nodes/insert_code_father.html', nodeForCode, name='insert_code'),


]

