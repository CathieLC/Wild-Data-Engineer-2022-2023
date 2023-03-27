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
from django.contrib import admin
from django.urls import path

from inventaire.views import home, place, inventairePerPlace, pieces_with_img, update_counter, increment_counter, article_detail


urlpatterns = [
    path("", home, name="home"),
    path("admin/", admin.site.urls),
    path("place/", place, name="place"),
    path("inventaire/", inventairePerPlace, name="inventaire-per-place"),
    path("pieces/", pieces_with_img, name="pieces"),
    path("update_counter", update_counter, name='update-counter'),
    path("increment_counter", increment_counter, name='increment-counter'),
    path("article_detail", article_detail, name="article-detail")


]
