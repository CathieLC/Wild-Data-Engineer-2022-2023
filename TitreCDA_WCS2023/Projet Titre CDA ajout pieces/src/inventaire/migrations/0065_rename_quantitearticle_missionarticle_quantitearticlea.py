# Generated by Django 4.2 on 2023-04-12 10:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("inventaire", "0064_alter_détaillistingclient_articlesclient"),
    ]

    operations = [
        migrations.RenameField(
            model_name="missionarticle",
            old_name="quantiteArticle",
            new_name="quantiteArticleA",
        ),
    ]