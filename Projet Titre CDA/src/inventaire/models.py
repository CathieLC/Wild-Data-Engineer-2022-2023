from django.db import models
from django.utils.text import slugify

from calcul_ton_volume.settings import AUTH_USER_MODEL

class Piece(models.Model):
    piece = models.CharField(max_length=50)
    slug = models.CharField(max_length=50)
    image_item = models.ImageField(upload_to="img_pieces", blank=True, null=True)

    def __str__(self):
        return self.piece


class Inventaire_items(models.Model):
    items = models.CharField(max_length=100)
    volume = models.DecimalField(max_digits=6, decimal_places=2)
    place = models.CharField(max_length=50)
    image_item = models.ImageField(upload_to="img_inventaire", blank=True, null=True)

    def __str__(self):
        return f"{self.items} ({self.place})"  # je veux le nom des pièces et l'endroit



class Mission(models.Model):
    user = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE)
    article = models.ForeignKey(Inventaire_items, on_delete=models.CASCADE)
    quantite = models.IntegerField(default=1)
    dejaCommande = models.BooleanField(default=False)  # par défaut l'article n'aura pas été commandé
    dateCommande = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return f"{self.article.items} ({self.quantite})"


"""
- Utilisateur (one to one car un utilisateur ne peut avoir qu'un seul contenu à la fois à déménager
- Articles de la mission many car on peut en avoir plusieurs à ajouter)
- Commandé ou non
- Date de la mission
"""

class Contenu(models.Model):
    user = models.OneToOneField(AUTH_USER_MODEL, on_delete=models.CASCADE)
    missions = models.ManyToManyField(Mission)

    def __str__(self):
        return self.user.username

    def delete(self, *args, **kwargs):
        for mission in self.missions.all():
            mission.dejaCommande = True
            mission.dateCommande = timezone.now()
            mission.save()

        self.missions.clear()
        super().delete(*args, **kwargs)









