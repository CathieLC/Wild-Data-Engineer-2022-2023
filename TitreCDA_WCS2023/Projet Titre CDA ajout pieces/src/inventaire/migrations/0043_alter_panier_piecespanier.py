# Generated by Django 4.1.7 on 2023-04-05 09:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventaire', '0042_rename_articles_panier_piecespanier'),
    ]

    operations = [
        migrations.AlterField(
            model_name='panier',
            name='piecesPanier',
            field=models.ManyToManyField(to='inventaire.missionpiece'),
        ),
    ]