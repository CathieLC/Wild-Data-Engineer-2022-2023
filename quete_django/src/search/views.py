from django.contrib.sites import requests
from django.shortcuts import HttpResponse


from django.shortcuts import render


# Create your views here.

def firstView(request):
    return HttpResponse("Hey ! tu es sur l'index de l'application search du projet NutriFood.")

