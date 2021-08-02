from django.shortcuts import get_object_or_404, render,redirect
from django.contrib.auth.models import User
from django.contrib import auth

def home(request) :
  return render(request, 'index.html')

def login(request) :
  if request.method =='POST':
    email = request.POST['email']
    password = request.POST['password']

    user = auth.authenticate(request, username=email, password=password)
    print(user)
    if user is None:
      return redirect('/signup')
    else:
      auth.login(request,user)
      return redirect('/')
  return render(request, 'login.html')

def signup(request) :
  if request.method =='POST':
    email = request.POST['email']
    password = request.POST['password']

    User.objects.create_user(username=email, password=password)
    return redirect('/login')
  return render(request, 'signup.html')

def signout(request) :
  auth.logout(request)

  return redirect('/')

def discover(request) :
  return render(request, 'discover.html')
