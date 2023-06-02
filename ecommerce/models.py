from django.db import models
from django.utils import timezone


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='category_img/', blank=True, null=True)
    about = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


class Brand(models.Model):
    name = models.CharField(max_length=100)
    logo = models.ImageField(upload_to='brand_logo/', blank=True, null=True)
    about = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


class Earphone(models.Model):
    name = models.CharField(max_length=100)
    logo = models.ImageField(upload_to='brand_logo/', blank=True, null=True)
    object = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


class ProductType(models.Model):
    name = models.CharField(max_length=100)
    logo = models.ImageField(upload_to='brand_logo/', blank=True, null=True)
    about = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


class Seller(models.Model):
    name = models.CharField(max_length=100)
    logo = models.ImageField(upload_to='brand_logo/', blank=True, null=True)
    about = models.TextField(blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    phone = models.SmallIntegerField(blank=True, null=True)

    def __str__(self):
        return self.name


class Warranty(models.Model):
    warranty_period = models.CharField(max_length=100)

    def __str__(self):
        return self.warranty_period


class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.SmallIntegerField()
    description = models.TextField()
    inventory = models.SmallIntegerField()
    feature_image = models.ImageField(upload_to='product_img/')
    multiple_images = models.ImageField(upload_to='product_multiple_img/', blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    brand = models.ForeignKey(Brand, on_delete=models.SET_NULL, null=True, blank=True)
    earphone = models.ForeignKey(Earphone, on_delete=models.SET_NULL, null=True, blank=True)
    product_type = models.ForeignKey(ProductType, on_delete=models.SET_NULL, null=True, blank=True)
    seller = models.ForeignKey(Seller, on_delete=models.SET_NULL, null=True, blank=True)
    warranty = models.ForeignKey(Warranty, on_delete=models.SET_NULL, null=True, blank=True)
    created = models.DateTimeField(editable=False)
    modified = models.DateTimeField(null=True, blank=True)

    def save(self, *args, **kwargs):
        # On save, update timestamps
        if not self.id:
            self.created = timezone.now()
        self.updated = timezone.now()
        return super(Product, self).save(*args, **kwargs)

    def __str__(self):
        return self.name