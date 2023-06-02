from django.shortcuts import render
from .models import *
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.template import loader
from django.db.models import Count
# Create your views here.

def home_views(request):
    context={}
    context['products'] = Product.objects.all()
    context['categories'] = Category.objects.annotate(number_of_product = Count("product"))
    context['brands'] = Brand.objects.annotate(number_of_product = Count("product"))
    context['sellers'] = Seller.objects.annotate(number_of_product = Count("product"))
    context['warranties'] = Warranty.objects.annotate(number_of_product = Count("product"))
    return render(request, 'index.html', context)


def search_product(request):
    products = Product.objects.all()
    if 'brand[]' in request.GET:
        brands = request.GET.getlist('brand[]')
        products = Product.objects.filter(brand__name__in=brands)
    if 'seller[]' in request.GET:
        sellers = request.GET.getlist('seller[]')
        products = Product.objects.filter(seller__name__in=sellers)
    if 'warrenty[]' in request.GET:
        warrenties = request.GET.getlist('warrenty[]')
        products = Product.objects.filter(warranty__warranty_period__in=warrenties)
    products_item_html = loader.render_to_string('searched_product.html', {'products': products})
    return JsonResponse({"valid": True, 'products_item_html': products_item_html})


def category_products(request, name):
    context={}
    products = Product.objects.filter(category__name=name)
    category = Category.objects.get(name=name)

    if 'start_price' and 'end_price' in request.GET:
        start_price = request.GET.get('start_price')
        end_price = request.GET.get('end_price')
        products = products.filter(price__range=(start_price, end_price))

    context['products'] = products
    context['category'] = category
    context['categories'] = Category.objects.annotate(number_of_product = Count("product")).all()
    context['brands'] = Brand.objects.annotate(number_of_product = Count("product")).all()
    context['sellers'] = Seller.objects.annotate(number_of_product = Count("product")).all()
    context['warranties'] = Warranty.objects.annotate(number_of_product = Count("product")).all()
    return render(request, 'category-products.html', context)