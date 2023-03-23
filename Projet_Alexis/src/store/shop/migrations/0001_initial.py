# Generated by Django 4.1.7 on 2023-03-21 14:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Product",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=100)),
                ("price", models.FloatField(default=0.0)),
                ("stock", models.IntegerField(default=0)),
                ("discount_price", models.FloatField(blank=True, null=True)),
                ("category", models.CharField(blank=True, max_length=100)),
                ("description", models.TextField(blank=True)),
                (
                    "image",
                    models.ImageField(blank=True, null=True, upload_to="products/"),
                ),
            ],
        ),
    ]