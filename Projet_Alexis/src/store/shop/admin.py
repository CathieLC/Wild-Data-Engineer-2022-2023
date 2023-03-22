from django.contrib import admin
from .models import Product, Order, Cart

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)} # slug field will be filled automatically with title field

admin.site.register(Order)
admin.site.register(Cart)