from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def index(request):

    # return HttpResponse("Welcome to the Health Centre!")
    return render(request,"HealthCentre/index.html")