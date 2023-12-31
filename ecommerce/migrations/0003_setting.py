# Generated by Django 4.2.4 on 2024-01-02 05:56

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0002_product_alter_category_description_productimage_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Setting',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('email', models.EmailField(max_length=100, unique=True)),
                ('phone', models.CharField(max_length=100, unique=True)),
                ('address', models.CharField(max_length=100, unique=True)),
                ('icon', models.ImageField(upload_to='media/icon')),
                ('logo', models.ImageField(upload_to='media/logo')),
                ('description', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True)),
            ],
        ),
    ]
