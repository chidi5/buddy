from django.contrib import admin
from .models import *

admin.site.register(Attribute)
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(ProductImage)