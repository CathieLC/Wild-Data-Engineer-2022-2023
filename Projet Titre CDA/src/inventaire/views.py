from django.db.models.functions import Lower
from django.shortcuts import render, get_object_or_404, redirect
from .models import Inventaire_items, Piece, Mission, Contenu


def listePieces(request):
    piecestablepiece = Piece.objects.all()
    return render(request, 'inventaire/liste_pieces.html', context={"piecestable": piecestablepiece})


def inventaireParLieu(request):
    # pass
    inventaireComplet = Inventaire_items.objects.all()
    typePiece = request.GET.get('place')  # Récupérer les paramètres de recherche

    if typePiece:
        inventaireComplet = inventaireComplet.filter(place=typePiece)  # Filtrer les objets

    return render(request, "inventaire/items_per_place.html", {"typePiece": inventaireComplet})





#A essayer de compléter avec le slug
# def inventaireParLieu(request):
#     inventaireComplet = Inventaire_items.objects.all()
#
#     pieces = Piece.objects.values_list('slug', flat=True)
#     #typePiece = request.GET.get('slug')  # Récupérer les paramètres de recherche
#
#     if pieces:
#         inventaireComplet = inventaireComplet.filter(place=pieces)  # Filtrer les objets
#
#     return render(request, "inventaire/items_per_place.html", {"typePiece": inventaireComplet})




"""cas de figures :
- Utilisateur n'a pas encore de mission (il part de zéro)
- A déjà des articles dans son panier, l'article y est déjà, il faut changer la quantité (incrémenter de 1)"""

def add_to_mission(request, items):
    # on récupère simplement l'utilisateur
    user = request.user
    article = get_object_or_404(Inventaire_items, items=items)
    contenu, _ = Contenu.objects.get_or_create(user=user) #si le contenu n'existe pas il sera créé

    # order ce sera l'article à récupérer si il existe déjà dans le contenu
    # created permettra à l'article d'être créé dans le contenu si ce n'est pas le cas
    mission, created = Mission.objects.get_or_create(user=user,
                                                     article=article)
    if created:
        contenu.missions.add(item)
        contenu.save()
    else:
        contenu.quantite +=1
        contenu.save()
        contenu.save()

    return redirect(reverse("inventaire-par-lieu"))
