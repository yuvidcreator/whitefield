from django.urls import path
from .views import *


urlpatterns = [
    path('', HomePage, name="Home-Page"),
    path('about/', AboutPage, name="About-Page"),
    path('contact/', ContactPage, name="Contact-Page"),
    path('login/', LoginPage, name="Login-Page"),
    path('product/', ProductPage, name="Product-Page"),
]