from src.api_parser import HeadHunterAPI


class Vacancy:
    """Класс для работы с вакансиями"""

    name: str
    url: str
    salary: int
    short_description = str

    def __init__(self, name, url, salary, short_description):
        self.name = name
        self.url = url
        self.validate_salary(salary)
        self.short_description = short_description
        self.__vacancies = []


    def validate_salary(self, salary_info):
        if salary_info:
            return 0
        if salary_info['from']:
            return salary_info['from']
        else:
            return salary_info['to']


    def validate_description(self, description_info):
        if description_info:
            return description_info


    def __lt__(self, other):
        return self.salary < other.salary


    def cast_to_object_list(self, hh_vacancy):
        """Преобразование набора данных из JSON в список объектов"""
        hh_api = HeadHunterAPI()
        hh_vacancy = hh_api.get_vacancies()
        return self.__vacancies.extend(hh_vacancy)
