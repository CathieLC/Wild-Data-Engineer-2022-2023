from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model, login, logout, authenticate

# Create your views here.

def home(request):
    return HttpResponse("<h1> Bonjour, tu es bien sur la page d'accueil !</h1>")


User = get_user_model()

def signup(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        #email = request.POST.get("email")
        user = User.objects.create_user(username=username, password=password)
        login(request, user)
        return render(request, 'accounts/login.html')

    return render(request, 'accounts/signup.html')

def login_user(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            return redirect("price")

    return render(request, 'accounts/login.html')

def logout_user(request):
    logout(request)
    return redirect("home")