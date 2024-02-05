from django.urls import path
from . import views

urlpatterns =[
    path('',views.myfuctioncall,name="index"),
    path('about',views.myfuctionabout,name="about"),
    path('add/<int:a>/<int:b>',views.add,name="add"), # this is used for integer value 
    path('intro/<str:name>/<int:age>',views.intro,name="intro")
    
]
