from abc import ABC, abstractmethod
import requests


# Абстрактный класс Parser
class Parser(ABC):
    @abstractmethod
    def _API_connections(self, *args, **kwargs):
        """ Метод для отправки API-запроса."""
        pass

    @abstractmethod
    def get_vacancies(self, *args, **kwargs):
        """Метод для получения вакансий"""
        pass

class HeadHunterAPI(Parser):
    """
    Класс для работы с API HeadHunter
    Класс Parser является родительским классом
    """

    def __init__(self):
        self.emp = None
        self.__url = 'https://api.hh.ru/vacancies'
        self.__headers = {'User-Agent': 'HH-User-Agent'}
        self.__params = {'text': '', 'page': 0, 'per_page': 100}
        #self.__vacancies = []
        #super().__init__(file_worker)

    def _API_connections(self):
        """ Метод подключения к API """
        return requests.get(self.__url, headers=self.__headers, params=self.__params)


    def get_vacancies(self, keyword: str) -> None:
        """ Метод получения данных """
        self.__params['text'] = keyword # Устанавливаем ключевое слово
        self.__params['per_page'] = 100  # Устанавливаем количество элементов на страницу
        while self.__params.get('page') != 20:
            response = self._API_connections() # Вызов метода подключения

            if response.status_code == 200:
                # Если ответ успешный, обрабатываем данные
                vacancies = response.json()['items']
                #self.__vacancies.extend(vacancies)
                self.__params['page'] += 1
            else:
                # Если ответ не успешный, выводим сообщение об ошибке и прекращаем цикл
                print(f"Ошибка: статус-код {response.status_code}")
                break
        return vacancies


hh_api = HeadHunterAPI()
hh_vacancies = hh_api.get_vacancies("Python Developer")
print(hh_vacancies)
