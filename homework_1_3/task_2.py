
INPUT_FIBONACCI_ELEMENTS_COUNT = 'Сумму скольки первых чисел Фибоначчи нужно посчитать: '
FIBONACCI_SUM_RESULT = 'Сумма первых {:s} чисел Фибоначи = {:s}'
FIBONACCI_VALUES_MESSAGE = 'Последовательность чисел Фибоначи:'
EXIT_INFO_MESSAGE = '*** Для выхода введите \'exit\' ***'
INPUT_EXIT_COMMAND = 'exit'
BAD_INPUT_MESSAGE = 'Введены неправильные данные!'


get_default_fibonacci_values = lambda: [0, 1]


def create_fibonacci_row(elements_count):

    fibonacci_values = get_default_fibonacci_values()

    if elements_count == 1 or elements_count == 2:
        return fibonacci_values

    idx_1 = None
    idx_2 = None

    for i in range(elements_count):
        if i == 0 or i == 1:
            continue

        idx_1 = i - 1
        idx_2 = i - 2
        fibonacci_values.append(fibonacci_values[idx_1] + fibonacci_values[idx_2])

    return fibonacci_values


def get_fibonacci_sum(elements_count):
    fibonacci_values = create_fibonacci_row(elements_count)

    if elements_count == 1:
        return fibonacci_values[0]

    elif elements_count == 2:
        return fibonacci_values[1]

    else:
        print(FIBONACCI_VALUES_MESSAGE)
        print(fibonacci_values)
        print()
        return sum(fibonacci_values)


is_user_input_valid = lambda user_input: (user_input is not None
                                          and type(user_input) == str
                                          and user_input.isnumeric()
                                          and int(user_input) > 0)


is_exit_command = lambda input_string: input_string == INPUT_EXIT_COMMAND


def get_fibonacci_row_by_recursion(elements_count, array):

    if elements_count > len(array):
        if len(array) == 0:
            array.append(0)

        elif len(array) == 1:
            array.append(1)

        else:
            idx_1 = len(array) - 1
            idx_2 = len(array) - 2

            array.append(array[idx_1] + array[idx_2])

        get_fibonacci_row_by_recursion(elements_count, array)

    return array


def get_fibonacci_sum_by_recursion(elements_count):
    fibonacci_values = get_fibonacci_row_by_recursion(elements_count, [])
    print(FIBONACCI_VALUES_MESSAGE)
    print(fibonacci_values)
    print()

    return sum(fibonacci_values)


def main():
    print(EXIT_INFO_MESSAGE)
    print()

    while True:
        fibonacci_elements_count = input(INPUT_FIBONACCI_ELEMENTS_COUNT).strip()

        if is_exit_command(fibonacci_elements_count):
            break

        if is_user_input_valid(fibonacci_elements_count):
            result = get_fibonacci_sum(int(fibonacci_elements_count))
            print(FIBONACCI_SUM_RESULT.format(fibonacci_elements_count, str(result)))

            print()
            print('Через рекурсию:')
            result_by_recursion = get_fibonacci_sum_by_recursion(int(fibonacci_elements_count))
            print(FIBONACCI_SUM_RESULT.format(fibonacci_elements_count, str(result_by_recursion)))

        else:
            print(BAD_INPUT_MESSAGE)

        print('****************************')
        print()


if __name__ == '__main__':
    main()
