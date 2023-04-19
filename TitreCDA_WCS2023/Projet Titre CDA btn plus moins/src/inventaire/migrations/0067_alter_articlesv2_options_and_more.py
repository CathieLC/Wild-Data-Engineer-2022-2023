# Generated by Django 4.1.7 on 2023-04-18 07:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('inventaire', '0066_delete_articles'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='articlesv2',
            options={'verbose_name_plural': 'Liste complète des articles'},
        ),
        migrations.AlterModelOptions(
            name='commandeclient',
            options={'verbose_name': 'Détail pièce par client', 'verbose_name_plural': 'Détail pièces par client'},
        ),
        migrations.AlterModelOptions(
            name='détaillistingclient',
            options={'verbose_name': 'Détail article par client', 'verbose_name_plural': 'Détail articles par client'},
        ),
        migrations.AlterModelOptions(
            name='piece',
            options={'verbose_name_plural': 'Liste complète des pièces'},
        )
    ]
