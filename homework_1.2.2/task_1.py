geo_logs = [
    {'visit1': ['Москва', 'Россия']},
    {'visit2': ['Дели', 'Индия']},
    {'visit3': ['Владимир', 'Россия']},
    {'visit4': ['Лиссабон', 'Португалия']},
    {'visit5': ['Париж', 'Франция']},
    {'visit6': ['Лиссабон', 'Португалия']},
    {'visit7': ['Тула', 'Россия']},
    {'visit8': ['Тула', 'Россия']},
    {'visit9': ['Курск', 'Россия']},
    {'visit10': ['Архангельск', 'Россия']}
]

VISIT_NAME_INDEX = 0
VISIT_ROUTE_INDEX = 1

ROUTE_COUNTRY_INDEX = 1
TARGET_COUNTRY = 'Россия'

ROUTE_LIST_LENGTH = 2
VISIT_KEY_PREFIX = 'visit'


get_logs = lambda: geo_logs

is_target_key = lambda key: (key is not None
                             and type(key) == str
                             and key.startswith(VISIT_KEY_PREFIX))


is_route_valid = lambda route: (route is not None
                                and type(route) == list
                                and len(route) == ROUTE_LIST_LENGTH
                                and route[ROUTE_COUNTRY_INDEX] is not None)


is_target_route = lambda route: route[ROUTE_COUNTRY_INDEX] == TARGET_COUNTRY


get_target_logs = lambda geo_logs: ([log_item
                                     for log_item in geo_logs
                                     for key, value in log_item.items()
                                     if is_target_key(key)
                                     and is_route_valid(value)
                                     and is_target_route(value)])


remove_invalid_logs = lambda geo_logs: ([log_item for log_item in geo_logs
                                         if log_item is not None
                                         and type(log_item) == dict
                                         and len(log_item) > 0])


def show_logs(logs):
    for log_item in logs:
        print(log_item)


def main():
    target_logs = get_target_logs(get_logs())
    show_logs(target_logs)


if __name__ == '__main__':
    main()
