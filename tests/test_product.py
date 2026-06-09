from src.product import Product


class TestProduct:
    """Тесты для класса Product"""

    def test_product_initialization(self):
        """Тест инициализации продукта"""

        name = "Samsung Galaxy S23 Ultra"
        description = "256GB, Серый цвет, 200MP камера"
        price = 180000.0
        quantity = 5

        product = Product(name, description, price, quantity)

        assert product.name == name
        assert product.description == description
        assert product.price == price
        assert product.quantity == quantity
