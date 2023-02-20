from django.db import models


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
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"