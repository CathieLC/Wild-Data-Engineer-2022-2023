from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model, login, logout, authenticate

import os


# Create your views here.

def home(request):
    return render(request, "accounts/Home.html")


User = get_user_model()


def signup(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = User.objects.create_user(username=username, password=password)
        login(request, user)
        return redirect("login")

    return render(request, 'accounts/signup.html')


def login_user(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            return redirect("objet")

    return render(request, 'accounts/login.html')



# def google_auth(request):
#     CLIENT_ID = "os.environ.get('GOOGLE_CLIENT_ID')"
#     REDIRECT_URI = request.build_absolute_uri('/google-auth')
#     context = {'CLIENT_ID': CLIENT_ID, 'REDIRECT_URI': REDIRECT_URI}
#     return render(request, 'accounts/login_register_modal.html', context=context)


def logout_user(request):
    logout(request)
    return redirect("login")


def login_register(request):
    return render(request, 'accounts/login_register_modal.html')
