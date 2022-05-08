# Generated by Django 4.0.4 on 2022-05-05 05:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0002_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='title_en',
            field=models.CharField(max_length=255, null=True, unique=True, verbose_name='Nomi'),
        ),
        migrations.AddField(
            model_name='course',
            name='title_ru',
            field=models.CharField(max_length=255, null=True, unique=True, verbose_name='Nomi'),
        ),
        migrations.AddField(
            model_name='lesson',
            name='description_en',
            field=models.TextField(null=True, verbose_name='Tavsifi'),
        ),
        migrations.AddField(
            model_name='lesson',
            name='description_ru',
            field=models.TextField(null=True, verbose_name='Tavsifi'),
        ),
        migrations.AddField(
            model_name='lesson',
            name='title_en',
            field=models.CharField(max_length=255, null=True, verbose_name='Tema'),
        ),
        migrations.AddField(
            model_name='lesson',
            name='title_ru',
            field=models.CharField(max_length=255, null=True, verbose_name='Tema'),
        ),
    ]
