import json

from classes.vacansy_class import Vacansy


class JSONSaver:
    """Класс для сохранение данных о вакансиях в json файл, получения вакансий оттуда и удаления"""

    def __init__(self, keyword: str):
        """
        инициализатор класса
        :param keyword: имя для файла
        """
        self.__filename = f'{keyword.title()}.json'  # имя файла
        self.vacancies = None  # список экземпляров класса Vacancy

    @property
    def filename(self):
        return self.__filename

    def add_vacancies(self, vacancies: list) -> None:
        """Записывает список с вакансиями в json файл"""

        with open(self.__filename, 'w', encoding='UTF-8') as file:
            json.dump(vacancies, file, indent=4, ensure_ascii=False)

        self.select()

    def select(self):
        """Функция для чтения json файла с вакансиями и создания из него списка с экземплярами класса Vacancy"""
        with open(self.__filename, 'r', encoding='UTF-8') as file:
            data = json.load(file)

            vacancies = []
            for vacancy in data:
                vacancies.append(Vacansy(vacancy['name'],
                                         vacancy['salary']['from'],
                                         vacancy['salary']['to'],
                                         vacancy['alternate_url'],
                                         vacancy['salary']['currency'],
                                         vacancy['area']['name'],
                                         vacancy['snippet']['requirement'],
                                         vacancy['snippet']['responsibility'],
                                         vacancy['experience']['name']))

            self.vacancies = vacancies  # создание списка с экземплярами класса Vacancy

    def get_vacancies_by_salary(self, salary: str) -> filter:
        """
        Фильтрация вакансий по зарплате
        :param salary: параметры фильтрации в следующем формате: минимальная з/п-максимальная з/п. Можно указать одно
        значение з/п, оно будет считаться минимальным, в фильтр попадут все вакансии с з/п больше либо равной переданной
        :return: отфильтрованный список вакансий
        """
        if '-' in salary:
            user_filter = salary.split('-')
            user_min, user_max = user_filter[0], user_filter[1]
            if not user_min.isdigit() and not user_max.isdigit():
                raise ValueError('Введите корректный фильтр по зарплате')
            filtered_vacancies = filter(lambda x: int(user_min) <= x.salary_min <= int(user_max), self.vacancies)

        else:
            user_min = salary
            if not user_min.isdigit():
                raise ValueError('Введите корректный фильтр по зарплате')
            filtered_vacancies = filter(lambda x: int(user_min) <= x.salary_min, self.vacancies)

        return filtered_vacancies

    def delete_vacancy(self):
        """Удаление вакансии из json-файла"""
