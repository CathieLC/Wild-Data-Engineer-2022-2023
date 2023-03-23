# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


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


class Neighbourhoods(models.Model):
    neighbourhood_group = models.TextField(blank=True, null=True)
    neighbourhood = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'neighbourhoods'


class Reviews(models.Model):
    listing_id = models.IntegerField(blank=True, null=True)
    date = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'reviews'