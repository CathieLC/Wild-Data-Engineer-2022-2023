# Generated by Django 4.1.7 on 2023-03-30 15:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("inventaire", "0016_remove_inventaire_items_piece_fk"),
    ]

    operations = [
        migrations.AddField(
            model_name="inventaire_items",
            name="piece_fk",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="inventaire.place",
            ),
        ),
    ]
