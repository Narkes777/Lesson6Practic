from django.contrib import admin
from .models import Car, Manufacturer

# Register your models here.

class CarAdmin(admin.ModelAdmin):
    list_display = ['lada', 'year', 'price', 'manufacturer']
    ordering = ['-lada']
    search_fields = ['year']

class ManufacturerAdmin(admin.ModelAdmin):
    list_display = ['name', 'country']
    list_filter = ['country']

admin.site.register(Car, CarAdmin)
admin.site.register(Manufacturer, ManufacturerAdmin)
