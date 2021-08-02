from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('discover/', views.discover, name="discover"),
    path('login/', views.login, name="login"),
    path('signup/', views.signup, name="signup"),
    path('signout/', views.signout, name="signout"),

]
