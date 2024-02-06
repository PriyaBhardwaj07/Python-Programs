from django.contrib import admin
from .models.product import Product
from .models.category import Category
# Register your models here.

class ProductTable(admin.ModelAdmin):
    list_display=['name','price','category','rating','discount','colors']
    
class CategoryTable(admin.ModelAdmin):
    list_display=['name']

admin.site.register(Product,ProductTable)
admin.site.register(Category)