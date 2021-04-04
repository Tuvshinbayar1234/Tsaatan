from django.shortcuts import render
from .models import Product
from .models import SliderPicture
from .models import Vaucher
from .models import Address
from .models import About
# Create your views here.


def index(request):

    pro = Product.objects.all()
    slider = SliderPicture.objects.all()
    giveaway = Vaucher.objects.all()[:1]
    addres = Address.objects.all()
    abouts = About.objects.all()
    return render(request, 'index.html', {'pro': pro, 'slider': slider, 'giveaway': giveaway, 'addres': addres, 'abouts': abouts})


def single(request):
    abouts = About.objects.all()

    return render(request, 'single-product.html' , {'abouts': abouts})


def singleProduct(request):
    abouts = About.objects.all()

    return render(request, 'single.html', {'abouts': abouts})
