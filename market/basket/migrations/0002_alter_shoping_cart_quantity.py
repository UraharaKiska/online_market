# Generated by Django 4.2.3 on 2023-07-24 02:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basket', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shoping_cart',
            name='quantity',
            field=models.IntegerField(default=1, verbose_name='count'),
        ),
    ]