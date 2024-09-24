from django.contrib import admin

# Register your models here.
from .models import Category, Product
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}
    
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'price',
    'available', 'created', 'updated']
    list_filter = ['available', 'created', 'updated']
    # this will allow to edit outer table displayed in admin page itself
    list_editable = ['price', 'available']
    # automatically populate certain fields based on the input from another field
    prepopulated_fields = {'slug': ('name',)}