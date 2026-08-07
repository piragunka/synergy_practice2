from __future__ import annotations

from datetime import date
from typing import Any


class Worker:
    """Класс для хранения информации о работнике организации."""

    def __init__(
        self,
        full_name: str = "",
        position: str = "",
        salary: float = 0.0,
        start_year: int = 0,
    ) -> None:
        """Конструктор по умолчанию и конструктор с параметрами."""
        self.full_name = full_name
        self.position = position
        self.salary = salary
        self.start_year = start_year

    @classmethod
    def from_name_and_position(
        cls,
        full_name: str,
        position: str,
    ) -> "Worker":
        """Дополнительный конструктор по ФИО и должности."""
        return cls(
            full_name=full_name,
            position=position,
            salary=0.0,
            start_year=date.today().year,
        )

    @classmethod
    def from_dictionary(cls, data: dict[str, Any]) -> "Worker":
        """Дополнительный конструктор из словаря."""
        return cls(
            full_name=str(data.get("full_name", "")),
            position=str(data.get("position", "")),
            salary=float(data.get("salary", 0.0)),
            start_year=int(data.get("start_year", 0)),
        )

    @property
    def full_name(self) -> str:
        return self._full_name

    @full_name.setter
    def full_name(self, value: str) -> None:
        value = value.strip()

        if not value:
            self._full_name = "Не указано"
            return

        self._full_name = value

    @property
    def position(self) -> str:
        return self._position

    @position.setter
    def position(self, value: str) -> None:
        value = value.strip()
        self._position = value if value else "Не указана"

    @property
    def salary(self) -> float:
        return self._salary

    @salary.setter
    def salary(self, value: float) -> None:
        numeric_value = float(value)

        if numeric_value < 0:
            raise ValueError("Заработная плата не может быть отрицательной.")

        self._salary = numeric_value

    @property
    def start_year(self) -> int:
        return self._start_year

    @start_year.setter
    def start_year(self, value: int) -> None:
        numeric_value = int(value)
        current_year = date.today().year

        if numeric_value == 0:
            self._start_year = current_year
            return

        if numeric_value < 1900 or numeric_value > current_year:
            raise ValueError(
                f"Год поступления должен находиться "
                f"в диапазоне от 1900 до {current_year}."
            )

        self._start_year = numeric_value

    def update(
        self,
        full_name: str | None = None,
        position: str | None = None,
        salary: float | None = None,
        start_year: int | None = None,
    ) -> None:
        """Изменяет выбранные поля работника."""
        if full_name is not None:
            self.full_name = full_name

        if position is not None:
            self.position = position

        if salary is not None:
            self.salary = salary

        if start_year is not None:
            self.start_year = start_year

    def calculate_experience(self, current_year: int | None = None) -> int:
        """Вычисляет стаж работника в полных календарных годах."""
        year = current_year or date.today().year

        if year < self.start_year:
            raise ValueError(
                "Текущий год не может быть меньше года поступления."
            )

        return year - self.start_year

    def get_surname(self) -> str:
        """Возвращает фамилию работника."""
        return self.full_name.split()[0]

    def display(self) -> str:
        """Возвращает информацию о работнике в текстовом виде."""
        return (
            f"Работник: {self.full_name}\n"
            f"Должность: {self.position}\n"
            f"Заработная плата: {self.salary:.2f} руб.\n"
            f"Год поступления: {self.start_year}\n"
            f"Стаж: {self.calculate_experience()} лет"
        )

    def __del__(self) -> None:
        """Деструктор класса."""
        # Python самостоятельно освобождает память.
        # Метод добавлен в соответствии с требованиями задания.
        pass
