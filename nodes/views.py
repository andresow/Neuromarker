from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy,reverse
from django.contrib import messages
from nodes.forms import NodesForm,NodesCodeForm
from nodes.models import Nodes, Node_father
from django.contrib.auth.models import User
import json
from django.views.decorators.csrf import csrf_exempt


# Create your views here.

def index(request):
    return render(request, 'products/index.html')
    
def createNodeShop(request):
    if request.method == 'POST':
        form = NodesForm(request.POST)
        form2 = NodesCodeForm(request.POST)
        if form.is_valid() and form2.is_valid():
            form.save()
            code = form2['generateCode'].value()
            node = Nodes.objects.all().last()
            node.user_id = request.user.id
            node.save()
            Node_father.objects.create(node=Nodes.objects.last(), generateCode=code)
            node.id_father = Node_father.objects.last().id
            messages.success(request,"Nodo agregado exitosamente")
        return HttpResponseRedirect(reverse('index'))
    else:
        form = NodesForm()
        form2 = NodesCodeForm()
        context = {'form':form,'form2':form2} 
    return render(request,'nodes/create_node.html', context) 

def listNodes(request):

    nodes = Nodes.objects.all().filter(user_id=request.user.id)
    user = User.objects.all()
    print(nodes)
    context = {'nodes':nodes,'user':user }
    return render(request,'nodes/list_node.html',context)

@csrf_exempt
def editComission(request, id):
    if request.method == "POST": #os request.GET()
        node = Nodes.objects.all().filter(id=id)
        for object in node:
            object.percentage_commission = request.POST['recipient-name']
            object.save()
        return render(request,'nodes/list_node.html')
    return render(request,'nodes/list_node.html')   

@csrf_exempt
def nodeForCode(request):
    if request.method == "POST": #os request.GET()
        var =  request.POST['recipient-name2']   
        nodeFather = Node_father.objects.all().filter(generateCode=var)
        primaryNode = Nodes.objects.all().filter(id_father=nodeFather.id) 
        user = User.objects.all().filter(id=request.user.id)
        Nodes.objects.create(user=user,is_red=True, name=request.user.first_name, percentage_commission=primaryNode.percentage_commission,id_father=nodeFather.id)
        print("creo")
        return render(request,'nodes/list_node.html')
    return render(request,'nodes/list_node.html')   


