data = [
    [13, 25, 23, 34],
    [45, 32, 44, 47],
    [12, 33, 23, 95],
    [13, 53, 34, 35]
]


def show_matrix(matrix):
    if matrix is not None and type(matrix) == list and len(matrix) > 0:
        for row in matrix:
            if len(row) > 0:
                print(row)


def calculate_main_diagonal_sum(matrix):
    show_matrix(data)
    print()
    main_diagonal_sum = 0

    for row_idx in range(len(matrix)):
        for col_idx in range(len(matrix[0])):
            if row_idx == col_idx:
                main_diagonal_sum += matrix[row_idx][col_idx]

    return main_diagonal_sum


def main():
    print(f'Сумма по основной диагонали: {calculate_main_diagonal_sum(data)}')


if __name__ == '__main__':
    main()
