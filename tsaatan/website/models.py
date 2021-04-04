from django.db import models

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=255)
    img = models.ImageField(upload_to="pics")
    img2 = models.ImageField(upload_to="pics")
    price = models.IntegerField()
    sale = models.BooleanField(default=False)
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name


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
