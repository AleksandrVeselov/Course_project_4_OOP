from classes import hh_sj_classes
from classes.json_saver_class import JSONSaver
from utils.utils import *


def main():
    print("Курсовой проект по теме объектно-ориентированное программирование: Парсинг вакансий\n"
          "======================= Нажмите Enter чтобы начать ================================")
    input()

    # Запрос платформ для поиска
    platforms = input('Введите платформы для поиска вакансий HH - Headhunter, SJ - SuperJob.'
                      'Для поиска вакансий на двух платформах нажмите Enter -> ')

    # начальные значения для платформ
    hh_api = None
    sj_api = None

    if platforms.lower() == 'hh':
        hh_api = hh_sj_classes.HeadHunterAPI()

    elif platforms.lower() == 'sj':
        sj_api = hh_sj_classes.SuperJobAPI()

    else:
        hh_api = hh_sj_classes.HeadHunterAPI()
        sj_api = hh_sj_classes.SuperJobAPI()

    keyword = input('Введите поисковый запрос -> ')
    count = int(input('Введите количество вакансий для парсинга (кратное 100) -> '))

    if hh_api and not sj_api:
        hh_vacancies = hh_api.get_vacancies(keyword, count)
        sj_vacancies = None
        if hh_vacancies:
            print(f'Парсинг прошел успешно. Найдено {len(hh_vacancies)} вакансий')

        else:
            print('Нет вакансий, соответствующих заданным критериям')
            exit()

    if sj_api and not hh_api:
        hh_vacancies = None
        sj_vacancies = sj_api.get_vacancies(keyword, count)

    else:
        hh_vacancies = hh_api.get_vacancies(keyword, count)
        sj_vacancies = sj_api.get_vacancies(keyword, count)

    json_saver = JSONSaver(keyword)
    json_saver.add_vacancies(hh_vacancies, sj_vacancies)

    filter_word = input("Введите ключевое слово для фильтрации вакансий: ")
    top_n = int(input("Введите количество вакансий для вывода в топ N: "))
    filtered_vacancies = filter_vacancies(filter_word, json_saver.vacancies)
    # sorted_vacancies = sort_vacancies(filtered_vacancies)
    # top_vacancies = get_top_vacancies(sorted_vacancies, top_n)
    without_experience = get_vacancies_without_experience(filtered_vacancies)
    print(*without_experience, sep='\n+++++++++++\n')


if __name__ == '__main__':
    main()
