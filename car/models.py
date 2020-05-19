from ckeditor.widgets import CKEditorWidget
from django.db import models
from django.contrib.auth.models import User
# Create your models here.
from django.forms import ModelForm, TextInput, FileInput, Select, NumberInput
from django.urls import reverse
from django.utils.safestring import mark_safe
from ckeditor_uploader.fields import RichTextUploadingField
from mptt.fields import TreeForeignKey
from mptt.models import MPTTModel


class Category(MPTTModel):
    STATUS = (
        ('True', 'Evet'),
        ('False' , 'Hayır'),
    )
    title = models.CharField(max_length=150)
    keywords = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    image = models.ImageField(blank=True, upload_to='images/')
    status = models.CharField(max_length=10, choices=STATUS)
    slug = models.SlugField(null=False, unique=True)
    parent = TreeForeignKey('self',blank=True, null=True, related_name='children', on_delete=models.CASCADE)
    create_up = models.DateTimeField(auto_now_add=True)
    update_up = models.DateTimeField(auto_now=True)

    class MPTTMeta:
        order_insertion_by = ['title']

    def __str__(self):  # alt kategori olduğu sürece alt kat arar
        full_path = [self.title]
        k = self.parent
        while k is not None:
            full_path.append(k.title)
            k = k.parent
        return ' / '.join(full_path[::-1])  # ard arda getirir

    def image_tag(self):
        return mark_safe('<img src="{}" height="50"/>'.format(self.image.url))
    image_tag.short_description = 'Image'

    def get_absolute_url(self):
        return reverse('category_detail', kwargs={'slug': self.slug})
STATUS = (
    ('True', 'Evet'),
    ('False', 'Hayır'),
)
SITUATION = (
    ('True','Used'),
    ('False','New'),
)
class Car(models.Model):

    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True )
    title = models.CharField(max_length=150)
    keywords = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    slug = models.SlugField(null=False, unique=True)
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

    def get_absolute_url(self):
        return reverse('car_detail', kwargs={'slug': self.slug})
class Images(models.Model):
    car = models.ForeignKey(Car,on_delete=models.CASCADE)
    title = models.CharField(max_length=150, blank=True)
    image = models.ImageField(blank=True, upload_to='images/')

    def __str__(self):
        return self.title

    def image_tag(self):
        return mark_safe('<img src="{}" height="50"/>'.format(self.image.url))
    image_tag.short_description = 'Image'

class Comment(models.Model):
    STATUS = (
        ('New','Yeni'),
        ('True', 'Evet'),
        ('False', 'Hayır'),
    )
    car = models.ForeignKey(Car,on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    subject = models.CharField(max_length=50,blank=True)
    comment = models.TextField(max_length=200, blank=True)
    status = models.CharField(max_length=10, choices=STATUS, default='New')
    ip = models.CharField(max_length=20, blank=True)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.subject

class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['subject','comment']


class CarForm(ModelForm):
    class Meta:
        model = Car
        fields = {'category','title','keywords','description','slug','image','price','year',
                  'fuel','gear', 'km','motorpower','color','situation','detail'}
        widgets = {
            'title': TextInput(attrs={'class': 'form-group', 'placeholder': 'Başlık'}),
            'category': Select(attrs={'class': 'input', 'placeholder': ''}, choices=Category.objects.all()),
            'slug': TextInput(attrs={'class': 'form-group', 'placeholder': 'Slug'}),
            'keywords': TextInput(attrs={'class': 'form-group', 'placeholder': 'Keywords'}),
            'description': TextInput(attrs={'class': 'form-group', 'placeholder': 'Description'}),
            'image': FileInput(attrs={'class': 'form-group', 'placeholder': 'Image'}),
            'price': NumberInput(attrs={'class': 'form-group', 'placeholder': 'Fiyat'}),
            'year': NumberInput(attrs={'class': 'form-group', 'placeholder': 'Yıl'}),
            'fuel': TextInput(attrs={'class': 'form-group', 'placeholder': 'Yakıt'}),
            'gear':TextInput(attrs={'class': 'form-group', 'placeholder': 'Vites'}),
            'km':NumberInput(attrs={'class': 'form-group', 'placeholder': 'Kilometre'}),
            'motorpower':NumberInput(attrs={'class': 'form-group', 'placeholder': 'Motor Gücü'}),
            'color': TextInput(attrs={'class': 'form-group', 'placeholder': 'Renk'}),
            'situation':Select(attrs={'class': 'form-group', 'placeholder': 'Type'}, choices=SITUATION),
            'detail': CKEditorWidget(),
        }