from netology_pyda.homework_1_3.task_1_with_user_input.config import config, get_run_types
from netology_pyda.homework_1_3.task_1_with_user_input.user_input import get_user_input, show_matrix

RUN_TYPE_KEY = 'run_type'
RUN_TYPE_DEMO = 'demo'
RUN_TYPE_USER_INPUT = 'user_input'

CONFIG_OBJECT_DATA_KEY = 'data'

BAD_CONFIG_MESSAGE = 'Некорректный конфигурационный файл'


config_object = config()


def validate_configuration():

    if RUN_TYPE_KEY in config_object:
        run_type = config_object[RUN_TYPE_KEY]
        all_run_types = get_run_types()

        if run_type is not None and type(run_type) == str and run_type in all_run_types:
            return

    if CONFIG_OBJECT_DATA_KEY in config_object:
        data = config_object[CONFIG_OBJECT_DATA_KEY]

        if data is not None and type(data) == list and len(data) > 0:
            return

    print(BAD_CONFIG_MESSAGE)


def calculate_main_diagonal_sum(matrix):

    main_diagonal_sum = 0

    for row_idx in range(len(matrix)):
        for col_idx in range(len(matrix[0])):
            if row_idx == col_idx:
                main_diagonal_sum += matrix[row_idx][col_idx]

    return main_diagonal_sum


def main():
    validate_configuration()
    run_type = config_object[RUN_TYPE_KEY]

    matrix = None

    if run_type == RUN_TYPE_DEMO:
        matrix = config_object[CONFIG_OBJECT_DATA_KEY]
        show_matrix(matrix)
        print()

    elif run_type == RUN_TYPE_USER_INPUT:
        matrix = get_user_input()

    main_diagonal_sum = calculate_main_diagonal_sum(matrix)

    print(f'Сумма по основной диагонали: {main_diagonal_sum}')


if __name__ == '__main__':
    main()
