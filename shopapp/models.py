from django.db import models
from django.urls import reverse
# from django.contrib.auth.models import User
# from cloudinary.models import CloudinaryField

# Create your models here.
# STATUS = ((0, "Draft"), (1, "Published")) 

# class Post(models.Model):
#     title = models.CharField(max_length=200, unique=True)
#     slugh = models.SlugField(max_length=200, unique=True)
#     author = models.ForeignKey(
#         User, on_delete=models.CASCADE, related_name="blog_posts"
#     )
#     excerpt = models.TextField(blank=True)
#     updated_on = models.DateTimeField(auto_now=True)
#     content = models.TextField()
#     created_on = models.DateTimeField(auto_now_add=True)
#     status = models.IntegerField(choices=STATUS, default=0)
#     likes = models.ManyToManyField(
#         User, related_name='blogpost_like', blank=True)

#     class Meta:
#         ordering = ["-created_on"]

#     def __str__(self):
#         return self.title

#     def number_of_likes(self):
#         return self.likes.count()



# class Comment(models.Model):
#     post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
#     name = models.CharField(max_length=80)
#     email = models.EmailField()
#     body = models.TextField()
#     created_on = models.DateTimeField(auto_now_add=True)
#     approved = models.BooleanField(default=False)

#     class Meta:
#         ordering = ["created_on"]

#     def __str__(self):
#         return f"Comment {self.body} by {self.name}"



class Collection(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True, unique=True)

    class Meta: 
        ordering = ('name',)
        verbose_name = 'collection'
        verbose_name_plural = 'collections'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('shop:item_list_by_collection', args=[self.slug])      




class Product(models.Model):
    collection = models.ForeignKey(Collection, on_delete=models.DO_NOTHING, related_name='products', ) 
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    inventory = models.PositiveIntegerField()
    created = models.DateTimeField(auto_now_add=True)
    available = models.BooleanField(default=True)
    updated = models.DateTimeField(auto_now=True)
    item_image = models.ImageField(upload_to='products/%Y/%m/%d/', blank=True)


    class Meta:
        ordering = ('-created',)
        index_together = (('id', 'slug'),)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('shop:item_description', args=[self.id, self.slug])    