# Generated by Django 3.0.4 on 2020-04-18 23:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('car', '0005_auto_20200407_0152'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='price',
            field=models.IntegerField(),
        ),
    ]
