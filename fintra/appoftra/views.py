from django.shortcuts import render
from .models import packages



# Create your views here.
def packages(request):
    return render(request, "appoftra/packages.html")
