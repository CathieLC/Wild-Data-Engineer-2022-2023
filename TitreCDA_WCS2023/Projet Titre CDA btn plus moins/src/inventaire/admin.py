from django.contrib import admin

# Register your models here.
from inventaire.models import Articles, ArticlesV2, Piece, CommandeClient, DétailListingClient

admin.site.register(Articles)
admin.site.register(ArticlesV2)
admin.site.register(Piece)
admin.site.register(CommandeClient)
admin.site.register(DétailListingClient)




