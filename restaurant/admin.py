from django.contrib import admin
from restaurant.models import Product, Order, Cart

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'with_beef', 'with_chicken', 'vegetarian', 'ingredients')
    search_fields = ['name']

admin.site.register(Product, ProductAdmin)
admin.site.register(Order)
admin.site.register(Cart)