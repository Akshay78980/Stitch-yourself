# Generated by Django 4.2.16 on 2024-11-10 15:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0014_alter_productvariantimage_image1'),
    ]

    operations = [
        migrations.AddField(
            model_name='productvariant',
            name='image1',
            field=models.ImageField(default='', upload_to='product_images/'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='productvariant',
            name='image2',
            field=models.ImageField(blank=True, null=True, upload_to='product_images/'),
        ),
        migrations.AddField(
            model_name='productvariant',
            name='image3',
            field=models.ImageField(blank=True, null=True, upload_to='product_images/'),
        ),
        migrations.AddField(
            model_name='productvariant',
            name='image4',
            field=models.ImageField(blank=True, null=True, upload_to='product_images/'),
        ),
        migrations.AddField(
            model_name='productvariant',
            name='image5',
            field=models.ImageField(blank=True, null=True, upload_to='product_images/'),
        ),
        migrations.DeleteModel(
            name='ProductVariantImage',
        ),
    ]