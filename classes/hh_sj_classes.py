from abc import ABC, abstractmethod
import requests
from pprint import pprint


class Engine(ABC):
    """Абстрактный класс-родитель для классов HH и SJ"""

    def get_request(self):
        pass


class HeadHunterAPI(Engine):
    """Класс для работы с API сайта headhunter.ru"""
    URL = 'https://api.hh.ru/vacancies'

    def get_request(self, keyword, page, area, per_page=50):
        """
        Отправка запроса на API
        :param keyword: ключевое слово (название вакансии)
        :param page: номер страницы
        :param per_page: количество вакансий на одной странице
        :param area: ID региона из справочника
        :return: json со списком вакансий
        """

        # в параметрах задана сортировка по дате и только с указанной зарплатой по России
        params = {'text': keyword,
                  'page': page,
                  'per_page': per_page,
                  'only_with_salary': True,
                  'order_by': "publication_time",
                  'area': area}

        response = requests.get(self.URL, params=params).json()
        for p in response['items']:
            pprint(p)
        return response['items']

    def get_vacancies(self, keyword: str, count: int, area=113) -> list[dict]:
        """
        Делает запросы, изменяя номер страницы
        :param keyword: ключевое слово (название вакансии)
        :param area: ID региона из справочника
        :param count: количество вакансий для парсинга
        :return: список с вакансиями на соответствующей странице
        """
        if count <= 100:
            pages = 1  # количество страниц с вакансиями
            vacancies = self.get_request(keyword, pages, area)

        else:
            pages = count // 50 + 1
            vacancies = []
            for i in range(pages):
                page = self.get_request(keyword, pages, area)
                vacancies.extend(page)
        return vacancies


if __name__ == '__main__':
    hh = HeadHunterAPI()
    hh.get_vacancies('Инженер-конструктор', 1716)  # 1716 - Владимирская область, 113 - Россия
