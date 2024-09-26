from django.contrib import admin
from parler.admin import TranslatableAdmin

# Register your models here.
from .models import Category, Product
@admin.register(Category)
# class CategoryAdmin(admin.ModelAdmin):
class CategoryAdmin(TranslatableAdmin):
    list_display = ['name', 'slug']
    def get_prepopulated_fields(self, request, obj=None):
        return {'slug': ('name',)}    
    
@admin.register(Product)
class ProductAdmin(TranslatableAdmin):
    list_display = ['name', 'slug', 'price',
    'available', 'created', 'updated']
    list_filter = ['available', 'created', 'updated']
    # this will allow to edit outer table displayed in admin page itself
    list_editable = ['price', 'available']
    # automatically populate certain fields based on the input from another field
    # prepopulated_fields = {'slug': ('name',)}
    # translation does not provide propopulated so same as this can be used
    def get_prepopulated_fields(self, request, obj=None):
        return {'slug': ('name',)}