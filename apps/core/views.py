from django.shortcuts import render

from apps.product.models import Product, Attribute, Category

def index(request):
    men = Attribute.objects.get(slug='men')
    women = Attribute.objects.get(slug='women')

    context = {
    }

    return render(request, 'core/base.html', context)

def frontpage(request):
    #newest_products = Product.objects.filter(gender=gender_slug)[0:8]
    newest_products = Product.objects.all()[0:8]
    menu = Category.objects.filter(parent=None, ordering=0).exclude(attribute__slug='men')

    return render(request, 'core/frontpage.html', {'newest_products': newest_products, 'menu':menu,})

def men(request):
    #newest_products = Product.objects.filter(gender=gender_slug)[0:8]
    products = Product.objects.filter(attribute__slug='men')[0:8]
    #attribute_slug = 'men'
    menu = Category.objects.filter(parent=None, ordering=0).exclude(attribute__slug='women')

    context = {
        'newest_products': products,
        'menu':menu,
    }

    return render(request, 'core/men.html', context)

def women(request):
    #newest_products = Product.objects.filter(gender=gender_slug)[0:8]
    products = Product.objects.filter(attribute__slug='women')[0:8]
    #attribute_slug = 'women'

    menu = Category.objects.filter(parent=None, ordering=0).exclude(attribute__slug='men')

    context = {
        'newest_products': products,
        'menu': menu,
    }

    return render(request, 'core/women.html', context)