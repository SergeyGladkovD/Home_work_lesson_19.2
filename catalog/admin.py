from django.contrib import admin
from catalog.models import Product, Category, Version


@admin.register(Product)
class Product(admin.ModelAdmin):
    list_display = ("id", "name", "price", "category")
    list_filter = ("category",)
    search_fields = ("name", "description")


@admin.register(Category)
class Category(admin.ModelAdmin):
    list_display = ("id", "name")


@admin.register(Version)
class Version(admin.ModelAdmin):
    list_display = (
        "product",
        "num_version",
        "name_version",
        "indicates_current_version",
    )
    list_filter = ("num_version", "name_version")
