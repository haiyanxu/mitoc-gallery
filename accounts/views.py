from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from imagestore import templates

# Create your views here.

def signup(request):
    if request.method == 'POST':
        if User.objects.filter(username=request.POST['username']).exists():
            return render(request, 'accounts/signup.html', {'error':'Username has already been taken'})
        elif User.objects.filter(email=request.POST['emailaddress']).exists():
            return render(request, 'accounts/signup.html', {'error':'Email has already been taken'})
        elif request.POST['password1'] != request.POST['password2']:
            return render(request, 'accounts/signup.html', {'error':'Passwords didn\'t match'})
        else:
            user = User.objects.create_user(request.POST['username'], password=request.POST['password1'], email=request.POST['emailaddress'])
            login(request, user)
            return render(request, 'imagestore/album_list.html', {'error':'Signup Successful!'})
    else:
        return render(request, 'accounts/signup.html')


def loginview(request):
    if request.method == 'POST':
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is not None:
            login(request, user)
            if 'next' in request.POST:
                return redirect(request.POST['next'])
            return redirect('home')
        else:
            return render(request, 'accounts/login.html', {'error':'Wrong credentials!'})
    else:
        return render(request, 'accounts/login.html')

def logoutview(request):
    if request.method == 'POST':
        logout(request)
        return redirect('home')
