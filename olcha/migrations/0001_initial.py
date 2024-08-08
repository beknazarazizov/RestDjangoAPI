# Generated by Django 5.0.7 on 2024-08-07 09:58

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Atribute',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('key_name', models.CharField(max_length=500, unique=True)),
                ('value_name', models.TextField()),
                ('slug', models.SlugField(blank=True, max_length=500, unique=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('category_title', models.CharField(max_length=500, unique=True)),
                ('slug', models.SlugField(blank=True, max_length=500, unique=True)),
                ('category_image', models.ImageField(upload_to='images/')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=500, unique=True)),
                ('slug', models.SlugField(blank=True, max_length=500, unique=True)),
                ('description', models.TextField()),
                ('price', models.IntegerField()),
                ('discount', models.IntegerField(default=0)),
                ('is_liked', models.BooleanField(default=False)),
                ('comment_count', models.IntegerField(default=0)),
                ('average_rating', models.FloatField(default=0)),
                ('primary_image', models.ImageField(upload_to='images/')),
                ('image_list', models.FileField(upload_to='images/')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('group_name', models.CharField(max_length=500, unique=True)),
                ('slug', models.SlugField(blank=True, max_length=500, unique=True)),
                ('group_image', models.ImageField(upload_to='images/')),
                ('category_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='categories', to='olcha.category')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Key',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('key_name', models.CharField(max_length=500, unique=True)),
                ('slug', models.SlugField(blank=True, max_length=500, unique=True)),
                ('atribute', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='keys', to='olcha.atribute')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('comment', models.TextField()),
                ('slug', models.SlugField(blank=True, max_length=500, unique=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to=settings.AUTH_USER_MODEL)),
                ('product_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='olcha.product')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='atribute',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='attributes', to='olcha.product'),
        ),
        migrations.CreateModel(
            name='Value',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('value_name', models.CharField(max_length=500, unique=True)),
                ('slug', models.SlugField(blank=True, max_length=500, unique=True)),
                ('atribute', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='values', to='olcha.atribute')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
