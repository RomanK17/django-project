from django.db import models

# Create your models here.


class ProductsCategory(models.Model):
    # зачем мы здесь перед классами CharField и тд добавляем скобки?
    # где поле id? primary_key=True сделает поле по умолчанию id(по дефолту джанго сам создает столбец id)
    name = models.CharField(max_length=128) # что такое max_length? что такое CharField?
    description = models.TextField(null=True, blank=True) # В чем отличие от CharField? для чего добавлять null=True, blank=True? (чтобы это строка могла быть пустой в таблице)
    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=256)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2) # что за тип данных? max_digits - максимальное число до запятой, decimal_places - после
    quantity = models.PositiveIntegerField(default=0) # default = значение для строки по умолчанию. Что за PositiveIntegerField?
    image = models.ImageField(upload_to='products_images') # папка, где сохраняем картинки
    # связываем с таблицей ProductsCategory
    category = models.ForeignKey(to=ProductsCategory, on_delete=models.CASCADE) # класс CASCADE не вызывается. При CASCADE удаляются связанные категории. Еще есть Set_default/ PROTECT. Что за ForeignKey, to=ProductsCategory?

    def __str__(self):
        return f'Товар:{self.name} из категории: {self.category.name}'