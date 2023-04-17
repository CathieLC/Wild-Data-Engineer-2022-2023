from django.db import models

from calcul_ton_volume.settings import AUTH_USER_MODEL


from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.utils.text import slugify
import string, random


# class Articles(models.Model):
#     nomArticle = models.CharField(max_length=100)
#     volume = models.DecimalField(max_digits=6, decimal_places=2)
#     imageArticle = models.ImageField(upload_to="img_inventaire", blank=True, null=True)
#     nomPieceArticle = models.CharField(max_length=50, blank=True, null=True)
#
#     def __str__(self):
#         return f"{self.nomArticle} ({self.nomPieceArticle})"

class Piece(models.Model):
    nomPiece = models.CharField(max_length=50)
    slugPiece = models.CharField(max_length=50)
    imagePiece = models.ImageField(upload_to="media/img_pieces", blank=True, null=True)

    class Meta:
        verbose_name_plural = "Liste complète des pièces"

    def __str__(self):
        return self.nomPiece


class ArticlesV2(models.Model):
    id = models.AutoField(primary_key=True)
    nomArticle = models.CharField(max_length=100)
    slugArticle = models.CharField(max_length=100)
    volume = models.DecimalField(max_digits=6, decimal_places=2)
    imageArticle = models.ImageField(upload_to="img_inventaire", blank=True, null=True)
    nomPieceArticle = models.CharField(max_length=50, blank=True, null=True)
    Piece_id = models.ForeignKey(Piece, default=19, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "Liste complète des articles"

    def __str__(self):
        return f"{self.id} - {self.nomArticle} ({self.nomPieceArticle})"

class MissionPiece(models.Model):
    utilisateur = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE)
    pieceMission = models.ForeignKey(Piece, on_delete=models.CASCADE)
    quantitePiece = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.pieceMission.nomPiece} ({self.quantitePiece})"


class MissionArticle(models.Model):
    utilisateur = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE)
    pieceMissionA = models.ForeignKey(Piece, on_delete=models.CASCADE)
    articlesMission = models.ForeignKey(ArticlesV2, on_delete=models.CASCADE)
    quantiteArticleA = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.articlesMission.nomArticle} ({self.quantiteArticleA})"


class CommandeClient(models.Model):
    utilisateur = models.OneToOneField(AUTH_USER_MODEL, on_delete=models.CASCADE)
    piecesPanier = models.ManyToManyField(MissionPiece)
    missionValidee = models.BooleanField(default=False)
    dateMissionValisee = models.DateTimeField(blank=True, null=True)

    class Meta:
        verbose_name = "Détail pièce par client"
        verbose_name_plural = "Détail pièces par client"

    def __str__(self):
        return self.utilisateur.username


class DétailListingClient(models.Model):
    utilisateur = models.OneToOneField(AUTH_USER_MODEL, on_delete=models.CASCADE)
    articlesClient = models.ManyToManyField(MissionArticle)

    class Meta:
        verbose_name = "Détail article par client"
        verbose_name_plural = "Détail articles par client"

    def __str__(self):
        return self.utilisateur.username

    def delete(self, *args, **kwargs):
        for article in articlesClient.all():
            article.save()

        self.articlesClient.clear()
        super().delete(*args, **kwargs)



