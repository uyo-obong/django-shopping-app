from django.contrib import admin
from .models import Product, Category


class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'old_price', 'new_price', 'category', 'created_at')


admin.site.register(Product, ProductAdmin)


admin.site.register(Category)


