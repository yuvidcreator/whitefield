from django.shortcuts import render
from .models import *

# Create your views here.


def categories(request):
    return {
        'categories': Category.objects.all()
    }



def HomePage(request):
    products = Product.objects.all()
    context = {'products':products}
    return render(request, 'frontend/index.html', context)




def AboutPage(request):
    return render(request, 'frontend/about-us.html')




def ContactPage(request):
    return render(request, 'frontend/contact.html')




def LoginPage(request):
    return render(request, 'frontend/login.html')



def ProductPage(request):
    return render(request, 'frontend/single-product.html')