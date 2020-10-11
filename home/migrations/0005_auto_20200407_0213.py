# Generated by Django 3.0.4 on 2020-04-07 00:13

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_auto_20200407_0152'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='setting',
            name='ip',
        ),
        migrations.RemoveField(
            model_name='setting',
            name='message',
        ),
        migrations.RemoveField(
            model_name='setting',
            name='name',
        ),
        migrations.RemoveField(
            model_name='setting',
            name='note',
        ),
        migrations.RemoveField(
            model_name='setting',
            name='subject',
        ),
        migrations.AddField(
            model_name='contactformmessage',
            name='create_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='contactformmessage',
            name='email',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name='contactformmessage',
            name='ip',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AddField(
            model_name='contactformmessage',
            name='message',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='contactformmessage',
            name='name',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AddField(
            model_name='contactformmessage',
            name='note',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='contactformmessage',
            name='status',
            field=models.CharField(choices=[('New', 'New'), ('Read', 'Read')], default='New', max_length=10),
        ),
        migrations.AddField(
            model_name='contactformmessage',
            name='subject',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name='contactformmessage',
            name='update_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='setting',
            name='status',
            field=models.CharField(choices=[('True', 'Evet'), ('False', 'Hayır')], max_length=10),
        ),
    ]