from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.core.mail import send_mail
from django.views.decorators.csrf import csrf_exempt
from .models import OTP_db
import random
# @csrf_exempt
# def home(request):
#     return render(request,"signup.html")

@csrf_exempt
def Logout(request):
    logout(request)
    login_link='login'
    login_label='Log In'
    if request.user.is_authenticated:
        login_link='logout'
        login_label="Log Out"
    return render(request,"login.html",{"url":"#","login_label":login_label})
@csrf_exempt
def Login(request):
    if request.method=="POST":
        email=request.POST.get('email')
        password=request.POST.get('password')
        # print(email,password)
        user=authenticate(request,password=password,username=email)
        if user is not None:
            login(request,user)
            login_link='login'
            login_label='Log In'
            if request.user.is_authenticated:
                login_link='logout'
                login_label="Log Out"
            return render(request,"login.html",{"url":"#","login_label":login_label})
    login_link='login'
    login_label='Log In'
    if request.user.is_authenticated:
        login_link='logout'
        login_label="Log Out"
    return render(request,"login.html",{"url":"#","login_label":login_label})

@csrf_exempt
def generate_otp():
    chars="ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    otp=""
    for i in range(4):
        otp=otp+random.choice(chars)
    return otp

@csrf_exempt
def send_otp(request):
    if request.method=="POST":
        email=request.POST.get("email")
        password=request.POST.get("password")
        sub="One Time Password for signup"
        otp=generate_otp()
        message="OTP for rahim-khan.azurewebsites.net  is "+otp
        from_mail="Rahim Khan"
        send_mail(subject=sub,message=message,recipient_list=[email],from_email=from_mail)
        if OTP_db.objects.filter(email=email).exists():
            otpdb=OTP_db.objects.get(email=email)
            otpdb.otp=otp
            otpdb.save()
        else:
            otpdb=OTP_db(email=email,otp=otp)
            otpdb.save()
        login_link='login'
        login_label='Log In'
        if request.user.is_authenticated:
            login_link='logout'
            login_label="Log Out"
        return render(request,"otp_validation.html",{"email":email,"password":password,"url":"#","login_label":login_label})
    login_link='login'
    login_label='Log In'
    if request.user.is_authenticated:
        login_link='logout'
        login_label="Log Out"
    return render(request,"otp_validation.html",{"url":"#","login_label":login_label})


@csrf_exempt
def register(request):
    if request.method=="POST":
        email=request.POST.get("email")
        password=request.POST.get("password")
        otp=request.POST.get("otp")
        otpdb=OTP_db.objects.get(email=email)
        if otpdb is not None and otpdb.otp==otp:
            User.objects.create_user(email,email,password)
            return redirect("login")
        return redirect("login")
    login_link='login'
    login_label='Log In'
    if request.user.is_authenticated:
        login_link='logout'
        login_label="Log Out"
    return render(request,"signup.html",{"url":"#","login_label":login_label})