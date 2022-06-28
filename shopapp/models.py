from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

# Create your models here.
STATUS = ((0, "Draft"), (1, "Published")) 

class Category(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField()
    parent = models.ForeignKey('self', blank=True, null=True, related_name='children')

    class Meta:
        unique_together = ('slug', 'parent',)
        verbose_name_plural = "categories"

    def __str__(self):
        full_path = [self.name]
        k = self.parent
        while k is not None:
            full_path.append(k.name)
            k - k.parent
        return '->'.join(full_path[::1])    

class Post(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, default=1)   
    title = models.CharField(max_length=120) 
    category = models.ForeignKey('Category', null=True, blank=True) 
    content = HTMLField('Content')
    draft = models.BooleanField(default=False)
    publish = models.DateField(auto_now=False, auto_now_add=False,)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.title

    