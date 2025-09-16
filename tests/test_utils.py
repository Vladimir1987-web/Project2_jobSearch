from unittest import TestCase

from src.utils import sort_vacancies
from src.vacancy import Vacancy


class TestSortVacancies(TestCase):
    def test_sort_vacancies(self):
        vacancy1 = Vacancy("Developer", "http://example.com/1", {"from": 50000}, "Develop software")
        vacancy2 = Vacancy("Manager", "http://example.com/2", {"from": 60000}, "Manage team")
        vacancy3 = Vacancy("Intern", "http://example.com/3", {"from": 30000}, "Assist team")

        vacancies = [vacancy1, vacancy2, vacancy3]
        sorted_vacancies = sort_vacancies(vacancies)

        # Проверяем, что вакансии отсортированы по убыванию зарплаты
        self.assertEqual(sorted_vacancies, [vacancy2, vacancy1, vacancy3])
