class Vacansy:
    """Класс для определения вакансии"""

    def __init__(self, title, salary_min, salary_max, employer, link, currency, area, responsibility):
        self.title = title  # vacancy['name']  Название вакансии
        self.salary_min = salary_min  # vacancy['salary']['from']  минимальная планка вакансии
        self.salary_max = salary_max  # vacancy['salary']['to']  максимальная планка вакансии
        self.employer = employer  # vacancy['employer']['name']  работодатель
        self.link = link  # vacancy['alternate_url']  ссылка на вакансию
        self.currency = currency   # vacancy['salary']['currency']  валюта
        self.area = area  # vacancy['area']['name']  регион
        self.responsibility = responsibility  # vacancy['snippet']['responsibility']  описание
