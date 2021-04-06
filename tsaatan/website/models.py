from django.db import models
import datetime
from django.utils import timezone


class Category(models.Model):
    name = models.CharField(max_length=255)
    category_picture = models.ImageField(upload_to="category-pictures")

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=255)
    img = models.ImageField(upload_to="product-pictures")
    img2 = models.ImageField(upload_to="product-pictures")
    price = models.IntegerField()
    sale = models.BooleanField(default=False)
    # gender - {True - male, False - female}
    gender = models.BooleanField(default=True)
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, null=True)
    description = models.TextField(default="")
    is_featured = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class ProductPicture(models.Model):
    picture = models.ImageField(upload_to="product-pictures")
    product = models.ForeignKey(Product, on_delete=models.CASCADE)


class SliderPicture(models.Model):
    name = models.CharField(max_length=255)
    name2 = models.CharField(max_length=255)
    name3 = models.CharField(max_length=255)
    subtitle = models.TextField()
    subtitle2 = models.TextField()
    subtitle3 = models.TextField()
    img = models.ImageField(upload_to="pics")
    img2 = models.ImageField(upload_to="pics")
    img3 = models.ImageField(upload_to="pics")

    def __str__(self):
        return self.name


class Vaucher(models.Model):
    img = models.ImageField(upload_to="pics")
    img2 = models.ImageField(upload_to="pics")
    text = models.TextField()
    text2 = models.TextField()
    title = models.TextField()

    def __str__(self):
        return self.text


class Address(models.Model):
    time = models.CharField(max_length=255)
    img = models.ImageField(upload_to="pics")
    title = models.CharField(max_length=255)
    decription = models.TextField()

    def __str__(self):
        return self.decription


class About(models.Model):
    title = models.CharField(max_length=255)
    decription = models.TextField()
    img = models.ImageField(upload_to="pics")
    description2 = models.TextField()
    img2 = models.ImageField(upload_to="pics")
    employee = models.CharField(max_length=255)
    customer = models.CharField(max_length=255)
    user = models.CharField(max_length=255)
    branch = models.CharField(max_length=255)

    def __str__(self):
        return self.title


class Settings(models.Model):

    logo = models.ImageField(upload_to='settings')
    phone = models.CharField(max_length=255, default="")
    center_address = models.CharField(max_length=255, default="")
    representation = models.TextField(default="")
