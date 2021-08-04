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

def paintings(request) :
  paintings = PaintingModel.objects.filter()
  
  return render(request, 'painting/index.html',{"paintings":paintings})

def painting(request,pk) :
  painting = get_object_or_404(PaintingModel, pk = pk)

  return render(request, 'painting/_pk.html',{"painting":painting})

def review_users(request) :
  reviews = Review_user_model.objects.filter()

  return render(request, 'review/user/index.html',{"reviews":reviews})

def review_user(request,pk) :
  review = get_object_or_404(Review_user_model, pk = pk)

  return render(request, 'review/user/_pk.html',{"review":review})



def review_celebritys(request) :
  # reviews = Review_celebrity_model.objects.filter()

  return render(request, 'review/celebrity/index.html')

def review_celebrity(request,pk) :
  # review = get_object_or_404(Review_celebrity_model, pk = pk)

  return render(request, 'review/celebrity/_pk.html')
