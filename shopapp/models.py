from django.db import models
from django.urls import reverse

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