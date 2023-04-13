from django.db.models.functions import Lower
from django.shortcuts import render, get_object_or_404, redirect
from .models import Piece, CommandeClient, MissionPiece, ArticlesV2, MissionArticle, DétailListingClient
from django.urls import reverse


def listePieces(request):
    listePieces = Piece.objects.all()
    quantitePiece = MissionPiece.objects.all()
    return render(request, 'inventaire/liste_pieces.html', context={"listePieces": listePieces,
                                                                    "quantitePiece": quantitePiece,})


def PiecesListe(request,nomPiece):
    Piecedeliste = get_object_or_404(Piece, nomPiece=nomPiece)
    quantitePiece = MissionPiece.objects.all()
    ListeArticles = ArticlesV2.objects.all()
    quantiteArticle = MissionArticle.objects.all()

    return render(request, 'inventaire/liste_pieces2.html', context={"Piecedeliste": Piecedeliste,
                                                                     "quantitePiece": quantitePiece,
                                                                     "ListeArticles": ListeArticles,
                                                                     "quantiteArticle": quantiteArticle})


def addMissionPiece(request, nomPiece):

    # on récupère simplement l'utilisateur
    utilisateur = request.user
    nomDePiece = get_object_or_404(Piece, nomPiece=nomPiece)
    contenu, _ = CommandeClient.objects.get_or_create(utilisateur=utilisateur)

    mission, created = MissionPiece.objects.get_or_create(utilisateur=utilisateur,
                                                          pieceMission=nomDePiece)
    if created:
        contenu.piecesPanier.add(mission)
        contenu.save()
    else:
        mission.quantitePiece += 1
        mission.save()

    return redirect(reverse("PiecesListe", kwargs={"nomPiece": nomPiece}))

def RemoveMissionPiece(request, nomPiece):

    utilisateur = request.user
    nomDePiece = get_object_or_404(Piece, nomPiece=nomPiece)
    contenu, _ = CommandeClient.objects.get_or_create(utilisateur=utilisateur)

    mission, created = MissionPiece.objects.get_or_create(utilisateur=utilisateur,
                                                          pieceMission=nomDePiece)
    if created:
        contenu.piecesPanier.add(mission)
        contenu.save()
        return redirect(reverse("PiecesListe", kwargs={"nomPiece": nomPiece}))
    else:
        mission.quantitePiece -= 1
        mission.save()
        if mission.quantitePiece <= 0:
            mission.quantitePiece = 0
            mission.save()
            return redirect("listePieces")

    return redirect(reverse("PiecesListe", kwargs={"nomPiece": nomPiece}))


def listingCompletClient(request):
    listing = get_object_or_404(DétailListingClient, utilisateur=request.user)
    return render(request, "inventaire/listingcompletclient.html", context={"listing": listing.articlesClient.all()})


def delete_MissionPiece(request):
    pass
    # #je récupère le panier
    # listing = request.user.DétailListingClient
    #
    # if cart:
    #     cart.delete()
    #
    # return redirect('index')


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
            missionA.quantiteArticleA = 0
            missionA.save()


    return redirect(reverse("PiecesListe", kwargs={"nomPiece": pieceArticle}))