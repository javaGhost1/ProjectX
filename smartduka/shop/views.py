from django.shortcuts import render, get_object_or_404
from .models import *

# Create your views here.
def product_list(request):
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    laptops = Product.objects.filter(category=1).order_by('id')[:3]
    speakers = Product.objects.filter(category=2)
    # screens = Product.objects.filter(categories.name=='screen')
    latest = products.order_by('-id')[:6]
    context = {'products':products, 'categories':categories, 'laptops':laptops, 'speakers':speakers, 'latest':latest}
    return render(request, 'product/index.html', context)