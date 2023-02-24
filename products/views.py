from django.http import HttpResponseRedirect
from django.shortcuts import render
from products.models import ProductCategory, Product, Basket
from users.models import User


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


def basket_add(request, product_id):
    product = Product.objects.get(id=product_id)
    baskets = Basket.objects.filter(user=request.user, product=product)

    if not baskets.exists():
        Basket.objects.create(user=request.user, product=product, quantity=1)
    else:
        basket = baskets.first()
        basket.quantity += 1
        basket.save()

    return HttpResponseRedirect(request.META['HTTP_REFERER'])
