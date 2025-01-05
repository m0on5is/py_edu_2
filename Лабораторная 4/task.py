from abc import abstractmethod

class Gadgets:  # Базовый класс "Гаджеты"
    def __init__(self, brand: str, model: str, price: float): #  Инициализирует объект с указанными маркой, моделью и ценой
        self.brand = brand
        self.model = model
        self.price = price

    @abstractmethod
    def increase_price(self, percentage: float) -> None:
        pass

    def __str__(self) -> str:  # Возвращает строковое представление объекта в формате «brand model»
        return f"{self.brand} {self.model}"

    def __repr__(self) -> str:  # Возвращает строковое представление объекта класса
        return f"{self.__class__.__name__}('{self.brand}', '{self.model}', {self.price})"


class Smartphone(Gadgets): # Дочерний класс "Смартфон"
    def __init__(self, brand: str, model: str, price: float, os: str): #  Инициализирует объект с указанными брендом, моделью, ценой и операционной системой
        super().__init__(brand, model, price)
        self.os = os

    def increase_price(self, percentage: float) -> None: # Причина перегрузки заключается в возможности изменения реализации метода в дочерних классах, для адаптации его поведения под конкретные требования класса
        """Увеличивает цену смартфона на указанный процент"""
        self.price += self.price * (percentage / 100)

    def make_call(self, number: str) -> None:
        """Совершает звонок на указанный номер"""
        print(f"Вызов {number} с {self.brand} {self.model}")

    def __str__(self) -> str:
        return f"Смартфон: {super().__str__()}"

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}('{self.brand}', '{self.model}', {self.price}, '{self.os}')"


class Laptop(Gadgets):  # Дочерний класс "Ноутбук"
    def __init__(self, brand: str, model: str, price: float, operating_system: str): # Инициализирует объект с указанными брендом, моделью, ценой и операционной системой
        super().__init__(brand, model, price)
        self.operating_system = operating_system

    def increase_price(self, percentage: float) -> None:
        """Увеличивает цену ноутбука на указанный процент"""
        self.price += self.price * (percentage / 100)

    def run_program(self, program: str) -> None:
        """Запуск программы на ноутбуке"""
        print(f"Запуск {program} на {self.brand} {self.model}")

    def __str__(self) -> str:
        return f"Ноутбук: {super().__str__()}"

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}('{self.brand}', '{self.model}', {self.price}, '{self.operating_system}')"
