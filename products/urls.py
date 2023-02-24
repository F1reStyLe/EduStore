from django.urls import path

from products.views import index, products, basket_add

urlpatterns = [
    path('', index, name="index"),
    path('products/', products, name="products"),
    path('products/baskets/add/<int:product_id>', basket_add, name='basket_add')
]