# Generated by Django 4.1.7 on 2023-04-07 15:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventaire', '0060_alter_articlesv2_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articlesv2',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
