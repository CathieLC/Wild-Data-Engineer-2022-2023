from django.contrib import admin

# Register your models here.
from inventaire.models import Articles, Piece, Mission, Panier

admin.site.register(Articles)
admin.site.register(Piece)
admin.site.register(Mission)
admin.site.register(Panier)




