from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('single', views.single, name='single'),
    path('singleProduct', views.singleProduct, name="singleProduct")
]
