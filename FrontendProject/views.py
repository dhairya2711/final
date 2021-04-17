from django.shortcuts import render, HttpResponse
from django.template import loader


# Create your views here.
def index(req):
    template = loader.get_template('index.html')
    return HttpResponse(template.render())
