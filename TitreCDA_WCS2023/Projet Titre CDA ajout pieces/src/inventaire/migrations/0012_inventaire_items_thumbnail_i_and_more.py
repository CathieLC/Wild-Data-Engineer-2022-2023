# Generated by Django 4.1.7 on 2023-03-30 11:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("inventaire", "0011_rename_nb_article_article"),
    ]

    operations = [
        migrations.AddField(
            model_name="inventaire_items",
            name="thumbnail_i",
            field=models.ImageField(blank=True, null=True, upload_to="img_inventaire"),
        ),
        migrations.AddField(
            model_name="inventaire_items",
            name="thumbnail_p",
            field=models.ImageField(blank=True, null=True, upload_to="img_pieces"),
        ),
    ]