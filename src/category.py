from src.product import Product


class Category:
    """Класс для представления категории продуктов"""

    name: str
    description: str

    # Атрибуты класса
    category_count: int = 0
    product_count: int = 0

    def __init__(self, name, description, products=None):
        """Метод для инициализации экземпляра класса"""

        self.name = name
        self.description = description
        self.__products = products if products else []

        # Автоматически обновляем атрибуты класса
        Category.category_count += 1
        Category.product_count += len(self.__products)

    def add_product(self, product):
        """Метод для добавления продукта в список продуктов с проверкой типа"""

        if not isinstance(product, Product):
            raise TypeError("Можно добавлять только объекты класса Product или его наследников")

        self.__products.append(product)
        Category.product_count += 1

    @property
    def products(self):
        """Геттер возвращает строку со всеми продуктами"""
        result = ""
        for product in self.__products:
            result += str(product) + "\n"
        return result

    def __str__(self):
        """Возвращает строковое представление категории"""
        total_quantity = sum(product.quantity for product in self.__products)
        return f"{self.name}, количество продуктов: {total_quantity} шт."

    def middle_price(self):
        """Возвращает среднюю цену товаров в категории с округлением до двух знаков после запятой.
        Если список продуктов пустой, возвращает ноль."""
        try:
            middle_price = sum(product.price for product in self.__products) / len(self.__products)
            return round(middle_price, 2)
        except ZeroDivisionError:
            return 0
