from django.urls import path

from catalog.apps import CatalogConfig
from catalog.views import (
    ProductsListView,
    ProductDetailView,
    ProductCreateView,
    ProductUpdateView,
    ProductDeleteView,
)

app_name = CatalogConfig.name

urlpatterns = [
    path("", ProductsListView.as_view(), name="product_list"),
    path("products/<int:pk>/", ProductDetailView.as_view(), name="product_detail"),
    path("create/", ProductCreateView.as_view(), name="create"),
    path("edit/<int:pk>", ProductUpdateView.as_view(), name="edit"),
    path("delete/<int:pk>", ProductDeleteView.as_view(), name="delete"),
]
