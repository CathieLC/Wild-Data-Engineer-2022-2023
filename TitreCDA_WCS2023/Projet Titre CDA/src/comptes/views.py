from django.contrib.auth import get_user_model, login, logout, authenticate
from django.shortcuts import render, redirect

User = get_user_model()

def signup(request):
    if request.method == "POST":
        #Traiter le formulaire
        username = request.POST.get("username")
        first_name = request.POST.get("first_name")
        email = request.POST.get("email")
        password = request.POST.get("password")
        user = User.objects.create_user(username=username,
                                        first_name=first_name,
                                        email=email,
                                        password=password)
        login(request, user)
        return redirect('home')

    return render(request, "comptes/signup.html")


def login_user(request):
    if request.method == "POST":
        # Connecter l'utilisateur
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(username=username,
                            password=password)
        if user:
            login(request, user)
            return redirect('home')

    return render(request, "comptes/login.html")


def logout_user(request):
    logout(request)
    return redirect('home')
