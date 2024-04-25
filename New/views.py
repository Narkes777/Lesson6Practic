from dataclasses import fields
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.shortcuts import render
from .models import Car, Manufacturer
from django.urls import reverse_lazy

from re import template
from sre_constants import SUCCESS
from django.http import HttpResponseRedirect, HttpResponse
from django.conf import settings

# Create your views here.

class CarList(ListView):
    model = Car
    context_object_name = 'car_list'

class CarDetail(DetailView):
    model = Car
    context_object_name = 'car'

class CarCreate(CreateView):
    model = Car
    fields = '__all__'
    success_url = reverse_lazy('car_list')

class CarUpdate(UpdateView):
    model = Car
    fields = '__all__'
    success_url = reverse_lazy('car_list')

class CarDelete(DeleteView):
    model = Car
    fields = '__all__'
    success_url = reverse_lazy('car_list')
    template_name = 'New/car_form.html'



class ManufacturerList(ListView):
    model = Manufacturer
    context_object_name = 'manufacturer_list'

class ManufacturerDetail(DetailView):
    model = Manufacturer
    context_object_name = 'manufacturer'

class ManufacturerCreate(CreateView):
    model = Manufacturer
    fields = '__all__'
    success_url = reverse_lazy('manufacturer_list')

class ManufacturerUpdate(UpdateView):
    model = Manufacturer
    fields = '__all__'
    success_url = reverse_lazy('manufacturer_list')

class ManufacturerDelete(DeleteView):
    model = Manufacturer
    fields = '__all__'
    success_url = reverse_lazy('Manufacturer_list')
    template_name = 'New/manufacturer_form.html'
