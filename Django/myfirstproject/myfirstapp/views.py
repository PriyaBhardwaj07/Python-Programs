from django.shortcuts import render
from django.http import HttpResponse,JsonResponse

# Create your views here.
def myfuctioncall(request):
    return HttpResponse("Hello World")

def myfuctionabout(request):
    return HttpResponse("About Response")

def add(request,a,b): # def add(request,x,y)
    return HttpResponse(a+b) # return HttpResponse(x+y) 
# if here we take x ,y instead of a and b it won't work gives a type error
# it is because in URL file i have written a,b will be passed as parameter and here i have passed x,y

def intro(request,name,age):
    mydict ={
        "name":name,
        "age":age
    }
    return JsonResponse(mydict) # jsonresponse take dictionary as a parameter