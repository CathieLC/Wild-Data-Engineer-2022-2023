from django.db import models
from django.core.validators import RegexValidator

# Create your models here.
from django.views.generic import DetailView


class Customers (models.Model):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100, blank=True)
    phone_number = models.CharField(max_length=10,
                                    validators=[RegexValidator(regex=r'^\d{10}$',
                                                               message="Le numéro doit comporter 10 chiffres.",),],
                                    blank=True)
    email = models.EmailField(max_length=200, blank=True)



class Piece(models.Model):
    piece = models.CharField(max_length=50)
    image_item = models.ImageField(upload_to="img_pieces", blank=True, null=True)

    def __str__(self):
        return self.piece


class Inventaire_items(models.Model):
    items = models.CharField(max_length=100)
    volume = models.DecimalField(max_digits=6, decimal_places=2)
    place = models.CharField(max_length=50)
    image_item = models.ImageField(upload_to="img_inventaire", blank=True, null=True)
    piecefk = models.ForeignKey(Piece, on_delete=models.CASCADE, related_name='inventaire_items', blank=True, null=True)

    def __str__(self):
        return f"{self.items} ({self.place})"  # je veut le nom des pièces et l'endroit





class HomeToMove(models.Model):
    customer_fk = models.ForeignKey(Customers, on_delete=models.CASCADE, null=True)
    housing_area =models.DecimalField(max_digits=4, decimal_places=2)
    address = models.TextField()
    additional_address = models.TextField(blank=True)
    code_postal = models.CharField(max_length=5,
                                   validators=[RegexValidator(regex=r'^\d{5}$',
                                                              message="Le code postal doit comporter 5 chiffres.")])
    city = models.CharField(max_length=50)
    country = models.CharField(max_length=50, blank=True)

    EstimatedVolume = models.DecimalField(max_digits=4, decimal_places=2, default=0)



class Housing_inventory(models.Model):
    HomeToMove_fk = models.ForeignKey(HomeToMove, on_delete=models.CASCADE, null=True)
    item = models.CharField(max_length=50)
    numberOfItems = models.IntegerField()
    totalVolumeOfItems = models.DecimalField(max_digits=4, decimal_places=2)


class Article(models.Model):
    items = models.ForeignKey(Inventaire_items, on_delete=models.CASCADE, null=True)
    counter = models.IntegerField(default=0)


class ArticleDetailView(DetailView):
   model = Article
   template_name = 'inventaire/items_per_place.html'

   def get_context_data(self, **kwargs):
      context = super().get_context_data(**kwargs)
      context['counter'] = self.object.counter
      return context





