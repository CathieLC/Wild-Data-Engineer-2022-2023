from django.shortcuts import HttpResponse

# Create your views here.

def firstView(request):
    return HttpResponse("Hey ! tu es sur l'index de l'application search du projet NutriFood.")
