import json


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

    def get_vacancies(self):
        """Получение вакансий из json-файла по определенным критериям"""

    def delete_vacancy(self):
        """Удаление вакансии из json-файла"""


