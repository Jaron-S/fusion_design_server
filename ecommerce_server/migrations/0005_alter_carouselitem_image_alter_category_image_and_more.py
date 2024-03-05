# Generated by Django 5.0.3 on 2024-03-04 17:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce_server', '0004_alter_carouselitem_image_alter_category_image_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carouselitem',
            name='image',
            field=models.ImageField(default='null', upload_to='images/carousel/'),
        ),
        migrations.AlterField(
            model_name='category',
            name='image',
            field=models.ImageField(default='null', upload_to='images/categories/'),
        ),
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(default='null', upload_to='images/products/'),
        ),
    ]
