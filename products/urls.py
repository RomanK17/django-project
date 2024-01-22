from django.urls import path

from products.views import products

app_name = 'products' # для чего ее указывать? чтобы в urls можно так ссылаться products:index

urlpatterns = [
    path('', products, name='index') # что такое path? что значат эти аргументы? 1 - путь, куда будет переходить
    # пользователь(то есть просто продактс). 2- наше приложение. 3. - как у нас будет называться вьюха.
]
