#from django.contrib import admin
from django.urls import path
#from . import views
from littleLemon import views 
         

urlpatterns = [
    path('dishes/<str:dish>/',views.menuitems)
    
    
]