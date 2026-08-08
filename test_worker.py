import unittest
from datetime import date

from worker import WORKER


class TestWorker(unittest.TestCase):

    def test_default_constructor(self):
        worker = WORKER()

        self.assertEqual(worker.full_name, "")
        self.assertEqual(worker.position, "")
        self.assertEqual(worker.salary, 0.0)
        self.assertEqual(worker.start_year, 0)

    def test_constructor_with_parameters(self):
        worker = WORKER(
            "Иванов И.И.",
            "Программист",
            100000,
            2020
        )

        self.assertEqual(worker.full_name, "Иванов И.И.")
        self.assertEqual(worker.position, "Программист")
        self.assertEqual(worker.salary, 100000)
        self.assertEqual(worker.start_year, 2020)

    def test_from_name_and_position(self):
        worker = WORKER.from_name_and_position(
            "Петров П.П.",
            "Аналитик"
        )

        self.assertEqual(worker.full_name, "Петров П.П.")
        self.assertEqual(worker.position, "Аналитик")

    def test_from_all_data(self):
        worker = WORKER.from_all_data(
            "Сидоров С.С.",
            "Администратор",
            90000,
            2019
        )

        self.assertEqual(worker.full_name, "Сидоров С.С.")
        self.assertEqual(worker.position, "Администратор")
        self.assertEqual(worker.salary, 90000)
        self.assertEqual(worker.start_year, 2019)

    def test_change_data(self):
        worker = WORKER(
            "Иванов И.И.",
            "Программист",
            100000,
            2020
        )

        worker.change_data(
            "Петров П.П.",
            "Аналитик",
            120000,
            2018
        )

        self.assertEqual(worker.full_name, "Петров П.П.")
        self.assertEqual(worker.position, "Аналитик")
        self.assertEqual(worker.salary, 120000)
        self.assertEqual(worker.start_year, 2018)

    def test_experience(self):
        current_year = date.today().year

        worker = WORKER(
            "Иванов И.И.",
            "Программист",
            100000,
            current_year - 5
        )

        self.assertEqual(worker.get_experience(), 5)


if __name__ == "__main__":
    unittest.main()
