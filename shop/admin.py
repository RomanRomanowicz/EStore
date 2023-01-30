from django.contrib import admin
from shop.models.category import *
from shop.models.products import *

# Register your models here.
admin.site.register(Product)
admin.site.register(Image)
admin.site.register(Category)
admin.site.register(CategoryColor)
admin.site.register(CategorySize)
