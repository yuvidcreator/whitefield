from django.shortcuts import render

# Create your views here.



def HomePage(request):
    return render(request, 'frontend/index.html')




def AboutPage(request):
    return render(request, 'frontend/about-us.html')




def ContactPage(request):
    return render(request, 'frontend/contact.html')




def LoginPage(request):
    return render(request, 'frontend/login.html')



def ProductPage(request):
    return render(request, 'frontend/single-product.html')