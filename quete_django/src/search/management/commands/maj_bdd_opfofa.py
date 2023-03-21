from django.core.management.base import BaseCommand
import requests
import json

class Command(BaseCommand):
    help = 'Get products by category from openfoodfacts.org'

    def add_arguments(self, parser):
        parser.add_argument('categories', nargs='+', type=str)
        parser.add_argument('--max-products-per-category', type=int, default=100)

    def handle(self, *args, **options):
        categories = options['categories']
        max_products_per_category = options['max_products_per_category']

        products_by_category = []
        for category in categories:
            url = f"https://world.openfoodfacts.org/category/{category}/{max_products_per_category}.json"
            response = requests.get(url)
            data = json.loads(response.text)
            products_by_category.append(data["products"])

            for product in products_by_category:
                self.stdout.write(self.style.SUCCESS('Category: %s' % category))
                self.stdout.write(self.style.SUCCESS('Product: %s' % product))