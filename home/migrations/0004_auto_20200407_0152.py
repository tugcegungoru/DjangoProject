# Generated by Django 3.0.4 on 2020-04-06 23:52

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_auto_20200404_2242'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactFormMessage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.AddField(
            model_name='setting',
            name='ip',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AddField(
            model_name='setting',
            name='message',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='setting',
            name='name',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AddField(
            model_name='setting',
            name='note',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='setting',
            name='subject',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='setting',
            name='aboutus',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True),
        ),
        migrations.AlterField(
            model_name='setting',
            name='contact',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True),
        ),
        migrations.AlterField(
            model_name='setting',
            name='references',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True),
        ),
        migrations.AlterField(
            model_name='setting',
            name='status',
            field=models.CharField(choices=[('True', 'Evet'), ('False', 'Hayır')], default='New', max_length=10),
        ),
    ]
