from classes import hh_sj_classes
from classes.json_saver_class import JSONSaver
from utils.utils import sort_vacancies, filter_vacancies, get_top_vacancies


def main():
    print("Курсовой проект по теме объектно-ориентированное программирование: Парсинг вакансий\n"
          "======================= Нажмите Enter чтобы начать ================================")
    input()

    # Запрос платформ для поиска
    platforms = input('Введите платформы для поиска вакансий HH - Headhunter, SJ - SuperJob.'
                      'Для поиска вакансий на двух платформах нажмите Enter -> ')

    if platforms.lower() == 'hh':
        hh_api = hh_sj_classes.HeadHunterAPI()

    elif platforms.lower() == 'sj':
        sj_api = hh_sj_classes.SuperJobAPI()

    else:
        hh_api = hh_sj_classes.HeadHunterAPI()
        sj_api = hh_sj_classes.SuperJobAPI()

    keyword = input('Введите поисковый запрос -> ')
    count = int(input('Введите количество вакансий для парсинга (кратное 100) -> '))

    hh_vacancies = hh_api.get_vacancies(keyword, count)
    if hh_vacancies:
        print(f'Парсинг прошел успешно. Найдено {len(hh_vacancies)} вакансий')

    else:
        print('Нет вакансий, соответствующих заданным критериям')
        exit()
    json_saver = JSONSaver(keyword)
    json_saver.add_vacancies(hh_vacancies)
    filter_word = input("Введите ключевое слово для фильтрации вакансий: ")
    top_n = int(input("Введите количество вакансий для вывода в топ N: "))
    filtered_vacancies = filter_vacancies(filter_word, json_saver.vacancies)
    sorted_vacancies = sort_vacancies(filtered_vacancies)
    top_vacancies = get_top_vacancies(sorted_vacancies, top_n)
    print(*top_vacancies, sep='\n+++++++++++\n')


if __name__ == '__main__':
    main()
