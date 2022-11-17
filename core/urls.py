from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('about/', views.about, name= "about"),
    path('price/', views.price, name= "price"),
    path('contact/', views.contact, name= "contact"),
    path('testimonial/', views.testimonial, name= "testimonial"),
]