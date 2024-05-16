from django.views.generic import ListView, DetailView

from catalog.models import Product


class ProductsListView(ListView):
	model = Product


class ProductDetailView(DetailView):
	model = Product

# app_name/<model_name>_<action>
# catalog/product_list.html
