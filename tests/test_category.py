import pytest
from src.category import Category
from src.product import Product, Smartphone, LawnGrass


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
        # Проверяем счётчики
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

    def test_add_product(self):
        """Тест добавления продукта в категорию"""
        category = Category("Тестовая категория", "Описание")
        product = Product("Тестовый товар", "Описание", 1000, 5)

        category.add_product(product)

        # Проверяем, что счётчик увеличился
        assert Category.product_count == 1

        # Проверяем, что продукт добавился (через геттер)
        products_str = category.products
        assert "Тестовый товар" in products_str

    def test_products_getter_format(self):
        """Тест формата вывода геттера products"""
        product1 = Product("Ноутбук", "Описание", 50000, 3)
        product2 = Product("Мышь", "Описание", 1000, 10)

        category = Category("Электроника", "Техника", [product1, product2])

        result = category.products

        # Проверяем формат строки
        assert "Ноутбук, 50000 руб. Остаток: 3 шт.\n" in result
        assert "Мышь, 1000 руб. Остаток: 10 шт.\n" in result
        # Проверяем, что есть перенос строки между товарами
        assert "\n" in result

    def test_category_str(self):
        product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
        product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
        product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)

        category = Category(
            "Смартфоны",
            "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
            [product1, product2, product3],
        )

        str_category = "Смартфоны, количество продуктов: 27 шт."

        assert str(category) == str_category


class TestCategoryAddProduct:
    """Тесты для метода add_product с проверкой типов"""

    def setup_method(self):
        """Обнуляем счётчики перед каждым тестом"""
        Category.category_count = 0
        Category.product_count = 0

    def test_add_product_valid_types(self):
        """Добавление продуктов разных типов — работает"""
        category = Category("Тест", "Описание")

        product = Product("Ноутбук", "Описание", 50000, 5)
        phone = Smartphone(
            "Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5, 95.5, "S23 Ultra", 256, "Серый"
        )
        grass = LawnGrass("Газонная трава", "Элитная трава для газона", 500.0, 20, "Россия", "7 дней", "Зеленый")

        category.add_product(product)
        category.add_product(phone)
        category.add_product(grass)

        # Проверка счётчика
        assert Category.product_count == 3

        # Проверка, что товары добавились через геттер
        products_str = category.products
        assert "Ноутбук" in products_str
        assert "Samsung Galaxy S23 Ultra" in products_str
        assert "Газонная трава" in products_str

    def test_add_product_invalid_type_raises_error(self):
        """Добавление непродукта — ошибка TypeError"""
        category = Category("Тест", "Описание")

        # добавление строки
        with pytest.raises(TypeError, match="Можно добавлять только объекты класса Product или его наследников"):
            category.add_product("не товар")

        # добавление числа
        with pytest.raises(TypeError):
            category.add_product(123)

        # добавление списка
        with pytest.raises(TypeError):
            category.add_product([])

        # добавление словаря
        with pytest.raises(TypeError):
            category.add_product({"name": "товар"})

    def test_add_product_keeps_counters(self):
        """Проверка счётчиков при добавлении"""
        category = Category("Тест", "Описание")
        assert Category.category_count == 1
        assert Category.product_count == 0

        product = Product("Ноутбук", "Описание", 50000, 5)
        category.add_product(product)
        assert Category.product_count == 1

        phone = Smartphone(
            "Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5, 95.5, "S23 Ultra", 256, "Серый"
        )
        category.add_product(phone)
        assert Category.product_count == 2
