from classes import hh_sj_classes


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
    count = int(input('Введите количество вакансий для парсинга (кратное 50) -> '))

    hh_vacancies = hh_api.get_vacancies(keyword, count)

    for vacancy in hh_vacancies:
        print(vacancy)
        print()


if __name__ == '__main__':
    main()
