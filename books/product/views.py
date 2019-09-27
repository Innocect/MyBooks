# from typing import Dict, Any

from django.shortcuts import render
from .models import Product, ProductImages
from django.core.paginator import Paginator


# Create your views here.
def productlist(request):
    product_list = Product.objects.all()
    # print(product_list)
    template = 'Product/product_list.html'

    paginator = Paginator(product_list, 1)  # show only 10 products on 1 page
    page = request.GET.get('page')
    product_list = paginator.get_page(page)

    context = {'product_list': product_list}

    return render(request, template, context)


def productdetail(request, product_slug):
    print(product_slug)
    # product_detail = Product.objects.filter(id=id).first()
    product_detail = Product.objects.get(slug=product_slug)
    productimages = ProductImages.objects.filter(product=product_detail)
    template = 'Product/product_detail.html'
    context = {'product_detail': product_detail, 'product_images': productimages}

    return render(request, template, context)
