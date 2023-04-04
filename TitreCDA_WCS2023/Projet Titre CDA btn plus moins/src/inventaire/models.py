from django.db import models
from django.utils.text import slugify

from calcul_ton_volume.settings import AUTH_USER_MODEL


class Articles(models.Model):
    nomArticle = models.CharField(max_length=100)
    volume = models.DecimalField(max_digits=6, decimal_places=2)
    imageArticle = models.ImageField(upload_to="img_inventaire", blank=True, null=True)
    nomPieceArticle = models.CharField(max_length=50, blank=True, null=True)


    def __str__(self):
        return f"{self.nomArticle} ({self.nomPieceArticle})"

class Piece(models.Model):
    nomPiece = models.CharField(max_length=50)
    article = models.ManyToManyField(Articles)
    slugPiece = models.CharField(max_length=50)
    imagePiece = models.ImageField(upload_to="img_pieces", blank=True, null=True)

    def __str__(self):
        return self.nomPiece











