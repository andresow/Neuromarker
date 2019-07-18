from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy,reverse
from django.contrib import messages
from nodes.forms import NodesForm
from nodes.models import Nodes

# Create your views here.

def index(request):
    return render(request, 'products/index.html')
    
def createNode(request):
    if request.method == 'POST':
        form = NodesForm(request.POST)
        print(request.user.id)
        if form.is_valid():
            form.save()
            node = Nodes.objects.all().last()
            node.user_id = request.user.id
            node.save()
            messages.success(request,"Nodo agregado exitosamente")
        return HttpResponseRedirect(reverse('index'))
    else:
        form = NodesForm()
        context = {'form':form} 
    return render(request,'nodes/create_node.html', context) 