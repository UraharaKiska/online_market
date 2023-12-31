# Generated by Django 4.2.3 on 2023-07-27 17:31

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
            name='Full_orders',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('personal_order_id', models.IntegerField(blank=True, verbose_name='personal order')),
                ('full_order_id', models.CharField(blank=True, unique=True, verbose_name='full order_id')),
                ('date_create', models.DateTimeField(auto_now_add=True)),
                ('date_update', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Order_status_types',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(max_length=100, verbose_name='status')),
            ],
        ),
        migrations.CreateModel(
            name='Orders_numbers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.IntegerField(verbose_name='count')),
                ('full_order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orders.full_orders', to_field='full_order_id', verbose_name='order id')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.product', verbose_name='product')),
            ],
        ),
        migrations.AddField(
            model_name='full_orders',
            name='status',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orders.order_status_types', verbose_name='status'),
        ),
        migrations.AddField(
            model_name='full_orders',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='user'),
        ),
        migrations.AddConstraint(
            model_name='orders_numbers',
            constraint=models.CheckConstraint(check=models.Q(('count__gte', 0)), name='check_product_count'),
        ),
        migrations.AddConstraint(
            model_name='full_orders',
            constraint=models.CheckConstraint(check=models.Q(('personal_order_id__gte', 0)), name='check_personal_order_id'),
        ),
    ]
