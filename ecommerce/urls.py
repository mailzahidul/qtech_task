from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_views, name='products'),
    path('search_products', views.search_product, name='search-products'),
    path('category_products/<str:name>', views.category_products, name='category-products'),
]