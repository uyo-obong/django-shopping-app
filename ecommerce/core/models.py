from django.contrib.auth.admin import User
from django.db import models
from autoslug import AutoSlugField


class Product(models.Model):
    author = models.ForeignKey(User, on_delete=True, default=1)
    title = models.CharField(max_length=200)
    slug = AutoSlugField(populate_from='title')
    old_price = models.FloatField(default=0.00)
    new_price = models.FloatField(default=0.00)
    image = models.ImageField(upload_to='product_photos')
    description = models.TextField(max_length=None)
    category = models.ForeignKey('Category', on_delete=True, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-title', )
        verbose_name = 'product'
        verbose_name_plural = 'products'

    def __str__(self):
        return self.title


class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = AutoSlugField(populate_from='name')

    class Meta:
        ordering = ('name', )
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name
