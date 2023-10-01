from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request=request,template_name="index.html")

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


