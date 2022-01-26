from unicodedata import category
from django.contrib import admin
from .models import MenuItem, OrderModel, Category

# Register your models here.
admin.site.register(MenuItem)
admin.site.register(OrderModel)
admin.site.register(Category)
