from django.contrib import admin
from django.urls import path
from pj3 import views

urlpatterns = [
    path('', views.index, name='home'),
    path('register', views.register, name='register'),
    path('employees', views.employees, name='employees'),
]
