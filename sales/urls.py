from django.conf.urls import url, include
from sales.views import *
from django.contrib.auth.decorators import login_required

urlpatterns = [

    url(r'sales/sales_code/(?P<ide>\d+)/', createSalesCode, name='createSalesCode'),

]
