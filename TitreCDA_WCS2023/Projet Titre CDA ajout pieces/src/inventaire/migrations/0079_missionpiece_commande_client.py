# Generated by Django 4.1.7 on 2023-04-19 12:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('inventaire', '0078_remove_détaillistingclient_articlesclient_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='missionpiece',
            name='commande_client',
            field=models.OneToOneField(default=None, on_delete=django.db.models.deletion.CASCADE, to='inventaire.commandeclient'),
            preserve_default=False,
        ),
    ]