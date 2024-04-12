from django.http import Http404
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.template.response import TemplateResponse
from appoffin.models import Service
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

def index(request):
    getdetails = Service.objects.all()
    context = {"getdetails": getdetails}
    return render(request, "index.html", context)

def loginpage(request):
    messages.success(request,'Welcome to login page')
    return render(request, "login.html")

def signuppage(request):
    messages.success(request,'Welcome to Login')
    return render(request, "signup.html")

def handleSignup(request):
    
    if request.method == "POST":
         #Get the parameters
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        phone = request.POST['phone'] 
        email = request.POST['email']
        password = request.POST['password']
        cpassword = request.POST['cpassword']

        #Check erroeneous inputs
        if len(fname) < 3 or len(phone) < 10 or len(email) < 4 or (len(password) <6 and password != cpassword):
             messages.error(request,"Please Fill The Details Correctly")

        else:
             myuser = User.objects.create_user(username = username , email = email, password = password)
             myuser.first_name = fname
             myuser.last_name = lname
             myuser.save()
             messages.success(request,"You've Signed up Successfully")
        # print('hello')
        # HttpResponse('document.getElementById("succ").innerHTML = setUpss.msg;') and  
        
        return redirect('loginpage') 
                
        # if phone (unique != True)
        # if password != cpassword :
        #      return HttpResponse('document.getElementById("err").innerHTML = setUp.passE;') and redirect (signuppage)
        
        # if len (phone) < 10:
        #      return HttpResponse('document.getElementById("err").innerHTML = setUp.phpneE;') and redirect (signuppage)
             

        #Create the user
       

    # else:
    #         return HttpResponse('404 - Not Found')    
            # print(error)
    

def handleLogin(request):
     
     if request.method == "POST":
         #Get the parameters
        loginusername = request.POST['loginusername']
        loginpass = request.POST['loginpass'] 

        user = authenticate(username = loginusername, password = loginpass)

        if user is not None:
             login(request,user)
             return redirect("/")
        else:
            HttpResponse ("error logout message")
     return HttpResponse("handleLogin")


def handleLogout(request):
     return HttpResponse("logout")