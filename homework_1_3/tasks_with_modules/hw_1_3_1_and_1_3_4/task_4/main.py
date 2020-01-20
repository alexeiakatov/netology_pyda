import tasks_with_modules.hw_1_3_1_and_1_3_4.task_4.app_modules.user_commands as user_commands

EXIT_INFO = 'Выход - exit в любом поле ввода'
ALL_COMMANDS_MESSAGE = 'Список команд - ? в любом поле ввода'
INPUT_COMMAND_MESSAGE = 'Введите команду: '
COMMAND_NOT_FOUND = 'Команда не найдена'


def main():
    while True:
        print()
        print('***************************************************')
        print(EXIT_INFO)
        print(ALL_COMMANDS_MESSAGE)
        input_command = input(INPUT_COMMAND_MESSAGE).strip().lower()
        handler = user_commands.get_handler(input_command)

        if handler is not None:
            handler()

        else:
            print(COMMAND_NOT_FOUND)


if __name__ == '__main__':
    main()
