# Generated by Django 4.1.7 on 2023-04-04 14:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventaire', '0038_mission'),
    ]

    operations = [
        migrations.RenameField(
            model_name='mission',
            old_name='user',
            new_name='utilisateur',
        ),
    ]
