from sys import exit
from tasks_with_modules.hw_1_3_1_and_1_3_4.task_1_with_user_input.config import config

BAD_INPUT_MESSAGE = 'Неправильное значение'

INPUT_SIDE_SIZE_DISPLAY_MESSAGE = 'длина стороны матрицы не должна превышать {:d}'
INPUT_ELEMENT_DISPLAY_MESSAGE = 'элемент матрицы не должен превышать {:d}'
NEED_NUMERIC_VALUE_MESSAGE = 'нужно вводить числа'

INPUT_VALUE_TOO_BIG = 'Превышение максимального значения.'

INPUT_EXIT_COMMAND = 'exit'
INPUT_EXIT_MESSAGE = 'Выход!'
EXIT_INFO_MESSAGE = 'Для выхода введите exit в любой форме ввода.'

MAX_SIDE_LENGTH_KEY = 'max_side_length'
MAX_VALUE_OF_ELEMENT_KEY = 'max_value_of_element'

BAD_CONFIG_MESSAGE = 'Некорректный конфигурационный файл'

INPUT_MATRIX_ELEMENT_MESSAGE = 'Введите следующее значение матрицы: '


config_object = config()

is_config_numeric_value_valid = lambda value: value is not None and type(value) == int and value > 0

def validate_configuration():

    if MAX_SIDE_LENGTH_KEY in config_object:
        value = config_object[MAX_SIDE_LENGTH_KEY]
        if is_config_numeric_value_valid(value):
            return

    if MAX_VALUE_OF_ELEMENT_KEY in config_object:
        value = config_object[MAX_VALUE_OF_ELEMENT_KEY]
        if is_config_numeric_value_valid(value):
            return

    exit(BAD_CONFIG_MESSAGE)


# Валидация числовых значений, которые вводит пользователь
is_input_element_valid = lambda input_element: (input_element is not None
                                                and type(input_element) == str
                                                and input_element.isnumeric())


# Валидация размера стороны матрицы, который ввел пользователь
is_matrix_side_length_valid = lambda matrix_side_length: int(matrix_side_length) <= config_object[MAX_SIDE_LENGTH_KEY]


# Валидация значения элемента матрицы, который ввел пользователь
is_matrix_element_valid = lambda matrix_element: 0 < int(matrix_element) <= config_object[MAX_VALUE_OF_ELEMENT_KEY]


def check_exit(input_string):
    if input_string == INPUT_EXIT_COMMAND:
        exit(INPUT_EXIT_MESSAGE)


def matrix_element_input():

    while True:
        input_element = input(INPUT_MATRIX_ELEMENT_MESSAGE).strip()
        check_exit(input_element)

        if not is_input_element_valid(input_element):
            print(f'{BAD_INPUT_MESSAGE} : {NEED_NUMERIC_VALUE_MESSAGE}')
            print()
            continue

        if not is_matrix_element_valid(input_element):
            print(f'{BAD_INPUT_MESSAGE} : {INPUT_ELEMENT_DISPLAY_MESSAGE.format(config_object[MAX_VALUE_OF_ELEMENT_KEY])}')
            print()
            continue

        return int(input_element)


def show_matrix(matrix):
    if matrix is not None and type(matrix) == list and len(matrix) > 0:
        for row in matrix:
            if len(row) > 0:
                print(row)


def matrix_elements_input(matrix_side_length):
    result = [[] for i in range(int(matrix_side_length) )]

    for row in range(int(matrix_side_length)):
        current_row = []

        for column in range(int(matrix_side_length)):
            current_row.append(matrix_element_input())
            result[row] = current_row
            print('Текущее состояние:')
            show_matrix(result)
            print()


def get_user_input():
    validate_configuration()

    print(EXIT_INFO_MESSAGE)

    while True:
        matrix_side_length = input('Введите длину стороны квадратной матрицы (целое число): ')
        check_exit(matrix_side_length)

        if not is_input_element_valid(matrix_side_length):
            print(f'{BAD_INPUT_MESSAGE} : {NEED_NUMERIC_VALUE_MESSAGE}')
            print()
            continue

        if not is_matrix_side_length_valid(matrix_side_length):
            print(f'{BAD_INPUT_MESSAGE} : {INPUT_SIDE_SIZE_DISPLAY_MESSAGE.format(config_object[MAX_SIDE_LENGTH_KEY])}')
            print()
            continue

        return matrix_elements_input(matrix_side_length)
