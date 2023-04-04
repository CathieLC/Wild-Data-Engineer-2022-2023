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


def detailPiecesArticle(request, nomPieceArticle):
    ListeArticles = Articles.objects.all()
    articleParPiece = ListeArticles.filter(nomPieceArticle=nomPieceArticle)

    return render(request, "inventaire/items_per_place.html", context={"articleParPiece": articleParPiece})


def addMission(request, nomPieceArticle):
    pass
    # on récupère simplement l'utilisateur
    utilisateur = request.user
    nomDePiece = get_object_or_404(Piece, nomPiece=nomPieceArticle)
    contenu, _ = Panier.objects.get_or_create(utilisateur=utilisateur)

    mission, created = Mission.objects.get_or_create(utilisateur=utilisateur,
                                                     nomPieceArticle=nomDePiece)
    if created:
        contenu.nomPieceArticle.add(mission)
        contenu.save()
    else:
        contenu.quantite +=1
        contenu.save()

    return redirect(reverse("addMission", kwargs={"nomPieceArticle": nomPieceArticle}))
