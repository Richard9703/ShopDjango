from django.contrib import admin
from .models import Collection, Product
# from django_summernote.admin import SummernoteModelAdmin

# Post, Comment, 
# @admin.register(Post)
# class PostAdmin(SummernoteModelAdmin):
#     list_display = ('title', 'slug', 'status', 'created_on')
#     search_fields = ('title', 'content')
#     prepopulated_fields = {'slug': ('title')}


# @admin.register(Comment)
# class CommentAdmin(admin.ModelAdmin):
#     list_display = ('name', 'body', 'post', 'created_on', 'approved')
#     list_filter = ('approved', 'created_on')
#     search_fields = ('name', 'email', 'body')
#     actions = ['approve_comments']

#     def approve_comments(self, request, queryset):
#         queryset.update(approved=True)


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