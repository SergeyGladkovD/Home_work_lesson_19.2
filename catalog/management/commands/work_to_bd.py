import json

from django.core.management import BaseCommand
from django.db import connection

from catalog.models import Category, Product


class Command(BaseCommand):

	def handle(self, *args, **options):

		with connection.cursor() as cursor:
			cursor.execute(f"TRUNCATE TABLE catalog_category RESTART IDENTITY CASCADE;")

		Product.objects.all().delete()
		Category.objects.all().delete()

		with open("catalog.json", encoding="utf8") as file:
			data = json.load(file)
			catalog_category = []
			catalog_product = []
			for category in data:
				if category["model"] == "catalog.category":
					catalog_category.append(
						Category(
							name=category["fields"]["name"],
							description=category["fields"]["description"],
						)
					)

			Category.objects.bulk_create(catalog_category)

			for product in data:
				if product["model"] == "catalog.product":
					catalog_product.append(
						Product(
							name=product["fields"]["name"],
							description=product["fields"]["description"],
							category=Category.objects.get(
								pk=product["fields"]["category"]),
							price=product["fields"]["price"],
							),
						)

			Product.objects.bulk_create(catalog_product)
