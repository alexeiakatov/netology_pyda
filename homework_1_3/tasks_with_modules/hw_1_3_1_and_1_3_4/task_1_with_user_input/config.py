# Пользовательские настройки
run_type = 'user_input'
# run_type = 'demo'

MAX_SIDE_LENGTH = 10
MAX_VALUE_OF_ELEMENT = 100

##################################

RUN_TYPES = ['demo', 'user_input']

RUN_TYPE_DEMO_INDEX = 0
RUN_TYPE_USER_INPUT_INDEX = 1

BAD_RUN_TYPE_MESSAGE = f'Неправильно указан тип выполнения программы в настройках. Возможные варианты: {RUN_TYPES}'


get_demo_data = lambda: ([
    [13, 25, 23, 34],
    [45, 32, 44, 47],
    [12, 33, 23, 95],
    [13, 53, 34, 35]
])


get_run_types = lambda: RUN_TYPES


def config():
    if run_type not in RUN_TYPES:
        exit(BAD_RUN_TYPE_MESSAGE)
        return

    if run_type == RUN_TYPES[RUN_TYPE_DEMO_INDEX]:
        return {'run_type': RUN_TYPES[RUN_TYPE_DEMO_INDEX],
                'data': get_demo_data()}

    if run_type == RUN_TYPES[RUN_TYPE_USER_INPUT_INDEX]:
        return {'run_type': RUN_TYPES[RUN_TYPE_USER_INPUT_INDEX],
                'max_side_length': MAX_SIDE_LENGTH,
                'max_value_of_element': MAX_VALUE_OF_ELEMENT}
