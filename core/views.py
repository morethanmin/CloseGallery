from django.shortcuts import get_object_or_404, render,redirect
from django.contrib.auth.models import User
from django.contrib import auth
from .models import Main_event_slide as eventModel, Weekly_painting as Weekly_painting_Model,Season_painting as Season_painting_Model,Review_user as Review_user_model, Review_celebrity as Review_celebrity_model, Painting as PaintingModel


def home(request) :
  events = eventModel.objects.filter()
  weeklys = Weekly_painting_Model.objects.filter()
  seasons = Season_painting_Model.objects.filter()
  # 길이 제한 필요
  Review_users = Review_user_model.objects.filter()
  Review_celebritys = Review_celebrity_model.objects.filter()

  return render(request, 'index.html',{"events":events,"weeklys": weeklys, "seasons":seasons,"Review_users":Review_users,"Review_celebritys":Review_celebritys})

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
  return render(request, 'login/index.html')

def signup(request) :
  if request.method =='POST':
    email = request.POST['email']
    password = request.POST['password']

    User.objects.create_user(username=email, password=password)
    return redirect('/login')
  return render(request, 'signup/index.html')

def signout(request) :
  auth.logout(request)

  return redirect('/')

def discover(request) :
  paintings = PaintingModel.objects.filter()
  
  return render(request, 'discover/index.html',{"paintings":paintings})
