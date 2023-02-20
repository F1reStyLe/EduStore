from django.shortcuts import render
from products.models import ProductCategory, Product


def index(request):
    return render(request, 'products/index.html')


def products(request):
    category = ProductCategory.objects.all()
    product = Product.objects.all()
    context = {
        "title": "Store",
        "categories": category,
        "products": product,
    }

    return render(request, 'products/products.html', context)
