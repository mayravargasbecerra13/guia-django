from django.http import HttpResponse
from django.template import loader
"""from django.shortcuts import render


# Create your views here.
def members(request):
    return HttpResponse("Hello, World")"""
    
def members(request):
    template = loader.get_template('myfirst.html')
    return HttpResponse(template.render())