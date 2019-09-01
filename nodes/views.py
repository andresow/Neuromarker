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
from django.contrib.auth.decorators import login_required


# Create your views here.

def index(request):
    return render(request, 'products/index.html')

@login_required(login_url='/login/')
def createNodeShop(request):
    if request.method == 'POST':
        form = NodesForm(request.POST)
        form2 = NodesCodeForm(request.POST)
        if form.is_valid() and form2.is_valid():
            form.save()
            code = form2['generateCode'].value()
            node = Nodes.objects.all().last()
            Node_father.objects.create(node=Nodes.objects.last(), generateCode=code)
            node.id_father = Node_father.objects.last().node_id
            node.user_id = request.user.id
            node.save()
            messages.success(request,"Nodo agregado exitosamente")
        return HttpResponseRedirect(reverse('list_node'))
    else:
        form = NodesForm()
        form2 = NodesCodeForm()
        context = {'form':form,'form2':form2} 
    return render(request,'nodes/create_node.html', context) 

@login_required(login_url='/login/')
def listNodes(request):
    if Node_father.objects.filter(node_id=Nodes.objects.get(user_id=request.user.id).id).exists() == True:
        print(Node_father.objects.filter(node_id=Nodes.objects.get(user_id=request.user.id).id))
        nodes = Nodes.objects.all().filter(id_father=request.user.id)
        user = User.objects.all()
        print(nodes)
        context = {'nodes':nodes,'user':user }
        return render(request,'nodes/list_node.html',context)
    else:
        notification = "No eres tienda, registrate en Neuromarker y empieza a crear tu red de tiendas."
        nodo = "nodo"
        context = {'notification':notification,'nodo':nodo }
        return render(request,'base/notification.html',context)


@login_required(login_url='/login/')
@csrf_exempt
def editComission(request, id):
    if request.method == "POST": #os request.GET()
        node = Nodes.objects.all().filter(id=id)
        for object in node:
            object.percentage_commission = request.POST['recipient-name']
            object.save()
        return render(request,'nodes/list_node.html')
    return render(request,'nodes/list_node.html')  

@login_required(login_url='/login/')
@csrf_exempt
def deleteNodeMyRed(request, ide):
    if request.method == "POST": #os request.GET()
        var = request.POST['mach2']
        print(var+ "soy yo soy yo")
        node = Nodes.objects.all().filter(id=var)
        for object in node:
            object.id_father = 0
            object.save()
        return render(request,'nodes/list_node.html')
    return render(request,'nodes/list_node.html')  

@login_required(login_url='/login/')
@csrf_exempt
def nodeForCode(request):
    print("voy aqui")
    if request.method == "POST": #os request.GET()
        var =  request.POST['recipient-name2'] 
        nodeFather = Node_father.objects.all().filter(generateCode=var)
        print(var)  
        print(nodeFather)
        for object in nodeFather:
            print(percentage_commission(object.node_id))
            print(object.node_id)
            user = User.objects.get(id=request.user.id)
            userName = user.first_name 
            Nodes.objects.create(user=user,is_red=False, name=userName, percentage_commission=percentage_commission(object.node_id),id_father=object.node_id)
            print("creo")
        return render(request,'nodes/list_node.html')
    return render(request,'nodes/list_node.html')  

def percentage_commission(value):
    
    node = Nodes.objects.all().filter(id_father=value) 
    for object in node:
        comission = object.percentage_commission
        return  comission
