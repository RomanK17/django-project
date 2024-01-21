from django.shortcuts import render, HttpResponse

from products.models import Product,ProductsCategory

def index(request):
    context = {'title': 'test',
    'is_promotion' : True
               }
    return render(request, 'products/index.html', context)

def products(request):
    context = {
        'title' : 'Catalog',
        'products': Product.objects.all(),
        'categories': ProductsCategory.objects.all()
    }
    return render(request, 'products/products.html', context)
