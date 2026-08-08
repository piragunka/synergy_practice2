from worker import WORKER


workers = []

count = int(input("Введите количество работников: "))

for i in range(count):
    print("\nРаботник №", i + 1)

    full_name = input("Фамилия и инициалы: ")
    position = input("Название должности: ")
    salary = float(input("Зарплата: "))
    start_year = int(input("Год поступления на работу: "))

    worker = WORKER.from_all_data(
        full_name,
        position,
        salary,
        start_year
    )

    workers.append(worker)


experience = int(
    input("\nВведите требуемый стаж работы: ")
)

found = False

print(
    "\nРаботники, стаж которых превышает",
    experience,
    "лет:"
)

for worker in workers:
    if worker.get_experience() > experience:
        surname = worker.full_name.split()[0]
        print(surname)
        found = True


if not found:
    print("Таких работников нет.")
