from django.shortcuts import render

# Create your views here.
from product.models import Category, Product


def home(request):
    all_category = Category.objects.all()
    products = Product.objects.all()

    template = 'home.html'
    context = {'all_category': all_category, 'products': products}

    return render(request, template, context)
