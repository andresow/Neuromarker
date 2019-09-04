from django.conf.urls import url, include
from sales.views import *
from django.contrib.auth.decorators import login_required

urlpatterns = [

    url(r'sales/sales_code/(?P<ide>\d+)/', createSalesCode, name='createSalesCode'),
    url(r'sales/add_product_cart/', addProductShoppingCart, name='addProductCart'),
    url(r'sales/delet_item_cart/', deleteProductShoppingCart, name='deleteProductCart'),
    url(r'sales/finish_sale/', finishSale, name='finishSale'),

]
