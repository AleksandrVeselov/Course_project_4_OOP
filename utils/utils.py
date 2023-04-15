from classes.vacansy_class import Vacancy


def sort_vacancies(vacancies: list[Vacancy]) -> list[Vacancy]:
    """
    Функция для сортировки списка вакансий по зарплате
    :param vacancies: список с экземплярами класса Vacancy
    :return: отсортированный по минимальной зарплате список с экземплярами класса Vacancy
    """
    sorted_vacancies = sorted(vacancies)
    return sorted_vacancies


def filter_vacancies(filter_word: None, hh_vac: None | list[Vacancy] = None, sj_vac=None) -> list[Vacancy]:
    """
    Поиск вакансий по ключевому слову. Ключевое слово ищется в описании вакансии, или в требованиях к вакансии
    :param filter_word:
    :param hh_vac:
    :param sj_vac:
    :return:
    """
    filtered_vac = []
    if hh_vac:
        for vacancy in hh_vac:
            if filter_word.lower() in vacancy.requirement.lower() or filter_word.lower() in vacancy.responsibility.lower():
                filtered_vac.append(vacancy)
        return filtered_vac


def get_top_vacancies(vacancies: list[Vacancy], top_n: int) -> list[Vacancy]:
    """
    Функция для возврата top_n вакансий с самой большой зарплатой
    :param vacancies: отсортированный по возрастанию з/п список с экземплярами класса Vacancy
    :param top_n: количество вакансий для вывода
    :return: список с top_n экземплярами класса Vacancy с самой большой зарплатой
    """
    return vacancies[-1:-top_n:-1]


def get_vacancies_without_experience(vacancies: list[Vacancy]):
    filtered_vacancies = filter(lambda x: x.experience == 'Нет опыта' or x.experience == 'без опыта'
                                          or '1' in x.experience, vacancies)

    return filtered_vacancies
