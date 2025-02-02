class Car:
    """
    Класс для описания автомобиля
    """
    def __init__(self, brand: str, color: str):
        """
            Инициализация объекта автомобиля.
            :param brand: Марка автомобиля (например, "Toyota", "Volkswagen", "Nissan").
            :param color: Цвет автомобиля.
        """
        self.brand = brand
        self.color = color


    def start_engine(self) -> str:
        """
        Запуск двигателя автомобиля.

        :return: Сообщение о запуске двигателя.

        Пример:
        >>> my_car = Car("Toyota", "red")
        >>> my_car.start_engine()
        'Двигатель запущен!'
        """
        return "Двигатель запущен!"

    def change_color(self, new_color: str = "black") -> None:
        """
        Выбор нового цвета автомобиля.

        :param new_color: Новый цвет, который будет установлен для автомобиля. По умолчанию «черный».

        Пример:
        >>> my_car = Car("Toyota", "red")
        >>> my_car.change_color("blue")
        """
        self.color = new_color

    def honk_horn(self, times: int) -> str:
        """
        Сигнал автомобильным клаксоном определенное количество раз.

        :param times: Количество сигналов клаксоном.

        :return: Сообщение о том, что был подан звуковой сигнал.

        Пример:
        >>> my_car = Car("Toyota", "red")
        >>> my_car.honk_horn(2)
        'Honk honk!'
        """
        if times <= 0:
            raise ValueError("Количество сигналов должно быть больше 0.")
        return "Honk honk!"



class CoffeeMachine:
    """
        Класс для описания кофемашины
    """
    def __init__(self, brand: str, water_level: int):
        """
            Инициализация объекта кофемашины.
            :param brand: Марка кофемашины.
            :param water_level: Уровень воды в кофемашине.
        """
        if water_level <= 0:
            raise ValueError("Объем воды должен быть больше 0.")
        self.brand = brand
        self.water_level = water_level

    def brew_coffee(self, coffee_type: str, cups: int) -> str:
        """
        Заваривание кофе определенного типа и в определенном количестве.


        :param coffee_type: Тип кофе для заваривания.
        :param cups: Количество заваренных чашек.

        :return: Сообщение о том, что кофе уже сварен.

        Пример:
        >>> my_coffee_machine = CoffeeMachine("Nespresso", 500)
        >>> my_coffee_machine.brew_coffee("Espresso", 2)
        'Brewing 2 cups of Espresso coffee...'
        """
        if self.water_level < cups * 100:
            raise ValueError("Недостаточно воды для приготовления такого количества чашек кофе.")
        self.water_level -= cups * 100
        return f"Brewing {cups} cups of {coffee_type} coffee..."

    def refill_water(self, amount: int) -> None:
        """
        Заполняет резервуар для воды в кофемашине.

        :param amount: Количество доливаемой воды в миллилитрах.

        Пример:
        >>> my_coffee_machine = CoffeeMachine("Nespresso", 500)
        >>> my_coffee_machine.refill_water(300)
        """
        if amount <= 0:
            raise ValueError("Количество доливаемой воды должно быть больше 0.")
        self.water_level += amount



class Table:
    """
    Класс для описания стола.
    """

    def __init__(self, material: str, length: float, width: float):
        """
        Инициализация объекта стола.
        :param material: Материал стола (например, "дерево", "металл", "пластик").
        :param length: Длина стола в метрах. Должна быть больше 0.
        :param width: Ширина стола в метрах. Должна быть больше 0.
        :raises ValueError: Если длина или ширина не удовлетворяют условиям.
        """
        if length <= 0 or width <= 0:
            raise ValueError("Длина и ширина должны быть больше 0.")
        self.material = material
        self.length = length
        self.width = width

    def calculate_area(self) -> float:
        """
        Рассчитывает площадь стола.
        :return: Площадь стола в квадратных метрах.
        Пример:
        >>> table = Table("дерево", 2.0, 1.0)
        >>> table.calculate_area()
        2.0
        """
        return self.length * self.width

    def change_material(self, new_material: str) -> None:
        """
        Изменяет материал стола.
        :param new_material: Новый материал стола.
        Пример:
        >>> table = Table("дерево", 2.0, 1.0)
        >>> table.change_material("металл")
        >>> table.material
        'металл'
        """
        self.material = new_material

    def is_suitable(self, room_area: float) -> bool:
        """
        Проверяет, подходит ли стол для комнаты с указанной площадью.
        :param room_area: Площадь комнаты в квадратных метрах.
        :return: True, если площадь комнаты больше площади стола, иначе False.
        :raises ValueError: Если площадь комнаты <= 0.
        Пример:
        >>> table = Table("дерево", 2.0, 1.0)
        >>> table.is_suitable(5.0)
        True
        """
        if room_area <= 0:
            raise ValueError("Площадь комнаты должна быть больше 0.")
        return room_area > self.calculate_area()
