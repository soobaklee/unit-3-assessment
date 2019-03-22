from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView
from django.views.generic import ListView

from .models import Item

# Create your views here.

class HomeList(ListView):
    template_name = 'home.html'
    model = Item
    context_object_name = 'items'

class WishCreate(CreateView):
    template_name = "item_form.html"
    model = Item
    fields = '__all__'
    success_url = '/'

# class WishDelete(DeleteView):
#     model = Item
#     success_url = '/'
