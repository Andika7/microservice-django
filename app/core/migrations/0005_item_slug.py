# Generated by Django 3.0.2 on 2020-02-05 10:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20200205_1029'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='slug',
            field=models.SlugField(default='product'),
            preserve_default=False,
        ),
    ]
