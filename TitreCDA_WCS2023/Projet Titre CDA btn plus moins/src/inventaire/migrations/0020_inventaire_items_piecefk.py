# Generated by Django 4.1.7 on 2023-03-30 19:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("inventaire", "0019_piece_remove_inventaire_items_place_item_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="inventaire_items",
            name="piecefk",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="inventaire_items",
                to="inventaire.piece",
            ),
        ),
    ]
