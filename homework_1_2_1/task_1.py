boys = ['Peter', 'Alex', 'John', 'Arthur', 'Richard']
girls = ['Kate', 'Liza', 'Kira', 'Emma', 'Trisha']


# Валидация входных значений
def validate_input(boys_list, girls_list):
    length_boys = len(boys_list)
    length_girls = len(girls_list)

    if length_boys != length_girls:
        print('Количество мальчиков и девочек д.б. равным')
        return False

    elif length_boys == 0 or length_girls == 0:
        print('И мальчиков, и девочек д.б. больше ноля')
        return False

    return True


# Отображение наилучших пар
def show_couples(couples_list):
    if couples_list is None or len(couples_list) == 0:
        return

    for couple in couples_list:
        print(couple)


# Создание пар с помощью zip
def create_couples_by_zip(boys_list, girls_list):
    return list(zip(boys_list, girls_list))


# Создание пар с помощью List comprehension
def create_couples_by_comprehension(boys_list, girls_list):

    return ([[boys[idx_boys], girls[idx_girls]]
             for idx_boys in range(len(boys_list))
             for idx_girls in range(len(girls_list))
             if idx_boys == idx_girls])


# Входная точка
def main():
    is_valid_input = validate_input(boys, girls)
    boys.sort()
    girls.sort()

    if is_valid_input:
        couples_by_zip = create_couples_by_zip(boys, girls)
        couples_by_comprehension = create_couples_by_comprehension(boys, girls)

        print('Идеальные пары (by zip)')
        show_couples(couples_by_zip)

        print()

        print('Идеальные пары (by comprehension)')
        show_couples(couples_by_comprehension)


main()


