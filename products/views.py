from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from products.models import Product, ProductsCategory, Basket


def index(request):
    context = {'title': 'test',
               'is_promotion': True
               }
    return render(request, 'products/index.html', context)


def products(request, category_id=None):
    if category_id:
        category = ProductsCategory.objects.get(id=category_id)
        products = Product.objects.filter(category=category)
    else:
        products = Product.objects.all()

    context = {
        'title': 'Catalog',
        'products': products,
        'categories': ProductsCategory.objects.all()
    }
    return render(request, 'products/products.html', context)


@login_required()
def add_basket(request, product_id):
    product = Product.objects.get(id=product_id)  # добавляем товар в корзирну
    basket = Basket.objects.filter(user=request.user, product=product)  # берем все корзины пользователя

    if not basket.exists():
        Basket.objects.create(user = request.user, product=product, quantity=1)
    else:
        basket = basket.first() # в queryset у нас всегда один элемент
        basket.quantity += 1 # добавляем количество товара
        basket.save()

    return HttpResponseRedirect(request.META['HTTP_REFERER']) # возвращает пользователя на обновленную страницу


def remove_basket(request, basket_id):
    basket = Basket.objects.get(id=basket_id)
    basket.delete()
    return HttpResponseRedirect(request.META['HTTP_REFERER'])