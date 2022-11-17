from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, "core/home.html")

def about(request):
    return render(request, "core/about.html")

def price(request):
    return render(request, "core/price.html")

def contact(request):
    return render(request, "core/contact.html")

def testimonial(request):
    return render(request, "core/testimonial.html")