from django.http import Http404
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.template.response import TemplateResponse
from appoffin.models import Service
from django.contrib.auth.models import User

def index(request):
    getdetails = Service.objects.all()
    context = {"getdetails": getdetails}
    return render(request, "index.html", context)

def login(request):
    return render(request, "login.html")

def signuppage(request):
    return render(request, "signup.html")

def handleSignup(request):
    if request.method == "POST":
         #Get the parameters
        name = request.POST['name']
        email = request.POST['email']
        # phone = request.POST['phone'] 
        password = request.POST['password']
        cpassword = request.POST['cpassword']

        #Check erroeneous inputs


        #Create the user
        myuser = User.objects.create_user(name,email,password)
        myuser.save()
        print(name)
        
        return HttpResponse('msg') and redirect('login')  

    else:
            return HttpResponse('404 - Not Found')    
    print(error)
