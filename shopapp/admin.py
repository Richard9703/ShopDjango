from django.contrib import admin
from .models import Collection, Product



@admin.register(Collection)
class CollectionAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    list_filter = ['name']
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ['name', 'slug']



@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'collection', 'price', 'inventory', 'created', 'updated', 'available']
    list_filter = ['collection', 'created', 'updated', 'available']
    list_editable = ['inventory', 'price', 'available']
    search_fields = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}

