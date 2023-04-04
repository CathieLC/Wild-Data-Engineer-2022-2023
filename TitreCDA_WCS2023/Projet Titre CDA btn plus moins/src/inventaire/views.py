from django.db.models.functions import Lower
from django.shortcuts import render, get_object_or_404, redirect
from .models import Articles, Piece


def listePieces(request):
    listePieces = Piece.objects.all()
    return render(request, 'inventaire/liste_pieces.html', context={"listePieces": listePieces})

def detailspieces(request,nomPieceArticle):
    ListeArticles = Articles.objects.all()
    articleParPiece = ListeArticles.filter(nomPieceArticle=nomPieceArticle)
    return render(request, "inventaire/items_per_place.html", context={"articleParPiece": articleParPiece})


# def inventaireParLieu(request):
#     # pass
#     inventaireComplet = Articles.objects.all()
#     typePiece = request.GET.get('nomPieceArticle')  # Récupérer les paramètres de recherche
#
#     if typePiece:
#         inventaireComplet = inventaireComplet.filter(nomPieceArticle=typePiece)  # Filtrer les objets
#
#     return render(request, "inventaire/items_per_place.html", {"typePiece": inventaireComplet})



#A essayer de compléter avec le slug
# def inventaireParLieu(request):
#     inventaireComplet = Articles.objects.all()#
#     pieces = Piece.objects.values_list('slug', flat=True)
#     #typePiece = request.GET.get('slug')  # Récupérer les paramètres de recherche#
#     if pieces:
#         inventaireComplet = inventaireComplet.filter(place=pieces)  # Filtrer les objets#
#     return render(request, "inventaire/items_per_place.html", {"typePiece": inventaireComplet})



# def add_to_mission(request, items): # comme add to cart
#     # on récupère simplement l'utilisateur
#     user = request.user
#     article = get_object_or_404(Articles, items=items)
#     contenu, _ = Contenu.objects.get_or_create(user=user) #si le contenu n'existe pas il sera créé
#
#     # order ce sera l'article à récupérer si il existe déjà dans le contenu
#     # created permettra à l'article d'être créé dans le contenu si ce n'est pas le cas
#     mission, created = Mission.objects.get_or_create(user=user,
#                                                      article=article)
#     if created:
#         contenu.missions.add(item)
#         contenu.save()
#     else:
#         contenu.quantite +=1
#         contenu.save()
#         contenu.save()
#
#     return redirect(reverse("inventaire-par-lieu", kwargs={"place": place}))
