from src.api_parser import HeadHunterAPI
from src.file_worker import JsonFileWorker
from src.vacancy import Vacancy
from src.utils import sort_vacancies


def main():
    # Создание экземпляра класса для работы с API сайтов с вакансиями
    hh_api = HeadHunterAPI()
    json_file_worker = JsonFileWorker()
    input_user = input("Введите команду: ")
    # Получение вакансий с hh.ru в формате JSON
    hh_vacancies = hh_api.get_vacancies(input_user)

    vacancy_objects = []
    for vacancy in hh_vacancies:
        v = Vacancy.from_dict(vacancy)
        vacancy_objects.append(v)

    vacancy_dicts = []
    for vacancy in vacancy_objects:
        vacancy_dicts.append(vacancy.to_dict())

    for v in vacancy_dicts:
        json_file_worker.add_vacancy(v)

    user_n = int(input("Введите количество вакансий: "))
    top_vacancies = sort_vacancies(vacancy_objects)[:user_n]
    for vacancy in top_vacancies:
        print(vacancy)


main()
