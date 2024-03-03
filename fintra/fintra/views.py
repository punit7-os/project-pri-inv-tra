from django.http import Http404
from django.http import HttpResponse
from django.shortcuts import render
from django.template.response import TemplateResponse
from appoffin.models import Service

def index(request):
    getdetails = Service.objects.all()
    context = {"getdetails": getdetails}
    return render(request, "index.html", context)

def login(request):
    return render(request, "login.html")

def signup(request):
    return render(request, "signup.html")