from django.shortcuts import render
from .models import *
from django.http import JsonResponse
from django.core import serializers


def index(request):

    # pro = Product.objects.all()[:5]
    latest_products = Product.objects.all().order_by(
        '-created_date').exclude(sale=True, is_featured=True)[:10]
    featured_products = Product.objects.filter(
        is_featured=True)
    sales_products = Product.objects.filter(
        sale=True)
    all_products = Product.objects.all().order_by(
        "-sale").order_by("-is_featured")[:10]
    # "-sale").order_by("-is_featured")[:10].order_by("-created_date")
    slider = SliderPicture.objects.all()
    giveaway = Vaucher.objects.all()[:1]
    addres = Address.objects.all()
    about = About.objects.first()
    categories = Category.objects.all()
    return render(request, 'index.html', {'categories': categories,
                                          'all_products': all_products,
                                          'slider': slider,
                                          'giveaway': giveaway,
                                          'addres': addres,
                                          'about': about})


def single(request):
    abouts = About.objects.all()
    categories = Category.objects.all()
    return render(request, 'single-product.html', {'categories': categories, 'abouts': abouts})


def singleProduct(request, id):
    abouts = About.objects.all()
    product = Product.objects.get(id=id)
    slider_pictures = ProductPicture.objects.filter(product=product)
    featured_products = Product.objects.order_by('?').exclude(id=id)[:4]

    return render(request, 'single.html', {'abouts': abouts,
                                           'product': product,
                                           'slider_pictures': slider_pictures,
                                           'featured_products': featured_products
                                           })


def allProducts(request):

    # data = serializers.serialize('json', Product.objects.all())

    productData = []
    # productData["products"] = []

    for product in Product.objects.all():
        productData.append({
            'id': product.id,
            'name': product.name,
            'price': product.price,
            'imgSrc1': product.img.url,
            'imgSrc2': product.img2.url,
            'gender': 'Эрэгтэй' if product.gender else 'Эмэгтэй',
            'category': product.category.name,
            'hassale': product.sale
        })

    categoryData = []
    # categoryData["products"] = []

    for category in Category.objects.all():
        categoryData.append({
            'id': category.id,
            'name': category.name,
        })

    return JsonResponse({'products': productData, 'category': categoryData})


def view_404(request, exception):
    return render(request, "404.html")
