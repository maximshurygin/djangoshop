from django.core.management import BaseCommand

from catalog.models import Category, Product


class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        """
        Удаляет данные из базы данных и заполняет их
        """

        Product.objects.all().delete()

        product_data = [
            {'name': 'RTX4070', 'category': Category.objects.get(id=4), 'price': 70000},
            {'name': 'i9-12900F', 'category': Category.objects.get(id=5), 'price': 38000},
            {'name': 'DEEPCOOL PQ850M', 'category': Category.objects.get(id=6), 'price': 12500},
            {'name': 'GIGABYTE B550', 'category': Category.objects.get(id=7), 'price': 13500},
        ]

        products_to_create = []

        for product in product_data:
            products_to_create.append(
                Product(**product)
            )

        Product.objects.bulk_create(products_to_create)
