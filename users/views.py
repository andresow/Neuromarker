from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy,reverse
from django.contrib import messages
from users.forms import UserForm, ProfileForm
from users.models import Profile
from nodes.models import Nodes
from django.contrib.auth.models import User
from django.views.generic import ListView,CreateView, UpdateView, DeleteView
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required,permission_required
from django.contrib.auth.mixins import LoginRequiredMixin,PermissionRequiredMixin
from django.contrib.auth.models import Permission

# Create your views here.
def index(request):
    return render(request, 'products/index.html')

def createUser(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        form2 = ProfileForm(request.POST)
        if form.is_valid() and form2.is_valid():
            form.save()
            form2.save()
            profile = Profile.objects.all().last()
            profile.user_id = User.objects.all().last().id
            profile.save()
            messages.success(request,"Usuario creado exitosamente")
        return HttpResponseRedirect(reverse('index'))
    else:
        form = UserForm()
        form2 = ProfileForm()
        context = {'form':form,'form2':form2} 
    return render(request,'users/create_user.html', context) 


def userLogin(request):
	
        context = {}
        if request.method == "POST":
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                if request.GET.get('next', None):
                    return HttpResponseRedirect(request.GET['next'])
                return HttpResponseRedirect(reverse('index'))
            else:
                context["error"] = "Provide valid credentials !!"
                return render(request, "auth/login.html", context)
        else:
            return render(request, "auth/login.html", context)

def success(request):

    context = {}
    context['user'] = request.user
    return render(request, "auth/success.html", context)

def userLogout(request):

		logout(request)
		return HttpResponseRedirect(reverse('userLogin'))

