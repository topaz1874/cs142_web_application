from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.core.urlresolvers import reverse    
from django.shortcuts import render
from django.http import HttpResponseRedirect

from .models import MyUser
from .forms import RegisterForm,LoginForm
# Create your views here.
def register(request):
    # render form and receive data from post method
    form = RegisterForm(request.POST or None)

    if form.is_valid():
        username = form.cleaned_data['username']
        email = form.cleaned_data['email']
        password = form.cleaned_data['password1']
        MyUser.objects.create_user(
            username=username,
            email=email,
            password=password,)
        return HttpResponseRedirect('login')
    return render(request, 'accounts/register.html', {'form':form})

def auth_login(request):
    if request.user.is_authenticated():
        messages.warning(request,"You've been login.")
        return HttpResponseRedirect(reverse('photo:photoindex'))
    form = LoginForm(request.POST or None)
    next_url = request.GET.get('next',None) or reverse('photo:photoindex')
    if form.is_valid():
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect((next_url))
    return render(request, 'accounts/login.html', {'form':form})

def auth_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('photo:photoindex'))

