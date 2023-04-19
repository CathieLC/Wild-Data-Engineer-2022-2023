from django.contrib import admin

# Register your models here.
from inventaireArticles.models import ArticlesV2, DétailListingClient, MissionArticle


class ArticlesDeLaTable(admin.ModelAdmin):
    class Meta:
        model = ArticlesV2
        verbose_name_plural = "Liste complète des articles"

admin.site.register(ArticlesV2, ArticlesDeLaTable)


# class DetailClient(admin.ModelAdmin):
#     class Meta:
#         model = DétailListingClient
#         verbose_name = "Détail article par client"
#         verbose_name_plural = "Détail articles par client"
#
# admin.site.register(DétailListingClient, DetailClient)

class DetailClient(admin.ModelAdmin):
    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        if obj is not None:
            # Si l'article est en cours de modification, on filtre les pièces par utilisateur
            form.base_fields['articlesClient'].queryset = MissionArticle.objects.filter(utilisateur=obj.utilisateur)
        # else:
        #     # Si l'article est en cours de création, on ne montre pas les pièces
        #     form.base_fields['articlesClient'].queryset = MissionArticle.objects.none()
        return form

    class Meta:
        model = DétailListingClient
        verbose_name = "Détail article par client"
        verbose_name_plural = "Détail articles par client"

admin.site.register(DétailListingClient, DetailClient)