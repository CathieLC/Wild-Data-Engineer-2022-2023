from django.shortcuts import render

from .models import Listings


# Create your views here.
def premier_jet(request):
    return render(request, "listing/index.html")


# def price(request):
#     # Récupérer les paramètres de recherche
#     price = request.GET.get('price')
#
#     # Initialiser le QuerySet avec tous les objets du modèle
#     queryset = Listings.objects.all()
#
#     # Filtrer les objets en fonction des paramètres de recherche
#     if price:
#         queryset = queryset.filter(price=price)
#
#     # Renvoyer le résultat de la recherche
#     return render(request, "listing/index.html", {"price": queryset})

# def price(request):
#    # Récupération des données de la colonne
#    prices = Listings.objects.values_list('price', flat=True)
#    # Passage des données récupérées au contexte
#    contexte = {'price': prices}
#    # Rendu du fichier HTML intégrant les données
#    return render(request, "listing/index.html", contexte)


# def index(request):
#     objs = Listings.objects.all()
#     context = {'objs': objs}
#     return render(request, "listing/index.html", context)
#
def price2(request):
    objs = Listings.objects.all()
    context = {'objs': objs}

    return render(request, "listing/index.html", context)
