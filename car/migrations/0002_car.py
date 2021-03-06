# Generated by Django 3.0.4 on 2020-03-09 18:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('car', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('keywords', models.CharField(max_length=255)),
                ('description', models.CharField(max_length=255)),
                ('image', models.ImageField(blank=True, upload_to='images/')),
                ('price', models.FloatField()),
                ('year', models.IntegerField()),
                ('fuel', models.CharField(max_length=15)),
                ('gear', models.CharField(max_length=20)),
                ('km', models.IntegerField()),
                ('motorpower', models.IntegerField()),
                ('color', models.CharField(max_length=20)),
                ('situation', models.CharField(choices=[('True', 'Used'), ('False', 'New')], max_length=10)),
                ('status', models.CharField(choices=[('True', 'Evet'), ('False', 'Hayır')], max_length=10)),
                ('detail', models.TextField()),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='car.Category')),
            ],
        ),
    ]
