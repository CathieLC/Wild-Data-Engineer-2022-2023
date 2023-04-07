from django.contrib import admin

# Register your models here.
from inventaire.models import Articles, Piece, CommandeClient, DétailListingClient

admin.site.register(Articles)
admin.site.register(Piece)
admin.site.register(CommandeClient)
admin.site.register(DétailListingClient)




