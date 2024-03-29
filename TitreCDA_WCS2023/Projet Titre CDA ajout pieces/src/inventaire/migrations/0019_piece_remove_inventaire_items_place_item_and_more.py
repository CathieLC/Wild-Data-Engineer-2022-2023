# Generated by Django 4.1.7 on 2023-03-30 15:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("inventaire", "0018_remove_inventaire_items_piece_fk_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="Piece",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("piece", models.CharField(max_length=50)),
                (
                    "image_item",
                    models.ImageField(blank=True, null=True, upload_to="img_pieces"),
                ),
            ],
        ),
        migrations.RemoveField(
            model_name="inventaire_items",
            name="place_item",
        ),
        migrations.DeleteModel(
            name="Place",
        ),
    ]
