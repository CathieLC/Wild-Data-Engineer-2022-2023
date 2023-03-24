from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
from inventaire.models import Inventaire_items


def pieces_with_img(request):
   distinct_values = Inventaire_items.objects.values_list('place', flat=True).distinct() #me permet de récupérer la liste de mes pièces
   items = Inventaire_items.objects.all()
   return render(request, "inventaire/pieces_with_img.html", context={"valeurs_distinctes": distinct_values, "items": items})


def home(request):
   return render(request, "inventaire/home.html")


def place(request):
   distinct_values = Inventaire_items.objects.values_list('place', flat=True).distinct() #me permet de récupérer la liste de mes pièces
   return render(request, "inventaire/place.html", context={"valeurs_distinctes":distinct_values})




def inventairePerPlace(request):

   # Récupérer les paramètres de recherche
   place_type = request.GET.get('place')

   #Initialiser le QuerySet avec tous les objets du modèle
   queryset = Inventaire_items.objects.all()

   #Filtrer les objets en fonction des paramètres de recherche
   if place_type :
      queryset = queryset.filter(place=place_type)

   # Renvoyer le résultat de la recherche
   return render(request, "inventaire/items_per_place.html", {"type_place": queryset})
