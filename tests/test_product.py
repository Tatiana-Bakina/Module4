from src.product import Product


class TestProduct:
    def test_product_initialization(self):
        """Тест инициализации продукта с реальными данными"""
        product = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
        assert product.name == "Samsung Galaxy S23 Ultra"
        assert product.description == "256GB, Серый цвет, 200MP камера"
        assert product.price == 180000.0
        assert product.quantity == 5

    def test_price_getter(self):
        """Тест геттера цены"""
        product = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
        assert product.price == 210000.0

    def test_price_setter_positive(self):
        """Тест установки положительной цены"""
        product = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)
        product.price = 35000.0
        assert product.price == 35000.0

    def test_price_setter_zero(self, capsys):
        """Тест установки цены 0"""
        product = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
        product.price = 0
        captured = capsys.readouterr()
        assert "Цена не должна быть нулевая или отрицательная" in captured.out
        assert product.price == 180000.0

    def test_price_setter_negative(self, capsys):
        """Тест установки отрицательной цены"""
        product = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
        product.price = -10000
        captured = capsys.readouterr()
        assert "Цена не должна быть нулевая или отрицательная" in captured.out
        assert product.price == 210000.0


class TestProductClassMethod:
    def setup_method(self):
        """Создаём список имеющихся товаров перед каждым тестом"""
        self.existing_products = [
            Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5),
            Product("Iphone 15", "512GB, Gray space", 210000.0, 8),
            Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14),
        ]

    def test_new_product_creates_new(self):
        """Тест: товара нет в списке — создаётся новый"""
        new_data = {"name": '55" QLED 4K', "description": "Фоновая подсветка", "price": 123000.0, "quantity": 7}
        result = Product.new_product(new_data, self.existing_products)
        assert result.name == '55" QLED 4K'
        assert result.price == 123000.0
        assert result.quantity == 7

    def test_new_product_updates_existing_higher_price(self):
        """Тест: товар есть, новая цена выше — обновляем цену и складываем количество"""
        new_data = {
            "name": "Samsung Galaxy S23 Ultra",
            "description": "256GB, Серый цвет, 200MP камера",
            "price": 190000.0,  # выше, чем 180000
            "quantity": 3,
        }
        result = Product.new_product(new_data, self.existing_products)
        assert result.name == "Samsung Galaxy S23 Ultra"
        assert result.quantity == 8  # 5 + 3
        assert result.price == 190000.0  # взяли максимальную

    def test_new_product_updates_existing_lower_price(self):
        """Тест: товар есть, новая цена ниже — цену не меняем, количество складываем"""
        new_data = {
            "name": "Iphone 15",
            "description": "512GB, Gray space",
            "price": 200000.0,  # ниже, чем 210000
            "quantity": 2,
        }
        result = Product.new_product(new_data, self.existing_products)
        assert result.name == "Iphone 15"
        assert result.quantity == 10  # 8 + 2
        assert result.price == 210000.0  # осталась максимальная

    def test_new_product_with_empty_list(self):
        """Тест: список существующих товаров пуст"""
        new_data = {
            "name": "Samsung Galaxy S23 Ultra",
            "description": "256GB, Серый цвет, 200MP камера",
            "price": 180000.0,
            "quantity": 5,
        }
        result = Product.new_product(new_data, [])
        assert result.name == "Samsung Galaxy S23 Ultra"

    def test_price_setter_decrease_with_confirmation(self, monkeypatch):
        """Тест: понижение цены с подтверждением y"""
        product = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)

        # Мокаем input, чтобы он возвращал "y"
        monkeypatch.setattr("builtins.input", lambda _: "y")

        product.price = 150000.0
        assert product.price == 150000.0

    def test_new_product_without_existing_products(self):
        """Тест: вызов new_product без передачи списка existing_products"""
        new_data = {"name": '55" QLED 4K', "description": "Фоновая подсветка", "price": 123000.0, "quantity": 7}
        # Не передаём second argument (existing_products)
        result = Product.new_product(new_data)

        assert result.name == '55" QLED 4K'
        assert result.quantity == 7

    def test_product_str(self):
        """Проверка предоставления продукта в строковом виде"""
        product = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
        str_product = "Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток: 5 шт."
        assert str(product) == str_product

    def test_product_add(self):
        "Проверка сложения суммы товаров"

        product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
        product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)

        result = product1 + product2

        assert result == 180000.0 * 5 + 210000.0 * 8
