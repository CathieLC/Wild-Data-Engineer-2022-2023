# Generated by Django 4.1.7 on 2023-04-18 09:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('inventaire', '0073_remove_articlesv2_user'),
    ]

