from django.forms import model_to_dict
from django.shortcuts import render
from .models import Product
from django.core import serializers
from math import ceil
# Create your views here.
def index(request):
    context={}
    #products = Product.objects.all()
    products = list(Product.objects.values())
    context["products"] = products
    no_of_slides = len(products) // 4 if len(products) % 4 != 0 else  (len(products) // 4) +1
    context["no_of_slides"] = no_of_slides
    context["range"] = range(1,no_of_slides - 1)
    context["total_products_count"] = len(products)

    # Convert the QuerySet to a list of dictionaries
   # product_list = [model_to_dict(product) for product in products]

    # Serialize the list to JSON
    #product_json = serializers.serialize('json', products)

    context["products_json"] = products


    return render(request=request,template_name="index.html",context=context)

def contact(request):
    return render(request=request,template_name="contact.html")

def about(request):
    return render(request=request,template_name="about.html")

def tracker(request):
    return render(request=request,template_name="tracker.html")

def search(request):
    return render(request=request,template_name="search.html")

def product_view(request):
    return render(request=request,template_name="product_view.html")

def checkout(request):
    return render(request=request,template_name="checkout.html")


