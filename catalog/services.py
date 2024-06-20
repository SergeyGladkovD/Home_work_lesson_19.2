from django.core.cache import cache

from catalog.models import Category
from config.settings import CASH_ENABLED


def get_category_from_cache():
    """Получает данные из кэша или из БД, если кэш пуст."""
    if not CASH_ENABLED:
        return Category.objects.all()
    key = "category_list"
    categories = cache.get(key)
    if categories is not None:
        return categories
    categories = Category.objects.all()
    cache.set(key, categories)
    return categories
