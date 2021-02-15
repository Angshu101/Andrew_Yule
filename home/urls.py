from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("",views.index,name='home'),
    path("home",views.index,name='home1'),
    path("contact",views.contact,name='contact')
]
