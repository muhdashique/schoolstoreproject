

from . import views

from django.urls import path

urlpatterns = [


    path('register', views.register, name='register'),
    path('login', views.login, name='login'),
    path('form', views.form, name='form'),
    path('home', views.home, name='home'),
    path('msg', views.msg, name='msg'),






]









