from django.http import Http404
from django.http import HttpResponse
from django.shortcuts import render
from .models import Service


def index(request):
    return render(request, "appoffin/index.html")


def services(request):
    getdetails = Service.objects.all()
    context = {"getdetails": getdetails}
    return render(request, "appoffin/services.html", context)


def virtualhr(request):
    response = "We Provide All Type Of Virtal HR Manager Service."
    return HttpResponse(response)


def acservice(request, serv_id):
    response = "We Provide All Type Of Accounting  Management Service."
    return HttpResponse(response)

# def Services(request):
#     try:
#         getdetails = Service.objects.get(pk=service_id)
#     except Service.DoesNotExist:
#         raise Http404("Service Does Not Exist")
#     context = {"getdetails": getdetails}
#     return render(request, "appoffin/Info.html", {"getdetails": getdetails})
