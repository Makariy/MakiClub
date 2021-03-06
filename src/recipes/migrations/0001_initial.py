# Generated by Django 3.2.10 on 2021-12-23 19:21

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
            name='Recipe',
            fields=[
                ('title', models.CharField(max_length=255, verbose_name='Title')),
                ('description', models.TextField(verbose_name='Description')),
                ('image', models.FilePathField(verbose_name='Image file')),
                ('recipe_file', models.FilePathField(verbose_name='Recipe file')),
                ('_ingredients', models.TextField(verbose_name='Ingredients')),
                ('date', models.TimeField(auto_now=True)),
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Author')),
            ],
        ),
    ]
