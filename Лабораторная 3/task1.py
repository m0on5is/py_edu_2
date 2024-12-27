class Book:
    """ Базовый класс книги. """

    def __init__(self, name: str, author: str):
        self._name = name  # Название книги
        self._author = author  # Автор книги

    @property
    def name(self):
        return self._name

    @property
    def author(self):
        return self._author

    def __str__(self):
        return f"Книга {self.name}. Автор {self.author}"

    def __repr__(self):
        return f"{self.__class__.__name__}(Книга={self.name!r}, Автор={self.author!r})"


class PaperBook(Book):
    """ Класс бумажной книги, наследуется от Book. """

    def __init__(self, name: str, author: str, pages: int):
        super().__init__(name, author)
        self._pages = pages  # Количество страниц

    @property
    def pages(self):
        return self._pages

    @pages.setter
    def pages(self, value):    # Проверка
        if not isinstance(value, int):
            raise TypeError("Количество страниц должно быть целым числом.")
        if value <= 0:
            raise ValueError("Количество страниц должно быть положительным.")
        self._pages = value

    def __str__(self):
        return f"Книга {self.name}. Автор {self.author}. Количество страниц: {self.pages}"


class AudioBook(Book):
    """ Класс аудиокниги, наследуется от Book. """

    def __init__(self, name: str, author: str, duration: float):
        super().__init__(name, author)
        self._duration = duration  # Продолжительность аудиокниги в часах

    @property
    def duration(self):
        return self._duration

    @duration.setter
    def duration(self, value):     # Проверка
        if not isinstance(value, float):
            raise TypeError("Время прослушивания должно быть числом с плавающей точкой.")
        if value <= 0:
            raise ValueError("Время прослушивания должно быть положительным числом")
        self._duration = value

    def __str__(self):
        return f"Книга {self.name}. Автор {self.author}. Продолжительность: {self.duration} часов"


if __name__ == "__main__":
    paper_book = PaperBook("Книга1", "Автор1", 200)
    print(paper_book)

    audio_book = AudioBook("Аудиокнига1", "Автор2", 5.5)
    print(audio_book)
    
