class Category:
    """Класс для представления категории продуктов"""

    name: str
    description: str
    products: list

    # Атрибуты класса
    category_count: int = 0
    product_count: int = 0

    def __init__(self, name, description, products=None):
        """ "Метод для инициализации экземпляра класса"""

        self.name = name
        self.description = description
        self.products = products if products else []

        # Автоматически обновляем атрибуты класса
        Category.category_count += 1
        Category.product_count += len(self.products)
