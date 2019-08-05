from django.shortcuts import render
from nodes.models import Nodes, Comission
from product.models import Product
from sales.models import Bill, ItemBill
from django.contrib.auth.models import User

# Create your views here.
    
def createSalesCode(request, ide):
    if request.method == "POST": #os request.GET()
        codePost = request.POST['codeSale']
        codeLen = len(codePost)
        code = codePost[codeLen-1]
        node = Nodes.objects.get(id=int(code))
        product = Product.objects.get(id=ide)
        comission=node.percentage_commission * product.value
        user = User.objects.get(id=request.user.id)
        Bill.objects.create(user=user)
        bill = Bill.objects.all().last()
        ItemBill.objects.create(Product=product,bill=bill,value=product.value, quantity=request.POST['quantity'])
        bill.node_id = node.id 
        bill.total = int(product.value) * int(request.POST['quantity'])
        bill.save()
        moreComittion(node.id)
        valueComission = (int(node.percentage_commission)/100)*int(product.value)
        Comission.objects.create(value_commision=valueComission, type_payment='CODIGO', type_commission='REFERIDO', current_balance=comission,node=node.user)       
        comission = Comission.objects.all().last()
        comission.node_id = node.id 
        comission.save() 
        return render(request, "products/index.html")
    product = Product.objects.get(id=ide) 
    context = {'product':product}
    return render(request,'products/view_product.html',context)


def moreComittion(idSeller):
    count = Bill.objects.all().filter(node_id=idSeller).count()
    node = Nodes.objects.get(id=idSeller)
    if count == 30:
        node.percentage_commission = node.percentage_commission + 3
        node.save()
    if count == 60:
        node.percentage_commission = node.percentage_commission + 3
        node.save()
    if count == 90:
        node.percentage_commission = node.percentage_commission + 3
        node.save()
    if count == 100:
        node.percentage_commission = node.percentage_commission + 1
        node.save()
