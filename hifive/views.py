from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
rooms = [
    {'id':1,'name':"Lets Learn Python"},
    {'id':2,'name':"Lets Learn JS"},
    {'id':3,'name':"Python For AI"},
    {'id':4,'name':"Design with me"},
]


def home(request):
    message = 'My Home page'
    return render(request,'home.html',{"message":message})

def room(request):
    message = 'My Rooms page'
    return render(request,"myrooms.html",{"message":message,"rooms":rooms})