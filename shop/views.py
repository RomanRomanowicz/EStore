from django.shortcuts import render
from django.views.generic import ListView

from shop.models.products import Product


class HomePageView(ListView):
    model = Product
    context_object_name = 'home'
    template_name = 'shop/home.html'