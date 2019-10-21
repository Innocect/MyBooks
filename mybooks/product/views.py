# from typing import Dict, Any

from django.shortcuts import render
from .models import Product, ProductImages, Category
from django.core.paginator import Paginator
from django.db.models import Count
from django.db.models import Q  # For searching purpose
from django.shortcuts import get_object_or_404  # we will replace get by get_object_or_404


# product_list.GET.get()


# Create your views here.
def productlist(request, category_slug=None):
    category = None
    product_list = Product.objects.all()
    # categorylist = Category.objects.all()
    categorylist = Category.objects.annotate(total_products=Count('product'))  # read annotate
    # print(product_list)
    template = 'Product/product_list.html'

    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        product_list = product_list.filter(category=category)

    search_query = request.GET.get('q')
    if search_query:
        product_list = product_list.filter(
            Q(name__icontains=search_query) |
            Q(description__icontains=search_query) |
            Q(condition__icontains=search_query) |
            Q(brand__brand_name__icontains=search_query)

        )




    # elif search_query.isdigit():
    #     product_list = product_list.filter(
    #         Q(price__lte=search_query)
    #
    #     )

    paginator = Paginator(product_list, 4)  # show only 10 products on 1 page
    page = request.GET.get('page')
    product_list = paginator.get_page(page)

    context = {'product_list': product_list, 'category_list': categorylist, 'category': category}

    return render(request, template, context)


def productdetail(request, product_slug):
    # print(product_slug)
    # product_detail = Product.objects.filter(id=id).first()
    product_detail = get_object_or_404(Product, slug=product_slug)
    productimages = ProductImages.objects.filter(product=product_detail)
    template = 'Product/product_detail.html'
    context = {'product_detail': product_detail, 'product_images': productimages}

    return render(request, template, context)
