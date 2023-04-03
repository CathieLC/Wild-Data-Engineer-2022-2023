"""calcul_ton_volume URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from inventaire.views import inventaireParLieu, listePieces, add_to_mission
from comptes.views import signup,login_user,logout_user
from views.views import home
from calcul_ton_volume import settings

urlpatterns = [
    path("", home, name="home"),
    path("admin/", admin.site.urls),

    path("inventaire/", inventaireParLieu, name="inventaire-par-lieu"),
    path("listePieces", listePieces, name="listePieces"),

    path("signup", signup, name="signup"),
    path("login", login_user, name="login"),
    path("logout", logout_user, name="logout"),

    path("inventaire/<str:items>/add-to-mission/", add_to_mission, name="add-to-mission"),

    #path("inventairetest", inventairetest, name="inventairetest")

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
