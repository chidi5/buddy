from apps.product.models import Category

def menu_categories(request):
    categories = Category.objects.filter(parent=None, ordering=0)
    men_categories = Category.objects.filter(parent=None, ordering=0).exclude(attribute__slug='women')
    women_categories = Category.objects.filter(parent=None, ordering=0).exclude(attribute__slug='men')

    context = {
        'menu_categories': categories,
        'men_menu': men_categories,
        'women_menu': women_categories,
    }
    return (context)

def location(request):
    url_parts = request.path.split('/')
    return {
        'url_part': url_parts[1],
    }