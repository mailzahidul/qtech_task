from django.contrib import admin
from .models import *
# Register your models here.


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']


class BrandAdmin(admin.ModelAdmin):
    list_display = ['name']


class EarphoneAdmin(admin.ModelAdmin):
    list_display = ['name']


admin.site.register(Earphone, EarphoneAdmin)


class ProductTypeAdmin(admin.ModelAdmin):
    list_display = ['name']


class SellerAdmin(admin.ModelAdmin):
    list_display = ['name']


class WarrantyAdmin(admin.ModelAdmin):
    list_display = ['warranty_period']


class ProductAdmin(admin.ModelAdmin):
    list_display = ['name','price','category', 'brand', 'warranty']


admin.site.register(Warranty, WarrantyAdmin)
admin.site.register(Seller, SellerAdmin)
admin.site.register(ProductType, ProductTypeAdmin)
admin.site.register(Brand, BrandAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)