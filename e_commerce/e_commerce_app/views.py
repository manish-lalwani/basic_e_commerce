from django.forms import model_to_dict
from django.shortcuts import render,redirect


from .models import Product
from django.core import serializers
from math import ceil

from django.contrib.auth import login, authenticate
from django.core.mail import send_mail
from django.conf import settings
from .forms import UserLoginForm, UserRegistrationForm
from .models import UserProfile

from django.contrib import messages
from django.contrib.auth.decorators import login_required
# Create your views here.




def login(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(request, username=email, password=password)
            if user is not None:
                login(request, user)
                return redirect('profile')
    else:
        form = UserLoginForm()

    return render(request, 'login.html', {'form': form})



@login_required(login_url='login')
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







def register(request):
    if request.method == 'POST':
        print("In post method")
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            print("got an entry in user table")

            user_profile = UserProfile(
                user=user,
                email=form.cleaned_data['email'],
                address=form.cleaned_data['address']
            )
            user_profile.save()
            print("got an entry in user_profile table")

            # Send activation email
            subject = 'Activate your account'
            message = 'Please click the following link to activate your account: http://localhost:8000/activate/{0}'.format(user_profile.id)
            from_email = settings.EMAIL_HOST_USER
            to_email = [user_profile.email]
            send_mail(subject, message, from_email, to_email, fail_silently=False)
            activateEmail(request=request, user=user, to_email=user_profile.email)
            return redirect('index')
        else:
            # Print the errors to the console
            print(form.errors)
            # Pass the errors to the template
            return render(request, 'register.html', {'form': form, 'errors': form.errors})
    else:
        form = UserRegistrationForm()

    return render(request, 'register.html', {'form': form})

def activate(request, user_profile_id):
    user_profile = UserProfile.objects.get(id=user_profile_id)
    user_profile.user.is_active = True
    user_profile.user.save()

    return render(request, 'activate.html')


def activateEmail(request, user, to_email):
    messages.success(request, f'Dear <b>{user}</b>, please go to you email <b>{to_email}</b> inbox and click on \
        received activation link to confirm and complete the registration. <b>Note:</b> Check your spam folder.')
    



