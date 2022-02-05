from multiprocessing import context
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login,  logout
from django.contrib import messages

def home(request):
    return render(request,"home.html")

def signup(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        if User.objects.filter(username=username).exists():
            messages.info(request,'Username Taken')
            return redirect('signup')
        myuser = User.objects.create_user(username = username,email = email,password = password,first_name = name)
        myuser.save()
        messages.success(request,"Your account is successfully created.")
        return redirect('signin')
    return render(request,"signup.html")

def signin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username,password=password)

        if user is not None:
            login(request,user)
            context = {'name' : user.first_name}
            return render(request,'home.html',context)
        
        else:
            messages.error(request,'Bad Credentials')
            return redirect('signin')
    return render(request,"signin.html")

def signout(request):
    logout(request)
    messages.success(request,"Logged Out Successfully")
    return redirect('home')