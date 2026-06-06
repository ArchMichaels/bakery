from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return HttpResponse ("welcome home")
    
def aboutus(request):
    return HttpResponse ("Welcome to our aboutus")

def menu(request):
    return HttpResponse ("This is our main menu page")