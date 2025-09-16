class Vacancy:
    """Класс для работы с вакансиями"""

    __slots__ = ["name", "url", "salary", "short_description"]

    def __init__(self, name, url, salary, short_description):
        self.name = name
        self.url = url
        self.salary = self.__validate_salary(salary)  # Сохраняем результат валидации
        self.short_description = self.__validate_short_description(short_description)

    def __validate_salary(self, salary_info) -> int:
        """
        Валидация параметра salary
        :param salary_info:
        :return:
        """
        if not salary_info:
            return 0
        if salary_info.get("from"):
            return int(salary_info["from"])
        return salary_info.get("to", 0)

    def __validate_short_description(self, description_info):
        """
        Валидация параметра short_description
        :param description_info:
        :return:
        """
        return description_info if description_info else "Описание отсутствует"

    def __lt__(self, other):
        """Магический метод сравнения"""
        return self.salary < other.salary

    def __gt__(self, other):
        """Магический метод сравнения"""
        return self.salary > other.salary

    def __eq__(self, other):
        """Магический метод сравнения"""
        return self.name == other.name and self.salary == other.salary and self.url == other.url

    @classmethod
    def from_dict(cls, vacancy_dict):
        """Преобразование ответа API в объекты Vacancy"""
        return cls(
            name=vacancy_dict.get("name", ""),
            url=vacancy_dict.get("url", ""),
            salary=vacancy_dict.get("salary"),
            short_description=vacancy_dict.get("snippet", {}).get("responsibility", ""),
        )

    def to_dict(self):
        """Преобразование объектов Vacancy в словарь"""
        return {"name": self.name, "url": self.url, "salary": self.salary, "short_description": self.short_description}

    def __str__(self):
        """Магический метод строчного вывода вакансии"""
        return (
            f"name: {self.name}, url: {self.url}, salary: {self.salary},"
            f"short_description: {self.short_description}"
        )
