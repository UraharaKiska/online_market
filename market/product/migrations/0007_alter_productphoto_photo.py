# Generated by Django 4.2.3 on 2023-07-24 00:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0006_alter_productphoto_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productphoto',
            name='photo',
            field=models.ImageField(null=True, upload_to='photo_product/%Y/%m/%d', verbose_name='photo'),
        ),
    ]
