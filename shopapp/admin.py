from django.contrib import admin
from .models import Collection, Product, Comment, Post
from django_summernote.admin import SummernoteModelAdmin


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


@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):
    list_display = ('name', 'slug', 'status', 'created_on')
    search_fields = ['name', 'content']
    list_filter = ('status', 'created_on')
    prepopulated_fields = {'slug': ('name',)}
    summernote_fields = ('content',)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'body', 'review', 'created_on', 'thumbs_up')
    list_filter = ['created_on']
    search_fields = ('name', 'email', 'body')
    actions = ['rate_comments']

    def rate_comments(self, request, queryset):
        queryset.update(approved=True)