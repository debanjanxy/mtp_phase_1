from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def index(request):
    templates = loader.get_template('findwell/index.html')
    return render(request, 'findwell/index.html')
    # return HttpResponse(templates.render(request,'findwell/index.html'))

# Create your views here.
