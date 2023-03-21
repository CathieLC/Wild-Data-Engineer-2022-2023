from django.contrib.sites import requests as req
from django.shortcuts import HttpResponse
from django.shortcuts import render
from .forms import ProductSearchForm, ProductReplacementForm


# Create your views here.
from requests import get


def firstView(request):
    return HttpResponse("Hey ! tu es sur l'index de l'application search du projet NutriFood.")


def product_detail(request, barcode):
    url = f"https://world.openfoodfacts.org/api/v0/product/{barcode}.json"
    response = get(url)

    if response.status_code == 200:
        product = response.json().get("product")
        context = {"product": product}
        return render(request, "search/product_detail.html", context)
    else:
        context = {"error": f"Le produit avec le code-barres {barcode} n'a pas été trouvé."}
        return render(request, "search/product_detail.html", context)



def product_search(request):
    search_form = ProductSearchForm()
    replacement_form = None

    if request.method == 'POST':
        search_form = ProductSearchForm(request.POST)

        if search_form.is_valid():
            code_barre = search_form.cleaned_data['code_barre']
            response = requests.get(f"https://world.openfoodfacts.org/api/v0/product/{code_barre}.json")

            if response.status_code == 200:
                product = response.json()

                if product['status'] == 1:
                    nutriscore_grade = product['product']['nutriscore_grade']

                    if nutriscore_grade in ['a', 'b', 'c']:
                        replacement_form = ProductReplacementForm()
                        context = {'search_form': search_form, 'product': product, 'replacement_form': replacement_form}
                        return render(request, 'product_search.html', context)

    context = {'search_form': search_form, 'replacement_form': replacement_form}
    return render(request, 'product_search.html', context)

def product_replacement(request):
    search_form = ProductSearchForm()
    replacement_form = ProductReplacementForm()

    if request.method == 'POST':
        replacement_form = ProductReplacementForm(request.POST, request.FILES)

        if replacement_form.is_valid():
            # enregistrer le produit de remplacement dans la base de données ou l'envoyer à un administrateur pour examen
            return render(request, 'product_replacement_confirmation.html')

    context = {'search_form': search_form, 'replacement_form': replacement_form}
    return render(request, 'product_replacement_confirmation.html', context)
