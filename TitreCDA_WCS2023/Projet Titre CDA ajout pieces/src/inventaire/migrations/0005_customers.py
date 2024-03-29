# Generated by Django 3.1.6 on 2023-02-24 17:08

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventaire', '0004_auto_20230222_1134'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=100)),
                ('lastname', models.CharField(max_length=100)),
                ('adress', models.TextField()),
                ('additional_address', models.TextField(blank=True)),
                ('code_postal', models.CharField(max_length=5, validators=[django.core.validators.RegexValidator(message='Le code postal doit comporter 5 chiffres.', regex='^\\d{5}$')])),
                ('city', models.CharField(max_length=50)),
                ('country', models.CharField(blank=True, max_length=50)),
            ],
        ),
    ]
