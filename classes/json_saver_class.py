import json

from classes.vacansy_class import Vacancy


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

    def add_vacancies(self, hh_vacancies: list | None = None, sj_vacancies: list | None = None) -> None:
        """Записывает список с вакансиями в json файлы (вакансии hh в один файл, sj в другой файл)"""

        with open(f'hh_{self.__filename}', 'w', encoding='UTF-8') as hh_file, \
                open(f'sj_{self.__filename}', 'w', encoding='UTF-8') as sj_file:

            json.dump(hh_vacancies, hh_file, indent=4, ensure_ascii=False)
            json.dump(sj_vacancies, sj_file, indent=4, ensure_ascii=False)

        self.select()

    def select(self):
        """Функция для чтения json файла с вакансиями и создания из него списка с экземплярами класса Vacancy"""
        with open(f'hh_{self.__filename}', 'r', encoding='UTF-8') as hh_file, \
                open(f'sj_{self.__filename}', 'r', encoding='UTF-8') as sj_file:
            hh_data = json.load(hh_file)
            sj_data = json.load(sj_file)

            vacancies = []
            if hh_data:
                for vacancy in hh_data:
                    salary_min = vacancy['salary']['from'] if vacancy['salary']['from'] else vacancy['salary']['to']
                    salary_max = vacancy['salary']['to'] if vacancy['salary']['to'] else salary_min
                    requirement = vacancy['snippet']['requirement'] if vacancy['snippet']['requirement'] \
                        else 'Нет требований'
                    responsibility = vacancy['snippet']['responsibility'] if vacancy['snippet']['responsibility'] \
                        else 'Нет описания'

                    vacancies.append(Vacancy(vacancy['name'],
                                             salary_min,
                                             salary_max,
                                             vacancy['alternate_url'],
                                             vacancy['salary']['currency'],
                                             vacancy['area']['name'],
                                             requirement,
                                             responsibility,
                                             vacancy['experience']['name']))

            if sj_data:
                for vacancy in sj_data:
                    responsibility = vacancy['work'] if vacancy['work'] else 'Нет описания'
                    requirement = vacancy['candidat'] if vacancy['candidat'] else 'Нет требований'
                    vacancies.append(Vacancy(vacancy['profession'],
                                             vacancy['payment_from'],
                                             vacancy['payment_to'],
                                             vacancy['link'],
                                             vacancy['currency'],
                                             vacancy['town']['title'],
                                             requirement,
                                             responsibility,
                                             vacancy['experience']['title']))

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
            filtered_vacancies = filter(lambda x: int(user_min) <= x, self.vacancies)

        return filtered_vacancies

    def get_vacancies_without_experience(self) -> filter:
        """Вывод вакансий без опыта или с опытом от 1 года"""

        filtered_vacancies = filter(lambda x: x.experience == 'Нет опыта' or '1' in x.experience, self.vacancies)

        return filtered_vacancies
