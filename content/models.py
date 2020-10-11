from ckeditor.widgets import CKEditorWidget
from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from django.forms import FileInput, TextInput, Select, ModelForm
from django.urls import reverse
from django.utils.safestring import mark_safe
from mptt.fields import TreeForeignKey
from mptt.models import MPTTModel

from car.models import Car


class Menu(MPTTModel):
    STATUS = (
        ('True', 'Evet'),
        ('False', 'Hayır'),
    )
    parent = TreeForeignKey('self', blank=True, null=True, related_name='children', on_delete=models.CASCADE)
    title = models.CharField(max_length=100, unique=True)
    link = models.CharField(max_length=100, blank=True)
    status = models.CharField(max_length=10, choices=STATUS)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    class MPTTMeta:
        order_insertion_by = ['title']

    def __str__(self):  # alt kategori olduğu sürece alt kat arar
        full_path = [self.title]
        k = self.parent
        while k is not None:
            full_path.append(k.title)
            k = k.parent
        return ' / '.join(full_path[::-1])  # ard arda getirir
TYPE = (
        ('menu', 'menu'),
        ('duyuru', 'duyuru'),
        ('ilan', 'ilan'),
    )
STATUS = (
        ('True', 'Evet'),
        ('False', 'Hayır'),
    )
class Content(models.Model):

    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True )
    menu = models.OneToOneField(Menu, null=True, on_delete=models.CASCADE)
    type = models.CharField(max_length=10, choices=TYPE)
    title = models.CharField(max_length=150)
    keywords = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    image = models.ImageField(blank=True, upload_to='images/')
    detail = RichTextUploadingField()
    slug = models.SlugField(null=False, unique=True)
    status = models.CharField(max_length=10, choices=STATUS)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def image_tag(self):
        return mark_safe('<img src="{}" height="50"/>'.format(self.image.url))
    image_tag.short_description = 'Image'

    def get_absolute_url(self):
        return reverse('content_detail', kwargs={'slug': self.slug})

class ContentForm(ModelForm):
    class Meta:
        model = Content
        fields = ['type', 'title', 'slug', 'keywords', 'description', 'image', 'detail']
        widgets = {
            'title': TextInput(attrs={'class': 'form-group', 'placeholder': 'Başlık'}),
            'slug': TextInput(attrs={'class': 'form-group', 'placeholder': 'Slug'}),
            'keywords': TextInput(attrs={'class': 'form-group', 'placeholder': 'Keywords'}),
            'description': TextInput(attrs={'class': 'form-group', 'placeholder': 'Description'}),
            'type': Select(attrs={'class': 'form-group', 'placeholder': 'Type'}, choices=TYPE),
            'image': FileInput(attrs={'class': 'form-group', 'placeholder': 'Image'}),
            'detail': CKEditorWidget(),
        }

class CImages(models.Model):
    content = models.ForeignKey(Content,on_delete=models.CASCADE)
    title = models.CharField(max_length=50, blank=True)
    image = models.ImageField(blank=True, upload_to='images/')

    def __str__(self):
        return self.title

    def image_tag(self):
        return mark_safe('<img src="{}" height="50"/>'.format(self.image.url))
    image_tag.short_description = 'Image'

class CarForm(ModelForm):
    class Meta:
        model = Car
        fields = ['title','year']