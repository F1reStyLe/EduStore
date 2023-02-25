from django.urls import path

from products.views import index, products, basket_add, basket_remove

urlpatterns = [
    path('', index, name="index"),
    path('products/', products, name="products"),
    path('category/<int:category_id>', products, name="category"),
    path('products/baskets/add/<int:product_id>', basket_add, name='basket_add'),
    path('products/baskets/remove/<int:basket_id>', basket_remove, name='basket_remove'),
]