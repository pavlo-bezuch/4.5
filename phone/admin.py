from django.contrib import admin
from .models import Brand, Smartphone

admin.site.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ('name', 'country', 'founded_year', 'is_active')
    search_fields = ('name',)

admin.site.register(Smartphone)
class SmartphoneAdmin(admin.ModelAdmin):
    list_display = ('model_name', 'brand', 'os', 'price', 'in_stock')
    list_filter = ('os', 'brand', 'in_stock', 'color')
    search_fields = ('model_name',)
