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
        username = request.POST.get('username') 
        fname = request.POST['fname']
        lname = request.POST['lname']
        phone = request.POST['phone'] 
        email = request.POST['email']
        password = request.POST['password']
        cpassword = request.POST['cpassword']

        #Check erroeneous inputs
        # if phone (unique != True)
        if password != cpassword :
             return HttpResponse('document.getElementById("err").innerHTML = setUp.passE;') and redirect (signuppage)
        
        if len (phone) < 10:
             return HttpResponse('document.getElementById("err").innerHTML = setUp.phpneE;') and redirect (signuppage)
             

        #Create the user
        myuser = User.objects.create_user(username = username , email = email, password = password)
        myuser.first_name = fname
        myuser.last_name = lname
        myuser.save()
        print('hello')
        
        return HttpResponse('document.getElementById("succ").innerHTML = setUpss.msg;') and  redirect('login') 

    else:
            return HttpResponse('404 - Not Found')    
            # print(error)
