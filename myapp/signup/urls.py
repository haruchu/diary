from django.urls import path
from . import views

app_name = 'signup'
urlpatterns = [
    path('', views.usersignup, name="signup"),
    path('confirm/', views.userconfirm, name="confirm"),
    path('create/', views.usercreate, name="create"),
    path('userLogin/', views.userLogIn, name="userLogIn"),
    path('login/', views.logIn, name="logIn"),
]
