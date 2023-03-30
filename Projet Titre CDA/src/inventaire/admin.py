from django.contrib import admin

# Register your models here.
from inventaire.models import Inventaire_items, Customers, Piece

admin.site.register(Inventaire_items)
admin.site.register(Customers)
admin.site.register(Piece)



