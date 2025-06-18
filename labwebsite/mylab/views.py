from django.shortcuts import render, HttpResponse, redirect
#from .forms import LoginForm , RegistrationForm
from .models import user_signup
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login



# Create your views here.
def index(request):
    return render(request,'index.html')

def loginform(request):
    if request.method == 'POST':
        loginusername=request.POST['username']
        loginpassword=request.POST['password']

        print(loginusername)
        print(loginpassword)



        if user_signup.objects.filter(email_id=loginusername,password=loginpassword).exists():
            # Display an success message if the username does exist

            print("hello hello")
            user = authenticate(request, email_id=loginusername, password=loginpassword)
            return redirect("studentinformation")
        return render(request,"signup_page.html")



    return render(request,'loginpage.html')


def signupform(request):
    if request.method == 'POST':
        fname=request.POST['first_name']
        lname = request.POST['last_name']
        email = request.POST['email_id']
        pwd = request.POST['password']

        user=user_signup.objects.create()
        user.first_name=fname
        user.last_name=lname
        user.email_id=email
        user.password=pwd


        user.save()
        messages.success(request,"your account has been successfullly created")
        return redirect('index')

    return render(request, "signup_page.html")

def logout(request):
    try:
        del request.session['user']
    except:
        return redirect('login')
    return redirect('login')

def studentinformation(request):
    return render(request,'studentinformation.html')