# Generated by Django 4.1.7 on 2023-04-06 14:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventaire', '0045_missionarticle_delete_mission'),
    ]

    operations = [
        migrations.CreateModel(
            name='ArticlesV2',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nomArticle', models.CharField(max_length=100)),
                ('slugArticle', models.SlugField(blank=True, unique=True)),
                ('volume', models.DecimalField(decimal_places=2, max_digits=6)),
                ('imageArticle', models.ImageField(blank=True, null=True, upload_to='img_inventaire')),
                ('nomPieceArticle', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
    ]
