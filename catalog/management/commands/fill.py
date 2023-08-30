from django.core.management import BaseCommand

from catalog.models import Category, Product


class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        """
        Удаляет данные из базы данных и заполняет их
        """
        Category.objects.all().delete()
        Product.objects.all().delete()

        category_data = [
            {'name': 'Видеокарты', 'description': 'Различные видеокарты для ПК'},
            {'name': 'Процессоры', 'description': 'Различные процессоры для ПК'},
            {'name': 'Блоки питания', 'description': 'Различные блоки питания для ПК'},
            {'name': 'Материнские платы', 'description': 'Различные материнские платы для ПК'}
        ]

        product_data = [
            {'name': 'RTX4070', 'category': 'Видеокарты', 'price': '70000'},
            {'name': 'i9-12900F', 'category': 'Процессоры', 'price': '38000'},
            {'name': 'DEEPCOOL PQ850M', 'category': 'Блоки питания', 'price': '12500'},
            {'name': 'GIGABYTE B550', 'category': 'Материнские платы', 'price': '13500'},
        ]

        category_to_create = []

        for category in category_data:
            category_to_create.append(
                Category(**category)
            )
        Category.objects.bulk_create(category_to_create)

        products_to_create = []

        for product in product_data:
            products_to_create.append(
                Product(**product)
            )

        Product.objects.bulk_create(products_to_create)
