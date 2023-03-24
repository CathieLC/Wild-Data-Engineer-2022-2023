from django.db import models

# Create your models here.

class Listings(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.TextField(blank=True, null=True)
    host_id = models.IntegerField(blank=True, null=True)
    host_name = models.TextField(blank=True, null=True)
    neighbourhood_group = models.TextField(blank=True, null=True)
    neighbourhood = models.TextField(blank=True, null=True)
    latitude = models.TextField(blank=True, null=True)
    longitude = models.TextField(blank=True, null=True)
    room_type = models.TextField(blank=True, null=True)
    price = models.IntegerField(blank=True, null=True)
    minimum_nights = models.IntegerField(blank=True, null=True)
    number_of_reviews = models.IntegerField(blank=True, null=True)
    last_review = models.TextField(blank=True, null=True)
    reviews_per_month = models.TextField(blank=True, null=True)
    calculated_host_listings_count = models.IntegerField(blank=True, null=True)
    availability_365 = models.IntegerField(blank=True, null=True)
    number_of_reviews_ltm = models.IntegerField(blank=True, null=True)
    license = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'listings'
