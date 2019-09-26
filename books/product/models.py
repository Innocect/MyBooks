from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.utils.text import slugify

# Create your models here.

condition_types = (
    ('New', 'New'),
    ('Used', 'Used')
)


class Product(models.Model):
    # have all items in here
    name = models.CharField(max_length=100)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.TextField(max_length=500)
    category = models.ForeignKey('Category', on_delete=models.SET_NULL, null=True)
    brand = models.ForeignKey('Brand', on_delete=models.SET_NULL, null=True)
    condition = models.CharField(max_length=100, choices=condition_types)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    image = models.ImageField(upload_to='main_product/', blank=True, null=True)
    created = models.DateTimeField(default=timezone.now)

    slug = models.SlugField(blank=True, null=True)  # For Urls

    def save(self, *args, **kwargs):
        if not self.slug and self.name:
            self.slug = slugify(self.name)
        super(Product, self).save(*args, **kwargs)

    def __str__(self):
        return self.name


class Category(models.Model):
    category_name = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.category_name


class ProductImages(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='products/', blank=True, null=True)

    def __str__(self):
        return self.product.name

    class Meta:
        verbose_name = 'product Image'
        verbose_name_plural = 'product Images'


class Brand(models.Model):
    brand_name = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'Brand'
        verbose_name_plural = 'Brands'

    def __str__(self):
        return self.brand_name
