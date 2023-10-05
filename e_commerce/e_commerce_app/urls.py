from django.urls import path
from . import views


urlpatterns = [
    path("",views.index,name="index"),
    path("contact",views.contact,name="contact"),
    path("about",views.about,name="about"),
    path("tracker",views.tracker,name="tracker"),
    path("search",views.search,name="search"),
    path("product_view",views.product_view,name="productview"),
    path("checkout",views.checkout,name="checkout"),
    path("register",views.register,name="register"),
    path("login",views.login,name="login"),
    path('activate/<int:user_profile_id>/', views.activate, name='activate')

 ]