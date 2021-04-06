from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='home'),
    path('product-grid', views.single, name='product-grid'),
    path('product-single/<int:id>', views.singleProduct, name="product-single"),
    path('all-products', views.allProducts, name="all-products")
]
