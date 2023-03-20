import requests
from django.shortcuts import render

def product_search(request):
    query = request.GET.get('query', '')
    url = 'https://fr.openfoodfacts.org/cgi/search.pl'
    params = {
        'action': 'process',
        'json': 1,
        'search_terms': query,
        'page_size': 20,
    }
    response = requests.get(url, params=params)
    data = response.json()
    products = data['products']
    context = {
        'query': query,
        'products': products,
    }
    return render(request, 'product_search.html', context)