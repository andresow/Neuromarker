# Generated by Django 2.1.7 on 2019-07-21 14:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0007_product_descuento'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='descuento',
            new_name='discount',
        ),
    ]
