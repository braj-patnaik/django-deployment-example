from django.shortcuts import render
from basic_app import views

# Create your views here.

def index(request):
    con_dict = {"text":"world Cup","year":"2018"}
    return render(request,'basic_app/index.html',con_dict)

def basic(request):
    return render(request,'basic_app/basic.html')

def other(request):
    return render(request,'basic_app/other.html')

def relative_url_templates(request):
    return render(request,'basic_app/relative_url_templates.html')
