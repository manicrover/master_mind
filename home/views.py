# Create your views here.
from cgitb import html
from django.http import HttpResponse
from django.shortcuts import render
import datetime

# def current_datetime(request):
#     now=datetime.datetime.now()
#     html

def index(request):
    # return HttpResponse("website is working")
    return render(request,"home/index.html")