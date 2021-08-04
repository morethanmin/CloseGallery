from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('painting/', views.paintings, name="paintings"),
    path('painting/<int:pk>/', views.painting, name="painting"),
    path('review/user/', views.review_users, name="review_users"),
    path('review/user/<int:pk>/', views.review_user, name="review_user"),
    path('review/celebrity/', views.review_celebritys, name="review_celebritys"),
    path('review/celebrity/<int:pk>/', views.review_celebrity, name="review_celebrity"),
    path('login/', views.login, name="login"),
    path('signup/', views.signup, name="signup"),
    path('signout/', views.signout, name="signout"),

]
