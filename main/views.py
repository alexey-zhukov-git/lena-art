from django.template import loader
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from .models import Category, Product

# Create your views here.
def index(request):
    template = loader.get_template('main/home.html')
    total_orders = 1
    context = {
        'total_orders': total_orders,
        }
    return HttpResponse(template.render(context, request))

def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    quantity = Product.objects.filter(available=True).count()
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    return render(
        request,
        'main/list.html',
        {
            'category': category,
            'categories': categories,
            'products': products,
            'quantity': quantity
        }
    )

def about(request):
    template = loader.get_template('main/about.html')
    context = {}
    return HttpResponse(template.render(context, request))

def contacts(request):
    template = loader.get_template('main/contacts.html')
    context = {}
    return HttpResponse(template.render(context, request))

def products(request):
    template = loader.get_template('main/products.html')
    context = {}
    return HttpResponse(template.render(context, request))

def cart(request):
    template = loader.get_template('main/cart.html')
    context = {}
    return HttpResponse(template.render(context, request))