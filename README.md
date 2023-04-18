# Course_project_4_OOP
## Задание

Напишите программу, которая будет получать информацию о вакансиях с разных платформ в России, сохранять ее в файл и позволять удобно работать с ней
(добавлять, фильтровать, удалять).

## Платформы для сбора вакансий

1. **hh.ru** ([ссылка на API](https://github.com/hhru/api/blob/master/docs/general.md))
2. **superjob.ru** ([ссылка на API](https://api.superjob.ru/))

В моем проекте в начале программа выдает запрос, на каких сайтах искать вакансии: Headhunter или Superjob. Если ничего не ввести, то она будет искать на обеих платформах. Затем необходимо ввести ключевое слово для поиска (название профессии) и количество страниц для парсинга (ограничение API для headhunter - 20 страниц, для Superjob - 5. На одной странице выдается 100 вакансий). По умолчанию поиск ведется по всей территории России, вакансии с указанным окладом в рублях.
После парсинга необходимо отфильтровать полученные вакансии по ключевому слову (данный шаг возможно пропустить).

Затем имеется возможность дополнительной фильтрации:
- Фильтрация вакансий по уровню минимального оклада. Пользователь может ввести желаемый минимальный и максимальный оклад в виде: 50000-70000. Тогда программа отфильтрует вакансии с минимальным окладом от 50000 до 70000 и отсортирует их. Есть возможность ввести только минимальный оклад, например 50000. Тогда программа выдаст вакансии с минимальным окладом от 50000. Оклад указывается в рублях.
- Фильтрация вакансий по региону. Пользователь может ввести название города и отфильтровать вакансии, доступные только для него.
- Фильтрация вакансий по опыту работы. Если выбрать данную опцию, программа отберет вакансии без опыта работы и с опытом от 1 года.
- Фильтрация по топ N (сохранение N вакансий с максимальным уровнем оклада, отсортированных по его убыванию)

На следующем шаге возможно следующие опции:
- сохранить отфильтрованные и отсортированные на предыдущем шаге вакансии в файл
- Вывести в консоль отфильтрованный на предыдущем шаге список вакансий в удобном для пользователя формате
- Вывести в консоль отфильтрованный на предыдущем шаге список вакансий у удобном для пользователя формате
- Удалить из отфильтрованного на предыдущем шаге списка определенную вакансию по ее id.

В итоге программа создает три файла в формаете json
- файл hh_пользовательский_запрос.json - ответ с API сайта Headhunter в изначальном виде
- файл sj_пользовательский_запрос.json - ответ с API сайта Superjob в изначальном виде
- при выборе опции "Сохранить результаты работы в json-файл" создается файл result_пользовательский_запрос.json, в котором содержаться отфильтрованные пользователем вакансии, отсортированные по возрастанию оклада.
