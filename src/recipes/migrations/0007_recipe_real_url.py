# Generated by Django 3.2.10 on 2022-06-20 13:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0006_auto_20220618_1748'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='real_url',
            field=models.TextField(null=True, verbose_name='Real url'),
        ),
    ]
