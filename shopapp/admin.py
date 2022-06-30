from django.contrib import admin
from .models import Collection, Product



class CollectionAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}
admin.site.register(Collection, CollectionAdmin)  


class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'collection', 'price', 'inventory', 'created', 'updated', 'available']
    list_filter = ['collection', 'created', 'updated', 'available']
    list_editable = ['inventory', 'price', 'available']
    prepopulated_fields = {'slug': ('name',)}
admin.site.register(Product, ProductAdmin) 