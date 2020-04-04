from django.contrib import admin

# Register your models here.
from car.models import Category, Car, Images

class CarImageInline(admin.TabularInline):
    model = Images
    extra = 5

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'status']
    list_filter = ['status']

class CarAdmin(admin.ModelAdmin):
    list_display = ['title', 'category','price','year', 'fuel','gear','km','situation','status']
    list_filter = ['status', 'category']
    inlines = [CarImageInline]

class ImagesAdmin(admin.ModelAdmin):
    list_display = ['title', 'car', 'image']
admin.site.register(Category, CategoryAdmin)
admin.site.register(Car, CarAdmin)
admin.site.register(Images, ImagesAdmin)
