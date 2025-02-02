from task_1 import Car, Table, CoffeeMachine

if __name__ == "__main__":
    # Инстанцирование класса Car
    car = Car("Toyota", "red")
    # Инстанцирование класса Table
    table = Table("дерево", 2.0, 1.5)
    # Инстанцирование класса CoffeeMachine
    coffee_machine = CoffeeMachine("Nespresso", 500)

    try:  # Попытка посигналить клаксоном отрицательное число раз в методе honk_horn
        car.honk_horn(-8)
    except ValueError:
        print('Ошибка: неправильные данные')

    try:  # Попытка установить некорректный размер комнаты в методе is_suitable
        table.is_suitable(-10)
    except ValueError:
        print('Ошибка: неправильные данные')

    try:  # Попытка налить количество чашек кофе, превышающее объём воды в методе brew_coffee
        coffee_machine.brew_coffee("Espresso", 8)
    except ValueError:
        print('Ошибка: неправильные данные')
