from django.http import Http404
from django.http import HttpResponse
from django.shortcuts import render
from django.template.response import TemplateResponse

def index(request):
    return render(request, "index.html")