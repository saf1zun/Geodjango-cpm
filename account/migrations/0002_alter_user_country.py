# Generated by Django 4.2.6 on 2023-10-28 22:10

from django.db import migrations
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='country',
            field=django_countries.fields.CountryField(default='ETH', max_length=2),
        ),
    ]
