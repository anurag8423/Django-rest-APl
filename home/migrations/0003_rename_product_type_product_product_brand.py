# Generated by Django 5.0.4 on 2024-04-09 10:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_rename_product_number_product_product_code'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='product_type',
            new_name='product_brand',
        ),
    ]