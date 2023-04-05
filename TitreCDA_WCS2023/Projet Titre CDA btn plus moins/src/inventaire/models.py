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
    imagePiece = models.ImageField(upload_to="media/img_pieces", blank=True, null=True)

    def __str__(self):
        return self.nomPiece


class MissionPiece(models.Model):
    utilisateur = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE)
    pieceMission = models.ForeignKey(Piece, on_delete=models.CASCADE)
    quantitePiece = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.pieceMission.nomPiece} ({self.quantitePiece})"


class MissionArticle(models.Model):
    utilisateur = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE)
    pieceMission = models.ForeignKey(MissionPiece, on_delete=models.CASCADE)
    articlesMission = models.ForeignKey(Articles, on_delete=models.CASCADE)
    quantiteArticle = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.articlesMission.nomArticle} ({self.quantite})"

class CommandeClient(models.Model):
    utilisateur = models.OneToOneField(AUTH_USER_MODEL, on_delete=models.CASCADE)
    piecesPanier = models.ManyToManyField(MissionPiece)
    missionValidee = models.BooleanField(default=False)
    dateMissionValisee = models.DateTimeField(blank=True, null=True)


    def __str__(self):
        return f"{self.utilisateur.username} {self.utilisateur.first_name}"





