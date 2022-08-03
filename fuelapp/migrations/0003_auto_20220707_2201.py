# Generated by Django 3.2.14 on 2022-07-07 16:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fuelapp', '0002_rename_petrol_prices_petrol_model'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='petrol_model',
            name='yesterdays_prices',
        ),
        migrations.AlterField(
            model_name='petrol_model',
            name='city_name',
            field=models.CharField(max_length=200, unique=True),
        ),
    ]