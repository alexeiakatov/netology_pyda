from datetime import date

stats = [
    ['2018-01-01', 'google', 25],
    ['2018-01-01', 'yandex', 65],
    ['2018-01-01', 'market', 89],
    ['2018-01-02', 'google', 574],
    ['2018-01-02', 'yandex', 249],
    ['2018-01-02', 'market', 994],
    ['2018-01-03', 'google', 1843],
    ['2018-01-03', 'yandex', 1327],
    ['2018-01-03', 'market', 1764],
]

DATE_INDEX = 0
COMPANY_NAME_INDEX = 1
ADVERTISING_COUNT_INDEX = 2

valid_companies = ['google', 'yandex', 'market']


def is_input_date_valid(date_string):
    if date_string is None or len(date_string) == 0:
        return False

    date_split = date_string.strip().split('-')

    if len(date_split) < 3:
        return False

    year = date_split[0].strip()
    month = date_split[1].strip()
    day = date_split[2].strip()

    if (len(year) > 4
            or 0 == len(month) > 2
            or 0 == len(day) > 2):
        return False

    try:
        date(int(year), int(month), int(day))

    except Exception:
        return False

    return True


def is_input_company_name_valid(company_name):
    if company_name is None or len(company_name) == 0:
        return False

    if company_name not in valid_companies:
        return False

    return True


def main():

    input_company_name = input('Введите название компании: ')
    input_date = input('Введите дату в формате \'YYYY-MM-DD\': ')

    valid_company_name = is_input_company_name_valid(input_company_name)
    valid_date = is_input_date_valid(input_date)

    if valid_company_name and valid_date:

        for stat_element in stats:
            if stat_element[DATE_INDEX] == input_date and stat_element[COMPANY_NAME_INDEX] == input_company_name:
                print(f'Рекламных компаний: {stat_element[ADVERTISING_COUNT_INDEX]}')
                break

    elif not valid_company_name:
        print('Такой компании нет')

    elif not valid_date:
        print('Неправильно введена дата')


main()
