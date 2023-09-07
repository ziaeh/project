from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib import auth
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
# 처음 들어갈 경우 page, 
def home_page(request):
    if request.method=="GET":
        print("get으로 시작할걸?")
    # 로그인 할 경우 
    context = {}
    news_text = {}
    if request.method=="POST":
        user_name = request.POST['username'] # 입력 값 받음 
        password = request.POST['password']
        context = {
            'user_name': user_name,
            'password': password
        } # 받아서 로그인 유지된거 확인 용 
        user = authenticate(request,user_name=user_name,password=password)
        if user is not None: # 유저가 맞으면 로그인
            auth.login(request,user)
            return redirect("main-page")
        # # 유저가 아니면
        else:
            print("에러다")
            text="없는데!!!!"
            messages.info(request, text)
            return redirect("main-page")
    return render(request,"main/main.html",context)
# Create your views here.

def enroll_page(request):
    return render(request,"main/enroll.html")

