from django.shortcuts import render
from .models import Package



# Create your views here.
def packages(request):
        getdetails = Package.objects.all()
        context = {"getdetails": getdetails}
        return render(request, "appoftra/packages.html", context)

def info(request, pid):
    # fetch the services using id
    know = Package.objects.filter(id=pid)
    # print(know)
    return render(request, "appoftra/info.html", {'knows': know[0]})