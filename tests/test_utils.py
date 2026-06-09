import os
from src.utils import load_categories_from_json


class TestLoadCategories:
    def test_load_real_json_file(self):
        """Тест загрузки реального JSON-файла с продуктами"""

        # Путь к файлу
        file_path = os.path.join("data", "products.json")

        # Загружаем категории
        categories = load_categories_from_json(file_path)

        # Проверяем количество категорий
        assert len(categories) == 2

        # Проверяем первую категорию ("Смартфоны")
        first_category = categories[0]
        assert first_category.name == "Смартфоны"
        assert len(first_category.products) == 3

        # Проверяем первый продукт в первой категории
        first_product = first_category.products[0]
        assert first_product.name == "Samsung Galaxy C23 Ultra"
        assert first_product.price == 180000.0
        assert first_product.quantity == 5

        # Проверяем вторую категорию ("Телевизоры")
        second_category = categories[1]
        assert second_category.name == "Телевизоры"
        assert len(second_category.products) == 1

        # Проверяем продукт во второй категории
        tv_product = second_category.products[0]
        assert tv_product.name == '55" QLED 4K'
        assert tv_product.price == 123000.0
        assert tv_product.quantity == 7
