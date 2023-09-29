from django.conf import settings
from django.core.cache import cache
from .models import Category

CACHE_TIMEOUT = 3600


def get_all_categories():
    """
    Получает все категории и кэширует их при включенном кешировании.
    """
    if settings.CACHE_ENABLED:
        cache_key = 'all_categories_list'
        categories = cache.get(cache_key)

        if not categories:
            categories = list(Category.objects.all())
            cache.set(cache_key, categories, CACHE_TIMEOUT)
    else:
        categories = list(Category.objects.all())

    return categories
