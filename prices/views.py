from django.shortcuts import render
from .models import Price

def price(request):
    prices=Price.objects.all() #select
    return render(request, "prices/price.html", {'prices': prices})
