# Generated by Django 5.0.1 on 2024-03-04 00:15

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CarouselItem',
            fields=[
                ('id', models.CharField(max_length=255, primary_key=True, serialize=False)),
                ('url', models.URLField()),
                ('imageUrl', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.CharField(max_length=255, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('imageUrl', models.URLField()),
                ('url', models.SlugField(max_length=255)),
                ('subCategories', models.JSONField()),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.CharField(max_length=255, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('imageUrl', models.URLField()),
                ('rating', models.FloatField()),
                ('subCategories', models.JSONField()),
                ('colors', models.JSONField()),
                ('availability', models.BooleanField()),
                ('tags', models.JSONField()),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to='ecommerce_server.category')),
            ],
        ),
    ]
