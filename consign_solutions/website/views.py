from django.shortcuts import render
from django.urls import path
from.models import countdown
from. import views
def index(request):
    time=countdown.objects.all()
    return render(request,'index.html',{'time':time})


# Create your views here.
