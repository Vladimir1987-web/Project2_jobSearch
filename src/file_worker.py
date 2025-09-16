from abc import ABC, abstractmethod
import json
import os


class FileWorker(ABC):
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
    def __init__(self, file_name="vacancies.json"):
        self.__file_name = "data/vacancy.json"

        if not os.path.exists(self.__file_name):
            with open(self.__file_name, "w", encoding="utf-8") as file:
                json.dump([], file)

    def add_vacancy(self, vacancy):
        with open(self.__file_name, "r", encoding="utf-8") as file:
            vacancies = json.load(file)
        if vacancy not in vacancies:
            vacancies.append(vacancy)
        with open(self.__file_name, "w", encoding="utf-8") as file:
            json.dump(vacancies, file, indent=4, ensure_ascii=False)

    def get_vacancies(self):
        with open(self.__file_name, "r", encoding="utf-8") as file:
            vacancies = json.load(file)
        return vacancies

    def delete_vacancy(self, vacancy):
        pass
