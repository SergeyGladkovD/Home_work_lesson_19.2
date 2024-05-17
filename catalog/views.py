from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView

from catalog.models import Product


class ProductsListView(ListView):
	model = Product


class ProductDetailView(DetailView):
	model = Product


class ProductCreateView(CreateView):
	model = Product
	fields =('name', 'description', 'photo', 'category', 'price', 'created_at')
	success_url = reverse_lazy('catalog:product_list')


class ProductUpdateView(UpdateView):
	model = Product
	fields = ('name', 'description', 'photo', 'category', 'price', 'created_at')
	success_url = reverse_lazy('catalog:product_list')
