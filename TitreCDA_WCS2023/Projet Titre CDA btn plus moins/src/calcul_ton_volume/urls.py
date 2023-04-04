
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from inventaire.views import listePieces, detailspieces, addMission
from comptes.views import signup,login_user,logout_user
from views.views import home
from calcul_ton_volume import settings

urlpatterns = [
    path("", home, name="home"),
    path("admin/", admin.site.urls),

    path("listePieces", listePieces, name="listePieces"),

    path("signup", signup, name="signup"),
    path("login", login_user, name="login"),
    path("logout", logout_user, name="logout"),

    path('detailspieces/<str:nomPieceArticle>', detailspieces, name="detailspieces"),
    path('detailspieces/<str:nomPieceArticle>/addMission/', addMission, name="addMission"),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
