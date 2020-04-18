from django.db import models

# Create your models here.
from django.utils.safestring import mark_safe
from ckeditor_uploader.fields import RichTextUploadingField


class Category(models.Model):
    STATUS = (
        ('True', 'Evet'),
        ('False' , 'Hayır'),
    )
    title = models.CharField(max_length=150)
    keywords = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    image = models.ImageField(blank=True, upload_to='images/')
    status = models.CharField(max_length=10, choices=STATUS)
    slug = models.SlugField()
    parent = models.ForeignKey('self',blank=True, null=True, related_name='children', on_delete=models.CASCADE)
    create_up = models.DateTimeField(auto_now_add=True)
    update_up = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def image_tag(self):
        return mark_safe('<img src="{}" height="50"/>'.format(self.image.url))
    image_tag.short_description = 'Image'


class Car(models.Model):
    STATUS = (
        ('True', 'Evet'),
        ('False', 'Hayır'),
    )
    SITUATION = (
        ('True','Used'),
        ('False','New'),
    )
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=150)
    keywords = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    slug = models.SlugField()
    image = models.ImageField(blank=True, upload_to='images/')
    price = models.IntegerField()
    year = models.IntegerField()
    fuel = models.CharField(max_length=15)
    gear = models.CharField(max_length=20)
    km = models.IntegerField()
    motorpower = models.IntegerField()
    color = models.CharField(max_length=20)
    situation = models.CharField(max_length=10, choices=SITUATION)
    status = models.CharField(max_length=10, choices=STATUS)
    detail = RichTextUploadingField()
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def image_tag(self):
        return mark_safe('<img src="{}" height="50"/>'.format(self.image.url))
    image_tag.short_description = 'Image'

class Images(models.Model):
    car = models.ForeignKey(Car,on_delete=models.CASCADE)
    title = models.CharField(max_length=150, blank=True)
    image = models.ImageField(blank=True, upload_to='images/')

    def __str__(self):
        return self.title

    def image_tag(self):
        return mark_safe('<img src="{}" height="50"/>'.format(self.image.url))
    image_tag.short_description = 'Image'
