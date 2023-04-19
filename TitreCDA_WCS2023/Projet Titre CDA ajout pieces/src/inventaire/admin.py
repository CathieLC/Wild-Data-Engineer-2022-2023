from django.contrib import admin

# Register your models here.
from inventaire.models import ArticlesV2, Piece, CommandeClient, DétailListingClient



class ArticlesDeLaTable(admin.ModelAdmin):
    class Meta:
        model = ArticlesV2
        verbose_name_plural = "Liste complète des articles"

admin.site.register(ArticlesV2, ArticlesDeLaTable)


class PiecesDeLaTable(admin.ModelAdmin):
    class Meta:
        model = Piece
        verbose_name_plural = "Liste complète des pièces"

admin.site.register(Piece, PiecesDeLaTable)

class Commandes(admin.ModelAdmin):
    class Meta:
        model = CommandeClient
        verbose_name = "Détail pièce par client"
        verbose_name_plural = "Détail pièces par client"

admin.site.register(CommandeClient, Commandes)

class DetailClient(admin.ModelAdmin):
    class Meta:
        model = DétailListingClient
        verbose_name = "Détail article par client"
        verbose_name_plural = "Détail articles par client"

admin.site.register(DétailListingClient, DetailClient)

