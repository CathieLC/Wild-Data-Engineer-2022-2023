# Generated by Django 4.1.7 on 2023-04-18 10:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventaire', '0075_remove_piece_utilisateur'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='articlesv2',
            name='user',
        ),
        migrations.RemoveField(
            model_name='piece',
            name='user',
        ),
    ]
