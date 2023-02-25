from django.db import models
from users.models import User


class ProductCategory(models.Model):
    name = models.CharField(max_length=128, null=False, db_index=True, verbose_name="Имя категории")
    description = models.TextField(null=True, blank=True, verbose_name="Описание")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"


class Product(models.Model):
    name = models.CharField(max_length=128, db_index=True, null=False, verbose_name="Имя продукта")
    description = models.TextField(verbose_name="Описание")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Цена")
    quantity = models.PositiveSmallIntegerField(default=0, verbose_name="Количество")
    image = models.ImageField(upload_to="products_images", verbose_name="Изображение")
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE, verbose_name='Категория')

    def __str__(self):
        return f"{self.name} | {self.category}"

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"


class BasketQuerySet(models.QuerySet):
    def total_sum(self):
        return sum(basket.sum() for basket in self)

    def total_quantity(self):
        return sum(basket.quantity for basket in self)


class Basket(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE, verbose_name='Пользователь')
    product = models.ForeignKey(to=Product, on_delete=models.CASCADE, verbose_name='Продукт')
    quantity = models.PositiveSmallIntegerField(default=0, verbose_name='Количество')
    created_timestamp = models.DateTimeField(auto_now_add=True, verbose_name='Время добавления')

    objects = BasketQuerySet.as_manager()

    def __str__(self):
        return f'Корзина {self.user.username} | Продукт {self.product.name}'

    def sum(self):
        return self.product.price * self.quantity

    class Meta:
        verbose_name = 'Корзина'
        verbose_name_plural = 'Корзины'
