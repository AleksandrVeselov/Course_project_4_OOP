from classes import hh_sj_classes
from classes.json_saver_class import JSONSaver
from utils.utils import *


def user_interaction():
    print("Курсовой проект по теме объектно-ориентированное программирование: Парсинг вакансий")
    input('======================= Нажмите Enter чтобы начать ================================\n')

    # Запрос платформ для поиска
    platforms = input('Введите платформы для поиска вакансий HH - Headhunter, SJ - SuperJob.'
                      'Для поиска вакансий на двух платформах нажмите Enter -> ')

    # начальные значения для платформ
    hh_api = None
    sj_api = None

    # Если пользователь ввел hh или HH, создается экземпляр класса HeadHunterAPI()
    if platforms.lower() == 'hh':
        hh_api = hh_sj_classes.HeadHunterAPI()

    # Если пользователь ввел sj или SJ, создается экземпляр класса SuperJobAPI()
    elif platforms.lower() == 'sj':
        sj_api = hh_sj_classes.SuperJobAPI()

    # Во всех остальных случаях создается два экземпляра класса: HeadHunterAPI() и SuperJobAPI()
    else:
        hh_api = hh_sj_classes.HeadHunterAPI()
        sj_api = hh_sj_classes.SuperJobAPI()

    # запрос у пользователя ключевого слова для поиска по вакансиям
    keyword = input('Введите поисковый запрос -> ')

    # Запрос у пользователя количества страниц для парсинга
    count = int(input('Введите количество страниц для парсинга (1 страница - 100 вакансий) -> '))

    # если есть экземпляр класса HeadHunterAPI() и нет экземпляра класса SuperJobAPI()
    if hh_api and not sj_api:
        hh_vacancies = hh_api.get_vacancies(keyword, count)  # Вакансии с сайта hh
        sj_vacancies = None  # вакансии с сайта sj

        if hh_vacancies:
            print(f'Парсинг прошел успешно. Найдено {len(hh_vacancies)} вакансий с сайта headhunter.ru')
        else:
            print('Нет вакансий, соответствующих заданным критериям')
            exit()

    # если есть экземпляр класса SuperJobAPI() и нет экземпляра класса HeadHunterAPI()
    if sj_api and not hh_api:
        hh_vacancies = None  # Вакансии с сайта hh
        sj_vacancies = sj_api.get_vacancies(keyword, count)  # вакансии с сайта sj

        if sj_vacancies:
            print(f'Парсинг прошел успешно. Найдено {len(sj_vacancies)} вакансий с сайта superjob.ru')
        else:
            print('Нет вакансий, соответствующих заданным критериям')
            exit()

    # во всех остальных случаях должны создаться два экземпляра: HeadHunterAPI() и SuperJobAPI()
    else:
        hh_vacancies = hh_api.get_vacancies(keyword, count)  # Вакансии с сайта hh
        sj_vacancies = sj_api.get_vacancies(keyword, count)  # вакансии с сайта sj

        if hh_vacancies:
            print(f'Парсинг прошел успешно. Найдено {len(hh_vacancies)} вакансий с сайта headhunter.ru')
        if sj_vacancies:
            print(f'Парсинг прошел успешно. Найдено {len(sj_vacancies)} вакансий с сайта superjob.ru')
        if not hh_vacancies and not sj_vacancies:
            print('Нет вакансий, соответствующих заданным критериям')
            exit()

    json_saver = JSONSaver(keyword)  # Создание экземпляра класса JSONSaver
    json_saver.add_vacancies(hh_vacancies, sj_vacancies)  # Добавление вакансий в json файлы (отдельно hh и sj)
    print_vacancies(json_saver.vacancies)
    filter_word = input("Введите ключевое слово для фильтрации вакансий: ")  # ключевое слово для поиска
    filtered_vacancies = filter_vacancies(filter_word, json_saver.vacancies)  # отфильтрованные вакансии

    if filtered_vacancies:
        print(f'По Вашему запросу найдено {len(filtered_vacancies)} вакансий')
    else:
        print('Нет вакансий, соответствующих заданным критериям')
        exit()

    # Запрос у пользователя какие операции произвести с вакансиями
    query = input(('1 - Фильтрация вакансий по уровню минимального оклада\n'
                   '2 - Фильтрация вакансий по региону\n'
                   '3 - Фильтрация вакансий без опыта работы или с опытом от 1 года\n'
                   '4 - Отфильтровать вакансии по максимальной зарплате\n'))

    # Фильтрация по зарплате
    if query == '1':
        salary = input('Введите желаемый уровень оклада в рублях, например 40000-60000, или 80000 -> ')
        filtered_vacancies = json_saver.get_vacancies_by_salary(salary)

    # Фильтрация по региону
    elif query == '2':
        region = input('Введите регион -> ')
        filtered_vacancies = json_saver.get_vacancies_by_region(region)

    # Фильтрация по опыту работы
    elif query == '3':
        filtered_vacancies = get_vacancies_without_experience(filtered_vacancies)

    if not filtered_vacancies:
        print('Нет вакансий, соответствующих заданным критериям')
        exit()

    sorted_vacancies = sort_vacancies(filtered_vacancies)  # Сортировка вакансий по минимальному окладу

    query = input('Хотите отфильтровать топ N вакансий с максимальным уровнем оклада?(Да/Нет)')
    if query.lower() == 'да':
        top_n = int(input("Введите количество вакансий для вывода в топ N: "))
        sorted_vacancies = get_top_vacancies(sorted_vacancies, top_n)

    while True:
        print_vacancies(sorted_vacancies)  # вывод в консоль результатов
        # Запрос у пользователя какие операции произвести с вакансиями
        query = input('1 - Сохранить результаты работы в json-файл\n'
                      '2 - Удалить из списка вакансию по ее ID\n')

        # Сохранение отфильтрованных и отсортированных вакансий в json-файл
        if query == '1':
            json_saver.save_results_to_json(sorted_vacancies)
            break

        # Удаление вакансии из списка
        elif query == '2':
            del_id = input('Введите ID вакансии для ее удаления из списка')
            json_saver.delete_vacancie(del_id)


if __name__ == '__main__':
    user_interaction()
