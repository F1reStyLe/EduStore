from django.db import models


class ProductCategory(models.Model):
    name = models.CharField(max_length=128, null=False, db_index=True, verbose_name="Имя категории")
    description = models.TextField(null=True, blank=True, verbose_name="Описание")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"
