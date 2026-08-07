from worker import Worker

def read_positive_integer(prompt: str) -> int:
    """Считывает целое неотрицательное число."""
    while True:
        try:
            value = int(input(prompt))

            if value < 0:
                print("Введите число, которое не меньше нуля.")
                continue

            return value
        except ValueError:
            print("Ошибка: необходимо ввести целое число.")


def read_salary(prompt: str) -> float:
    """Считывает неотрицательное число с плавающей точкой."""
    while True:
        try:
            value = float(input(prompt).replace(",", "."))

            if value < 0:
                print("Заработная плата не может быть отрицательной.")
                continue

            return value
        except ValueError:
            print("Ошибка: введите корректное числовое значение.")


def create_worker(number: int) -> Worker:
    """Создаёт работника на основе данных пользователя."""
    print(f"\nВвод данных работника № {number}")

    while True:
        try:
            full_name = input("Фамилия и инициалы: ").strip()
            position = input("Должность: ").strip()
            salary = read_salary("Заработная плата: ")
            start_year = read_positive_integer("Год поступления на работу: ")

            return Worker(
                full_name=full_name,
                position=position,
                salary=salary,
                start_year=start_year,
            )
        except ValueError as error:
            print(f"Ошибка: {error}")
            print("Повторите ввод данных работника.")


def find_workers_by_experience(
    workers: list[Worker],
    minimum_experience: int,
) -> list[Worker]:
    """Возвращает работников со стажем больше заданного."""
    return [
        worker
        for worker in workers
        if worker.calculate_experience() > minimum_experience
    ]


def main() -> None:
    print("Программа учёта работников организации")

    workers_count = read_positive_integer(
        "Введите количество работников: "
    )

    workers: list[Worker] = []

    for number in range(1, workers_count + 1):
        workers.append(create_worker(number))

    minimum_experience = read_positive_integer(
        "\nВведите минимальный стаж в годах: "
    )

    selected_workers = find_workers_by_experience(
        workers,
        minimum_experience,
    )

    if not selected_workers:
        print(
            "\nРаботников, стаж которых превышает "
            f"{minimum_experience} лет, не найдено."
        )
        return

    print(
        "\nРаботники, стаж которых превышает "
        f"{minimum_experience} лет:"
    )

    for worker in selected_workers:
        print(f"- {worker.get_surname()}")


if __name__ == "__main__":
    main()
