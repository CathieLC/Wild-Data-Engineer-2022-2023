from django.db import models

from calcul_ton_volume.settings import AUTH_USER_MODEL


from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.utils.text import slugify
import string, random



class Piece(models.Model):

    nomPiece = models.CharField(max_length=50)
    slugPiece = models.CharField(max_length=50)
    imagePiece = models.ImageField(upload_to="media/img_pieces", blank=True, null=True)

    class Meta:
        verbose_name_plural = "Liste complète des pièces"

    def __str__(self):
        return self.nomPiece




class MissionPiece(models.Model):
    utilisateur = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE)
    pieceMission = models.ForeignKey(Piece, on_delete=models.CASCADE)
    quantitePiece = models.IntegerField(default=1)
    commande_client = models.ForeignKey('CommandeClient', on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f"{self.pieceMission.nomPiece} ({self.quantitePiece})"




class CommandeClient(models.Model):
    utilisateur = models.OneToOneField(AUTH_USER_MODEL, on_delete=models.CASCADE)
    piecesPanier = models.ManyToManyField(MissionPiece)
    missionValidee = models.BooleanField(default=False)
    dateMissionValidee = models.DateTimeField(blank=True, null=True)

    class Meta:
        verbose_name = "Détail pièce par client"
        verbose_name_plural = "Détail pièces par client"

    def __str__(self):
        return self.utilisateur.username





