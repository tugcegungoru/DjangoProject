# Generated by Django 3.0.4 on 2020-06-01 11:18

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('car', '0023_auto_20200601_1327'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='phone',
            field=models.IntegerField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
