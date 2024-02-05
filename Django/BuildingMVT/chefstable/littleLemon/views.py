from django.shortcuts import render
from django.http import HttpResponse

#from datetime import datetime


# Create your views here.

def menuitems(request, dish):
    items = {
        "pasta":'from Italy',
        "pastry":'from London',
        "sushi":'from Japan'
    }

    description = items[dish]
    return HttpResponse(f"<h2>{dish}</h2>" + description)
   


    
 
