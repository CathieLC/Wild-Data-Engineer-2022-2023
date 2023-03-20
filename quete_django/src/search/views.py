from django.contrib.sites import requests
from django.shortcuts import HttpResponse


from django.shortcuts import render


# Create your views here.

def firstView(request):
    return HttpResponse("Hey ! tu es sur l'index de l'application search du projet NutriFood.")



# def product_search(request):
#     query = request.GET.get('query', '')
#     url = 'https://fr.openfoodfacts.org/cgi/search.pl'
#     params = {
#         'action': 'process',
#         'json': 1,
#         'search_terms': query,
#         'page_size': 20,
#     }
#     response = requests.get(url, params=params)
#     data = response.json()
#     products = data['products']
#     context = {
#         'query': query,
#         'products': products,
#     }
#     return render(request, 'product_search.html', context)


def ma_vue(request):
    code_barres = '737628064502' # Remplacez par le code-barres de votre produit
    url = f'https://world.openfoodfacts.org/api/v0/product/{code_barres}.json'
    reponse = requests.get(url)
    if reponse.ok:
        produit = reponse.json()
        return render(request, 'product_search.html', context={"produit": produit}) # Utilisez les informations du produit ici
    else:
        return HttpResponse("Ce code-barres n'existe pas dans notre base de données OFF.")