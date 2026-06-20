from abc import ABC, abstractmethod


class BaseProduct(ABC):
    """Абстрактный класс для всех продуктов"""

    @abstractmethod
    def __str__(self):
        """Строковое представление продукта"""
        pass

    @abstractmethod
    def __add__(self, other):
        """Сложение продуктов"""
        pass

    @property
    @abstractmethod
    def price(self):
        """Геттер для цены"""
        pass

    @price.setter
    @abstractmethod
    def price(self, value):
        """Сеттер для цены"""
        pass


class MixinProductInfo:
    """Миксин для вывода информации о созданном продукте"""

    def __init__(self, name, description, price, quantity, *args, **kwargs):
        print(f"{self.__class__.__name__}('{name}', '{description}', {price}, {quantity})")
        super().__init__(name, description, price, quantity, *args, **kwargs)

    def __repr__(self):
        return f"{self.__class__.__name__}({self.name}, {self.description}, {self.price}, {self.quantity})"


class Product(MixinProductInfo, BaseProduct):
    """Класс для представления продукта"""

    name: str
    description: str
    quantity: int

    def __init__(self, name, description, price, quantity):
        """ "Метод для инициализации экземпляра класса"""

        super().__init__()
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

    @classmethod
    def new_product(cls, product_dict, existing_products=None):
        """
        Создаёт новый продукт из словаря.
        Если продукт с таким именем уже есть в existing_products, обновляет его.
        """
        if existing_products is None:
            existing_products = []

        name = product_dict["name"]
        description = product_dict["description"]
        price = product_dict["price"]
        quantity = product_dict["quantity"]

        # Проверка наличия продукта с таким же именем
        for existing in existing_products:
            if existing.name == name:
                # Обновляем количество и цену
                existing.quantity += quantity
                existing.price = max(existing.price, price)
                return existing

        # Если товара с таким же именем нет, то создаём новый товар
        return cls(name, description, price, quantity)

    @property
    def price(self):
        """Геттер для цены"""
        return self.__price

    @price.setter
    def price(self, new_price):
        """Сеттер для цены с проверкой"""
        # Проверка на отрицательную или нулевую цену
        if new_price <= 0:
            print("Цена не должна быть нулевая или отрицательная")
            return

        # Проверка на понижение цены
        if new_price < self.__price:
            answer = input("Новая цена ниже текущей. Вы уверены? Введите y или n: ")
            if answer == "y":
                self.__price = new_price
            # Если ответ не "y" — ничего не меняем
        else:
            self.__price = new_price

    def __str__(self):
        return f"{self.name}, {self.__price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other):
        """Складывает товары и возвращает их полную стоимость"""
        if type(self) is not type(other):
            raise TypeError("Нельзя складывать товары разных классов")
        return self.__price * self.quantity + other.__price * other.quantity


class Smartphone(Product):
    """Класс для представления смартфонов"""

    def __init__(self, name, description, price, quantity, efficiency, model, memory, color):
        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color


class LawnGrass(Product):
    """Класс для представления газонной травы"""

    def __init__(self, name, description, price, quantity, country, germination_period, color):
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color
