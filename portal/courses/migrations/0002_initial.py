# Generated by Django 4.0.3 on 2022-04-29 06:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Avtor'),
        ),
        migrations.AddField(
            model_name='comment',
            name='lesson',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses.lesson', verbose_name='Dars'),
        ),
        migrations.AlterUniqueTogether(
            name='lesson',
            unique_together={('number', 'course')},
        ),
    ]