from django.contrib.sites import requests as req
from django.shortcuts import HttpResponse
from django.shortcuts import render


# Create your views here.

def firstView(request):
    return HttpResponse("Hey ! tu es sur l'index de l'application search du projet NutriFood.")


def product_detail(request, barcode):
    url = f"https://world.openfoodfacts.org/api/v0/product/{barcode}.json"
    response = req.get(url)

    if response.status_code == 200:
        product = response.json().get("product")
        context = {"product": product}
        return render(request, "product_detail.html", context)
    else:
        context = {"error": f"Le produit avec le code-barres {barcode} n'a pas été trouvé."}
        return render(request, "product_detail.html", context)