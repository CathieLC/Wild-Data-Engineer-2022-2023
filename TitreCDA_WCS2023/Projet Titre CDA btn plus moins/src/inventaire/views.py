from django.db.models.functions import Lower
from django.shortcuts import render, get_object_or_404, redirect
from .models import Articles, Piece, CommandeClient, MissionPiece, ArticlesV2, MissionArticle, DétailListingClient
from django.urls import reverse


def listePieces(request):
    listePieces = Piece.objects.all()
    return render(request, 'inventaire/liste_pieces.html', context={"listePieces": listePieces})


def PiecesListe(request,nomPiece):
    Piecedeliste = get_object_or_404(Piece, nomPiece=nomPiece)
    quantitePiece = MissionPiece.objects.all()
    ListeArticles = ArticlesV2.objects.all()
    quantiteArticle = MissionArticle.objects.all()

    return render(request, 'inventaire/liste_pieces2.html', context={"Piecedeliste": Piecedeliste,
                                                                     "quantitePiece": quantitePiece,
                                                                     "ListeArticles": ListeArticles,
                                                                     "quantiteArticle": quantiteArticle})

# def detailspieces(request,nomPieceArticle):
#     ListeArticles = Articles.objects.all()
#     articleParPiece = ListeArticles.filter(nomPieceArticle=nomPieceArticle)
#     return render(request, "inventaire/articlesParLieu.html", context={"articleParPiece": articleParPiece})


# def detailArticle(request, nomPieceArticle):
#     ListeArticles = ArticlesV2.objects.all()
#     quantiteArticle = MissionArticle.objects.all()
#
#     #return render(request, "inventaire/articlesParLieu.html", context={"articleParPiece": articleParPiece})
#
#     return render(request, 'inventaire/liste_pieces2.html', context={"ListeArticles": ListeArticles,
#                                                                      "quantiteArticle": quantiteArticle})


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
    else:
        mission.quantitePiece -= 1
        mission.save()

    return redirect(reverse("PiecesListe", kwargs={"nomPiece": nomPiece}))
    #return redirect("listePieces")

def addMissionArticle(request, nomArticle):
    # on récupère simplement l'utilisateur
    utilisateur = request.user
    nomDeLArticle = get_object_or_404(ArticlesV2, nomArticle=nomArticle)
    pieceArticle = get_object_or_404(Piece, nomPiece=nomDeLArticle.nomPieceArticle)

    contenu, _ = DétailListingClient.objects.get_or_create(utilisateur=utilisateur)

    missionA, created = MissionArticle.objects.get_or_create(utilisateur=utilisateur,
                                                             pieceMissionA=pieceArticle,
                                                             articlesMission=nomDeLArticle)
    if created:
        contenu.articlesClient.add(missionA)
        contenu.save()
    else:
        missionA.quantiteArticle += 1
        missionA.save()

    return redirect(reverse("PiecesListe", kwargs={"nomPiece": pieceArticle}))

def RemoveMissionArticle(request, nomArticle):
    # on récupère simplement l'utilisateur
    utilisateur = request.user
    nomDeLArticle = get_object_or_404(Articles, nomArticle=nomArticle)
    pieceArticle = get_object_or_404(Piece, nomPiece=nomDeLArticle.nomPieceArticle)

    contenu, _ = DétailListingClient.objects.get_or_create(utilisateur=utilisateur)

    missionA, created = MissionArticle.objects.get_or_create(utilisateur=utilisateur,
                                                             pieceMission=pieceArticle,
                                                             articlesMission=nomDeLArticle)
    if created:
        contenu.articlesClient.add(missionA)
        contenu.save()
    else:
        missionA.quantiteArticle -= 1
        missionA.save()

    return redirect(reverse("PiecesListe", kwargs={"nomPiece": pieceArticle}))