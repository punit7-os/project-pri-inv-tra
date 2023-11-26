from django.http import Http404
from django.http import HttpResponse
from django.shortcuts import render
from .models import Service
from django.template.response import TemplateResponse



# def index(request):
#     return render(request, "appoffin/index.html")


def services(request):
    getdetails = Service.objects.all()
    context = {"getdetails": getdetails}
    return render(request, "appoffin/services.html", context)


def info(request, mid):
    # fetch the services using id
    know = Service.objects.filter(id=mid)
    # print(know)
    return render(request, "appoffin/info.html", {'knows': know[0]})


def about(request):
    return render(request, "appoffin/about.html")



# def Services(request):
#     try:
#         getdetails = Service.objects.get(pk=service_id)
#     except Service.DoesNotExist:
#         raise Http404("Service Does Not Exist")
#     context = {"getdetails": getdetails}
#     return render(request, "appoffin/Info.html", {"getdetails": getdetails})
