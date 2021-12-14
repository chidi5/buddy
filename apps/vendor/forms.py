from django.forms import ModelForm

from .models import Vendor
from apps.product.models import Product, ProductImage


class VendorForm(ModelForm):
    class Meta:
        model = Vendor
        fields = [
            'name',
            'description',
        ] #Note that we didn't mention user field here.

class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ['category', 'attribute', 'image', 'title', 'description', 'price']

class ProductImageForm(ModelForm):
    class Meta:
        model = ProductImage
        fields = ['image']
