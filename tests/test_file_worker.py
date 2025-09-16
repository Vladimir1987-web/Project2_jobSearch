import unittest
from unittest.mock import mock_open, patch

from src.file_worker import JsonFileWorker


class TestJsonFileWorker(unittest.TestCase):

    @patch("builtins.open", new_callable=mock_open, read_data="[]")
    def test_get_vacancies(self, mock_file):
        worker = JsonFileWorker()
        vacancies = worker.get_vacancies()

        self.assertEqual(vacancies, [])
        mock_file.assert_called_with("data/vacancy.json", "r", encoding="utf-8")
