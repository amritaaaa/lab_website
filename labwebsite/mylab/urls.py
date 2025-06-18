#from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('login', views.loginform , name='login'),
    path('signup', views.signupform , name='signup'),
    path('logout', views.logout , name='logout'),
    path('studentinformation',views.studentinformation,name='studentinformation'),
]