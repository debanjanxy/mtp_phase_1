from django.shortcuts import render
from django.http import HttpResponse

def index(request):
   return HttpResponse("Hello there! You are looking for wells?")

# Create your views here.
