from src.category import Category
from src.product import Product


class TestCategory:
    """Тесты для класса Category"""

    def setup_method(self):
        """Обнуляем счётчики перед каждым тестом"""
        Category.category_count = 0
        Category.product_count = 0

    def test_category_initialization(self):
        """Тест инициализации категории"""

        product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
        product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
        product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)

        category = Category(
            "Смартфоны",
            "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
            [product1, product2, product3],
        )

        assert category.name == "Смартфоны"
        assert (
            category.description
            == "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций "
            "для удобства жизни"
        )
        assert category.products == [product1, product2, product3]
        assert Category.category_count == 1
        assert Category.product_count == 3

    def test_category_empty(self):
        """Тест проверки на категорию без продуктов"""

        Category(
            "Смартфоны",
            "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
        )
        assert Category.category_count == 1
        assert Category.product_count == 0
