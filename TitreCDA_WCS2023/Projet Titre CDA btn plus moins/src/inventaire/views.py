from django.db.models.functions import Lower
from django.shortcuts import render, get_object_or_404, redirect
from .models import Articles, Piece, CommandeClient, MissionPiece
from django.urls import reverse


def listePieces(request):
    listePieces = Piece.objects.all()
    return render(request, 'inventaire/liste_pieces.html', context={"listePieces": listePieces})



def detailspieces(request,nomPieceArticle):
    ListeArticles = Articles.objects.all()
    articleParPiece = ListeArticles.filter(nomPieceArticle=nomPieceArticle)
    return render(request, "inventaire/articlesParLieu.html", context={"articleParPiece": articleParPiece})


def detailPiecesArticle(request, nomPieceArticle):
    ListeArticles = Articles.objects.all()
    articleParPiece = ListeArticles.filter(nomPieceArticle=nomPieceArticle)

    return render(request, "inventaire/articlesParLieu.html", context={"articleParPiece": articleParPiece})


def addMissionPiece(request, nomPieceArticle):

    # on récupère simplement l'utilisateur
    utilisateur = request.user
    nomDePiece = get_object_or_404(Piece, nomPiece=nomPieceArticle)
    contenu, _ = CommandeClient.objects.get_or_create(utilisateur=utilisateur)

    mission, created = MissionPiece.objects.get_or_create(utilisateur=utilisateur,
                                                          pieceMission=nomDePiece)
    if created:
        contenu.piecesPanier.add(mission)
        contenu.save()
    else:
        mission.quantitePiece += 1
        mission.save()

    return redirect(reverse("detailspieces", kwargs={"nomPieceArticle": nomPieceArticle}))

def RemoveMissionPiece(request, nomPieceArticle):

    utilisateur = request.user
    nomDePiece = get_object_or_404(Piece, nomPiece=nomPieceArticle)
    contenu, _ = CommandeClient.objects.get_or_create(utilisateur=utilisateur)

    mission, created = MissionPiece.objects.get_or_create(utilisateur=utilisateur,
                                                          pieceMission=nomDePiece)
    if created:
        contenu.piecesPanier.add(mission)
        contenu.save()
    else:
        mission.quantitePiece -= 1
        mission.save()

    return redirect(reverse("detailspieces", kwargs={"nomPieceArticle": nomPieceArticle}))

#même chose avec nomArticle
# def addMissionArticle(request, nomArticle):
#
#     # on récupère simplement l'utilisateur
#     utilisateur = request.user
#     nomDArticle = get_object_or_404(Articles, nomArticle=nomArticle)
#     contenu, _ = Panier.objects.get_or_create(utilisateur=utilisateur)
#
#     mission, created = Mission.objects.get_or_create(utilisateur=utilisateur,
#                                                      nomArticle=nomArticle)
#     if created:
#         contenu.nomArticle.add(mission)
#         contenu.save()
#     else:
#         contenu.quantite +=1
#         contenu.save()
#
#     return redirect(reverse("addMission", kwargs={"nomArticle": nomArticle}))