from django.db.models.functions import Lower
from django.shortcuts import render, get_object_or_404, redirect
from inventaire.models import Piece, CommandeClient, MissionPiece
from inventaireArticles.models import ArticlesV2, MissionArticle, DétailListingClient
from django.urls import reverse
from django.contrib import messages
from django.http import HttpResponse
from comptes.models import Client




def listePieces(request):
    listePieces = Piece.objects.all()
    quantitePiece = MissionPiece.objects.filter(utilisateur=request.user)

    return render(request, 'inventaire/liste_pieces.html', context={"listePieces": listePieces,
                                                                    "quantitePiece": quantitePiece,})


def PiecesListe(request,nomPiece):

    Piecedeliste = get_object_or_404(Piece, nomPiece=nomPiece)
    quantitePiece = MissionPiece.objects.filter(utilisateur=request.user)
    ListeArticles = ArticlesV2.objects.all()
    quantiteArticle = MissionArticle.objects.filter(utilisateur=request.user)

    return render(request, 'inventaire/liste_pieces2.html', context={"Piecedeliste": Piecedeliste,
                                                                      "quantitePiece": quantitePiece,
                                                                      "ListeArticles": ListeArticles,
                                                                      "quantiteArticle": quantiteArticle})


def addMissionPiece(request, nomPiece):

    # on récupère simplement l'utilisateur
    user = request.user
    nomDePiece = get_object_or_404(Piece, nomPiece=nomPiece)
    # Commande = CommandeClient.objects.filter(utilisateur=request.user)

    contenu, _ = CommandeClient.objects.get_or_create(utilisateur=user)

    mission, created = MissionPiece.objects.get_or_create(utilisateur=user,
                                                          pieceMission=nomDePiece)

    if created:
        contenu.piecesPanier.add(mission)
        contenu.save()
    else:
        mission.quantitePiece += 1
        mission.save()

    return redirect(reverse("PiecesListe", kwargs={"nomPiece": nomPiece}))



def RemoveMissionPiece(request, nomPiece):

    user = request.user
    nomDePiece = get_object_or_404(Piece, nomPiece=nomPiece)

    contenu, _ = CommandeClient.objects.get_or_create(utilisateur=user)

    mission, created = MissionPiece.objects.get_or_create(utilisateur=user,
                                                          pieceMission=nomDePiece)
    if created:
        contenu.piecesPanier.add(mission)
        contenu.save()
        return redirect("listePieces")
    else:
        mission.quantitePiece -= 1
        mission.save()
        if mission.quantitePiece <= 0:
            mission.quantitePiece = 0
            mission.save()
            return redirect("listePieces")

    return redirect(reverse("PiecesListe", kwargs={"nomPiece": nomPiece}))

def listingCompletPièces(request):
    listingP = MissionPiece.objects.filter(utilisateur=request.user)

    if listingP :
        return render(request, "inventaire/listingcompletpieces.html", context={"listingP": listingP})
    else :
        return HttpResponse("Vous n'avez pas sélectionné de pièce")

def deleteListingPieces(request):
    # je récupère le panier DétailListingClient pour l'utilisateur connecté
    PiècesClient = MissionPiece.objects.filter(utilisateur=request.user)

    if PiècesClient.all():
        PiècesClient.all().delete()
        return redirect('listePieces')

    return redirect('listePieces')

