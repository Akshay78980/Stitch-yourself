# Generated by Django 4.2.16 on 2024-12-08 12:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0021_alter_product_name_alter_productvariant_color_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(help_text='Enter category name (e.g., Hoodie, T-Shirt)', max_length=30),
        ),
        migrations.AlterField(
            model_name='productvariant',
            name='size',
            field=models.CharField(blank=True, choices=[('S', 'S'), ('M', 'M'), ('L', 'L')], db_index=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='productvariant',
            name='variant_price',
            field=models.DecimalField(blank=True, db_index=True, decimal_places=2, max_digits=10, null=True),
        ),
    ]