# Generated by Django 4.2.3 on 2023-07-24 00:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('product', '0007_alter_productphoto_photo'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Shoping_cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(verbose_name='count')),
                ('in_stock', models.BooleanField(default='True')),
                ('date_create', models.DateField(auto_now_add=True)),
                ('date_update', models.DateField(auto_now=True)),
                ('id_product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.product', verbose_name='product')),
                ('id_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='user')),
            ],
        ),
        migrations.AddConstraint(
            model_name='shoping_cart',
            constraint=models.CheckConstraint(check=models.Q(('quantity__gte', 0)), name='check_quantity_cart_product'),
        ),
    ]
