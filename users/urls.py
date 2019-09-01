from django.conf.urls import url, include
from users.views import *
from django.contrib.auth.decorators import login_required

urlpatterns = [

    url(r'products/index.html', createUser,  name='index'),
    url(r'users/create_users.html', createUser, name='create_users'),

]

