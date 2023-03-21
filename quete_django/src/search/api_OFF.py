import requests

def get_product_details(barcode):
    url = f'https://world.openfoodfacts.org/api/v0/product/{barcode}.json'
    response = requests.get(url)
    if response.status_code == 200:
        product = response.json()['product']
        return product
    else:
        return None