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

        # Проверяем, что товары есть в строковом представлении
        products_str = first_category.products
        assert "Samsung Galaxy C23 Ultra" in products_str
        assert "Iphone 15" in products_str
        assert "Xiaomi Redmi Note 11" in products_str

        # Проверяем вторую категорию ("Телевизоры")
        second_category = categories[1]
        assert second_category.name == "Телевизоры"

        products_str2 = second_category.products
        assert '55" QLED 4K' in products_str2
