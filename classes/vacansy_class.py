class Vacansy:
    """Класс для определения вакансии"""

    def __init__(self, title, salary_min, salary_max, link, currency, area, requirement, responsibility, experience):
        self.title = title  # vacancy['name']  Название вакансии
        self.salary_min = salary_min  # vacancy['salary']['from']  минимальная планка вакансии
        self.salary_max = salary_max  # vacancy['salary']['to']  максимальная планка вакансии
        self.link = link  # vacancy['alternate_url']  ссылка на вакансию
        self.currency = currency   # vacancy['salary']['currency']  валюта
        self.area = area  # vacancy['area']['name']  регион
        self.requirement = requirement  # vacancy['snippet']['requirement']
        self.responsibility = responsibility  # vacancy['snippet']['responsibility']  описание
        self.experience = experience  # vacancy['experience']['name']  # требования к опыту работы

    def __str__(self):
        return f'Вакансия в регионе {self.area}: {self.title}\n' \
               f'Зарплата от {self.salary_min} до {self.salary_max} {self.currency}\n' \
               f'Требования к кандидату: {self.requirement}\n' \
               f'Описание вакансии: {self.responsibility}\n' \
               f'Требования к опыту: {self.experience}\n' \
               f'Ссылка на вакансию: {self.link}'
