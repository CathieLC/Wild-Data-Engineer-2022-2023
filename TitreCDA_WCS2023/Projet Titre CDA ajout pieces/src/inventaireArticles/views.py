from django.db.models.functions import Lower
from django.shortcuts import render, get_object_or_404, redirect
from inventaire.models import Piece, CommandeClient, MissionPiece
from inventaireArticles.models import ArticlesV2, MissionArticle, DétailListingClient
from django.urls import reverse
from django.contrib import messages
from django.http import HttpResponse
from comptes.models import Client


def addMissionArticle(request, nomArticle):
    # on récupère simplement l'utilisateur
    utilisateur = request.user
    nomDeLArticle = get_object_or_404(ArticlesV2, slugArticle=nomArticle)
    pieceArticle = get_object_or_404(Piece, nomPiece=nomDeLArticle.nomPieceArticle)

    contenu, _ = DétailListingClient.objects.get_or_create(utilisateur=utilisateur)

    missionA, created = MissionArticle.objects.get_or_create(utilisateur=utilisateur,
                                                             pieceMissionA=pieceArticle,
                                                             articlesMission=nomDeLArticle)
    if created:
        contenu.articlesClient.add(missionA)
        contenu.save()
    else:
        missionA.quantiteArticleA += 1
        missionA.save()

    return redirect(reverse("PiecesListe", kwargs={"nomPiece": pieceArticle}))

def removeMissionArticle(request, nomArticle):
    # on récupère simplement l'utilisateur
    utilisateur = request.user
    nomDeLArticle = get_object_or_404(ArticlesV2, slugArticle=nomArticle)
    pieceArticle = get_object_or_404(Piece, nomPiece=nomDeLArticle.nomPieceArticle)

    contenu, _ = DétailListingClient.objects.get_or_create(utilisateur=utilisateur)

    missionA, created = MissionArticle.objects.get_or_create(utilisateur=utilisateur,
                                                             pieceMissionA=pieceArticle,
                                                             articlesMission=nomDeLArticle)
    if created:
        contenu.articlesClient.add(missionA)
        contenu.save()
    else:
        missionA.quantiteArticleA -= 1
        missionA.save()

        if missionA.quantiteArticleA < 0 :
            # missionA.quantiteArticleA = 0
            missionA.quantiteArticleA.delete()
            missionA.save()
            return redirect("listePieces")

    return redirect(reverse("PiecesListe", kwargs={"nomPiece": pieceArticle}))

def listingCompletArticles(request):
    listingA = MissionArticle.objects.filter(utilisateur=request.user)
    if listingA:
        return render(request, "inventaireArticles/listingcompletarticles.html", context={"listing": listingA})
    else :
        return HttpResponse("Vous n'avez pas sélectionné d'articles")

def deleteListingArticles(request):
    # je récupère le panier DétailListingClient pour l'utilisateur connecté
    # listingClient = get_object_or_404(DétailListingClient, utilisateur=request.user)
    listingClient = MissionArticle.objects.filter(utilisateur=request.user)

    if listingClient.all():
        listingClient.all().delete()
        return redirect('listePieces')

    return redirect('listePieces')