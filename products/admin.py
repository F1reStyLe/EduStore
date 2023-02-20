from django.contrib import admin

from products.models import ProductCategory, Product
from users.models import User


@admin.register(ProductCategory)
class ProductCategoryAdmin(admin.ModelAdmin):
    pass


@admin.register(Product)
class Product(admin.ModelAdmin):
    pass


@admin.register(User)
class User(admin.ModelAdmin):
    pass
