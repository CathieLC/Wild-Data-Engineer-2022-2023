from django.contrib import admin

# Register your models here.
from inventaire.models import Piece, CommandeClient, MissionPiece






class PiecesDeLaTable(admin.ModelAdmin):
    class Meta:
        model = Piece
        verbose_name_plural = "Liste complète des pièces"

admin.site.register(Piece, PiecesDeLaTable)




class Commandes(admin.ModelAdmin):
    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        if obj is not None:
            # Si l'article est en cours de modification, on filtre les pièces par utilisateur
            form.base_fields['piecesPanier'].queryset = MissionPiece.objects.filter(utilisateur=obj.utilisateur)
        else:
            # Si l'article est en cours de création, on ne montre pas les pièces
            form.base_fields['piecesPanier'].queryset = MissionPiece.objects.none()
        return form

    class Meta:
        model = CommandeClient
        verbose_name = "Détail pièce par client"
        verbose_name_plural = "Détail pièces par client"

admin.site.register(CommandeClient, Commandes)