from django.contrib import admin

# Register your models here.
from inventaire.models import Inventaire_items, Piece, Mission, Contenu

admin.site.register(Inventaire_items)
admin.site.register(Piece)
admin.site.register(Mission)
admin.site.register(Contenu)



