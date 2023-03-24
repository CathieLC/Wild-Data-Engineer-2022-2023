from django.db import models
from django.core.validators import RegexValidator

# Create your models here.
class Inventaire_items(models.Model):
    items = models.CharField(max_length=100)
    volume = models.DecimalField(max_digits=6, decimal_places=2)
    place = models.CharField(max_length=50)



class Customers (models.Model):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100, blank=True)
    phone_number = models.CharField(max_length=10,
                                    validators=[RegexValidator(regex=r'^\d{10}$',
                                                               message="Le numéro doit comporter 10 chiffres.",),],
                                    blank=True)
    email = models.EmailField(max_length=200, blank=True)


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




