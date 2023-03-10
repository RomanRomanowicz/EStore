# Generated by Django 4.1.5 on 2023-01-30 18:51

import autoslug.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=200, verbose_name='наименование категории')),
                ('slug', autoslug.fields.AutoSlugField(default=None, editable=False, null=True, populate_from='name', unique=True)),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='CategoryColor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('color', models.CharField(db_index=True, max_length=200, verbose_name='Категория по цвету')),
                ('slug', autoslug.fields.AutoSlugField(default=None, editable=False, null=True, populate_from='color', unique=True)),
            ],
            options={
                'verbose_name': 'Категория по цвету',
                'verbose_name_plural': 'Категория по цвету',
                'ordering': ('color',),
            },
        ),
        migrations.CreateModel(
            name='CategorySize',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('size', models.CharField(db_index=True, max_length=200, verbose_name='Категория по размеру')),
                ('slug', autoslug.fields.AutoSlugField(default=None, editable=False, null=True, populate_from='size', unique=True)),
            ],
            options={
                'verbose_name': 'Категория по размеру',
                'verbose_name_plural': 'Категория по размеру',
                'ordering': ('size',),
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=200, verbose_name='Наименование товара')),
                ('slug', autoslug.fields.AutoSlugField(default=None, editable=False, null=True, populate_from='name', unique=True)),
                ('image', models.ImageField(blank=True, upload_to='products/%Y/%m/%d', verbose_name='главное фото')),
                ('description', models.TextField(blank=True, verbose_name='описание')),
                ('price', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='цена')),
                ('stock', models.PositiveIntegerField()),
                ('available', models.BooleanField(default=True, verbose_name='доступный')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name=' дата создания')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='дата обновления')),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='products', to='shop.category', verbose_name='категория')),
                ('color', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='products', to='shop.categorycolor', verbose_name='Цвет')),
                ('size', models.ForeignKey(blank=True, default='All Size', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='products', to='shop.categorysize', verbose_name='Размер')),
                ('vendor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Товар',
                'verbose_name_plural': 'Товары',
                'ordering': ('name',),
                'index_together': {('id', 'slug')},
            },
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('images', models.ImageField(blank=True, upload_to='products/%Y/%m/%d', verbose_name='фото')),
                ('product', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='photos', to='shop.product', verbose_name='product')),
            ],
            options={
                'verbose_name': 'фото',
                'verbose_name_plural': 'фото',
                'ordering': ('product', 'images'),
            },
        ),
    ]
