import json
import os
from abc import ABC, abstractmethod


class FileWorker(ABC):
    """
    Абстрактный класс, который обязывает реализовать методы для добавления вакансий в файл,
    получения данных из файла по указанным критериям и удаления информации о вакансиях.
    """

    @abstractmethod
    def add_vacancy(self, vacancy):
        pass

    @abstractmethod
    def get_vacancies(self):
        pass

    @abstractmethod
    def delete_vacancy(self, vacancy):
        pass


class JsonFileWorker(FileWorker):
    """
    Класс для сохранения информации о вакансиях в JSON-файл.
    :param vacancy:
    :return:
    """

    def __init__(self, file_name="vacancies.json"):
        self.__file_name = "data/vacancy.json"

        if not os.path.exists(self.__file_name):
            with open(self.__file_name, "w", encoding="utf-8") as file:
                json.dump([], file)

    def add_vacancy(self, vacancy):
        """Функция записи вакансий в json-файл"""
        with open(self.__file_name, "r", encoding="utf-8") as file:
            vacancies = json.load(file)
        if vacancy not in vacancies:
            vacancies.append(vacancy)
        with open(self.__file_name, "w", encoding="utf-8") as file:
            json.dump(vacancies, file, indent=4, ensure_ascii=False)

    def get_vacancies(self):
        """Функция чтения вакансий из json-файла"""
        with open(self.__file_name, "r", encoding="utf-8") as file:
            vacancies = json.load(file)
        return vacancies

    def delete_vacancy(self, vacancy):
        """Функция удаления вакансий в json-файле"""
        pass
