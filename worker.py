from datetime import date


class WORKER:
    """
    Класс для хранения информации о работнике.
    """

    def __init__(
        self,
        full_name="",
        position="",
        salary=0.0,
        start_year=0
    ):
        """
        Конструктор по умолчанию.
        Также позволяет создать объект со всеми параметрами.
        """
        self.full_name = full_name
        self.position = position
        self.salary = salary
        self.start_year = start_year

    @classmethod
    def from_name_and_position(cls, full_name, position):
        """
        Конструктор с фамилией, инициалами и должностью.
        """
        return cls(
            full_name,
            position,
            0.0,
            date.today().year
        )

    @classmethod
    def from_all_data(
        cls,
        full_name,
        position,
        salary,
        start_year
    ):
        """
        Конструктор со всеми параметрами.
        """
        return cls(
            full_name,
            position,
            salary,
            start_year
        )

    def change_data(
        self,
        full_name,
        position,
        salary,
        start_year
    ):
        """
        Изменение данных работника.
        """
        self.full_name = full_name
        self.position = position
        self.salary = salary
        self.start_year = start_year

    def display(self):
        """
        Отображение всех полей работника.
        """
        print("Фамилия и инициалы:", self.full_name)
        print("Должность:", self.position)
        print("Зарплата:", self.salary)
        print("Год поступления на работу:", self.start_year)

    def get_experience(self):
        """
        Возвращает стаж работника.
        """
        return date.today().year - self.start_year

    def __del__(self):
        """
        Деструктор класса.
        """
        pass
