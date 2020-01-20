source = ['2018-01-01', 'yandex', 'cpc', 100]


def validate_params(source_list, current_idx, target_map):
    if source_list is None or len(source_list) < 2:
        raise Exception('Массив-источник не м.б. None или содержать менее 2х элементов ')

    if type(current_idx) != int or current_idx < 0:
        raise Exception('Индекс д.б. положительным числом')

    if type(target_map) != dict:
        raise Exception('Неправильный тип целевого словаря')


def generate_map(source_list, current_idx=0, target_map={}):

    validate_params(source_list, current_idx, target_map)

    if current_idx <= len(source_list) - 1:

        if current_idx == 1:
            previous_list_element = source_list[current_idx - 1]
            target_map = {source_list[current_idx]:  previous_list_element}

        elif current_idx > 1:
            target_map = {source_list[current_idx]: target_map}

        return generate_map(source_list, current_idx + 1, target_map)

    return target_map


def main():
    source.reverse()
    result = generate_map(source)
    print()
    print(f'Результат {result}')


if __name__ == '__main__':
    main()

