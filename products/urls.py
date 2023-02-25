from django.urls import path

from products.views import IndexView, products, basket_add, basket_remove

urlpatterns = [
    path('', IndexView.as_view(), name="index"),
    path('products/', products, name="products"),
    path('category/<int:category_id>', products, name="category"),
    path('page/<int:page_number>', products, name="paginator"),
    path('products/baskets/add/<int:product_id>', basket_add, name='basket_add'),
    path('products/baskets/remove/<int:basket_id>', basket_remove, name='basket_remove'),
]