from unittest import TestCase

from src.vacancy import Vacancy


class TestVacancy(TestCase):
    def test_initialization(self):
        vacancy = Vacancy("Developer", "http://example.com", {"from": 50000}, "Develop software")
        self.assertEqual(vacancy.name, "Developer")
        self.assertEqual(vacancy.url, "http://example.com")
        self.assertEqual(vacancy.salary, 50000)
        self.assertEqual(vacancy.short_description, "Develop software")

    def test_salary_validation(self):
        vacancy = Vacancy("Developer", "http://example.com", None, "Develop software")
        self.assertEqual(vacancy.salary, 0)

    def test_short_description_validation(self):
        vacancy = Vacancy("Developer", "http://example.com", {"from": 50000}, None)
        self.assertEqual(vacancy.short_description, "Описание отсутствует")

    def test_comparison_operators(self):
        vacancy1 = Vacancy("Developer", "http://example.com", {"from": 50000}, "Develop software")
        vacancy2 = Vacancy("Manager", "http://example.com", {"from": 60000}, "Manage team")
        self.assertTrue(vacancy1 < vacancy2)
        self.assertFalse(vacancy1 > vacancy2)
        self.assertFalse(vacancy1 == vacancy2)
