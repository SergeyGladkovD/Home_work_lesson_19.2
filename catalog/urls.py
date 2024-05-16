from django.urls import path

from catalog.apps import CatalogConfig
from catalog.views import ProductsListView, ProductDetailView

app_name = CatalogConfig.name

urlpatterns = [
	path("", ProductsListView.as_view(), name="base"),
	path("products/<int:pk>/", ProductDetailView.as_view(), name='product_detail')
]
