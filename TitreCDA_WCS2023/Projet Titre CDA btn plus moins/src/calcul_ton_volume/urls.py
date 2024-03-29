
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from inventaire.views import listePieces, addMissionPiece, RemoveMissionPiece, PiecesListe,  listingCompletPièces, deleteListingPieces
from inventaire.views import addMissionArticle, removeMissionArticle, listingCompletArticles, deleteListingArticles
from comptes.views import signup,login_user,logout_user
from views.views import home
from calcul_ton_volume import settings


urlpatterns = [
    path("", home, name="home"),
    path("admin/", admin.site.urls),

    path("listePieces", listePieces, name="listePieces"),

    path("PiecesListe/<str:nomPiece>/", PiecesListe, name="PiecesListe"),

    path("signup", signup, name="signup"),
    path("login", login_user, name="login"),
    path("logout", logout_user, name="logout"),

    path('PiecesListe/<str:nomPiece>/addMissionPiece/', addMissionPiece, name="addMissionPiece"),
    path('PiecesListe/<str:nomPiece>/RemoveMissionPiece/', RemoveMissionPiece, name="RemoveMissionPiece"),

    path("listingCompletPièces", listingCompletPièces, name="listingCompletPièces"),
    path("listingCompletPièces/delete", deleteListingPieces, name="deleteListingPieces"),

    # path('detailspieces/<str:nomPieceArticle>', detailspieces, name="detailspieces"),
    path("addMissionArticle/<str:nomArticle>/addMissionArticle", addMissionArticle, name="addMissionArticle"),
    path("RemoveMissionArticle/<str:nomArticle>/removeMissionArticle", removeMissionArticle, name="removeMissionArticle"),

    path("listingCompletArticles", listingCompletArticles, name="listingCompletArticles"),
    path("listingCompletArticles/delete", deleteListingArticles, name="listingCompletArticlesDelete"),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
