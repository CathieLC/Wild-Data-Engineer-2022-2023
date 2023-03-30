from django.shortcuts import render, get_object_or_404, redirect
from .models import Inventaire_items, Article, Piece

from django.http import JsonResponse, HttpResponseNotAllowed
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt


def pieces(request):
   distinct_values = Inventaire_items.objects.values_list('place', flat=True).distinct() #me permet de récupérer la liste de mes pièces
   pieces_img = Piece.objects.all()
   piece_item = Inventaire_items.objects.get(pk=1)
   piece_associee = piece_item.place

   return render(request, "inventaire/pieces.html", context={"valeurs_distinctes": distinct_values,
                                                             "pieces_img": pieces_img,
                                                             "piece_associee": piece_associee})


# def pieces_with_img(request):
#     # items_inventory = Inventaire_items.objects.all()
#     distinct_values = Inventaire_items.objects.values_list('place', flat=True).distinct()
#     return render(request, "inventaire/pieces2.html", context={"distinct_values": distinct_values})
#
#
# def get_object(self):
#     return get_object_or_404(Inventaire_items, id=self.request.query_params['thumbnail_p'])


def place(request):
   distinct_values = Inventaire_items.objects.values_list('place', flat=True).distinct() #me permet de récupérer la liste de mes pièces
   return render(request, "inventaire/place.html", context={"valeurs_distinctes": distinct_values})


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



def increment_counter(request):
    if request.method == 'POST':
        article_id = request.POST.get('article.id')
        article = get_object_or_404(Article, pk=article_id)
        article.counter += 1
        article.save()
        articles = Article.objects.all()
        total_count = articles.aggregate(Sum('counter'))['counter__sum']
        return render(request, 'inventaire/article_detail.html', {'articles': articles, 'total_count': total_count})
    else:
        return redirect('place')



@require_POST
@csrf_exempt
def update_counter(request, article_id):
    article = get_object_or_404(Article, pk=article_id)
    article.counter += 1
    article.save()
    return JsonResponse({'counter': article.counter})


def article_detail(request):
    return render(request, "inventaire/article_detail.html")



