from src.api_parser import HeadHunterAPI


class Vacancy:
    """Класс для работы с вакансиями"""

    __slots__ = ['name', 'url', 'salary', 'short_description']

    def __init__(self, name, url, salary, short_description):
        self.name = name
        self.url = url
        self.salary = self.__validate_salary(salary)  # Сохраняем результат валидации
        self.short_description = self.__validate_short_description(short_description)


    def __validate_salary(self, salary_info) -> int:
        if not salary_info:
            return 0
        if salary_info.get("from"):
            return int(salary_info["from"])
        return salary_info.get("to", 0)

    def __validate_short_description(self, description_info):
        return description_info if description_info else "Описание отсутствует"


    def __lt__(self, other):
        return self.salary < other.salary

    def __gt__(self, other):
        return self.salary > other.salary

    def __eq__(self, other):
        return self.name == self.other and self.salary == other.salary and self.url == other.url

    @classmethod
    def from_dict(cls, vacancy_dict):
        return cls(
            name=vacancy_dict.get("name", ""),
            url=vacancy_dict.get("url", ""),
            salary=vacancy_dict.get("salary"),
            short_description=vacancy_dict.get("snippet", {}).get("responsibility", ""),
        )


    def to_dict(self):
        return {
            'name': self.name,
            'url': self.url,
            'salary': self.salary,
            'short_description': self.short_description
        }

    def __str__(self):
        return (f"name: {self.name}, url: {self.url}, salary: {self.salary},"
                f"short_description: {self.short_description}")
