# Generated by Django 4.0.6 on 2022-08-29 22:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0003_rename_data_restaurantrecord_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='restaurantrecord',
            name='date',
            field=models.DateField(auto_now_add=True, verbose_name='날짜'),
        ),
    ]
