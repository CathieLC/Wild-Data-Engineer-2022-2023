# Generated by Django 4.1.7 on 2023-04-07 15:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('inventaire', '0057_articlesv2_piece_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articlesv2',
            name='Piece_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventaire.piece'),
        ),
    ]
