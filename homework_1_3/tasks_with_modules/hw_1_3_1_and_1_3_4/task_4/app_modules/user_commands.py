import tasks_with_modules.hw_1_3_1_and_1_3_4.task_4.app_modules.handlers as handlers

COMMAND_NAME_KEY = 'command'
COMMAND_ALIAS_KEY = 'alias'
COMMAND_HANDLER_KEY = 'handler'
COMMAND_DESCRIPTION_KEY = 'description'


commands = [
    {'command': 'people', 'alias': 'p', 'handler': handlers.get_person_name_handler,
     'description': 'Cпросит номер документа и выведет имя человека, которому он принадлежит'},

    {'command': 'shelf', 'alias': 's', 'handler': handlers.get_shelf_id_handler,
     'description': 'Cпросит номер документа и выведет номер полки, на которой он находится'},

    {'command': 'list', 'alias': 'l', 'handler': handlers.show_all_documents_handler,
     'description': 'Выведет список всех документов в формате: (тип_документа номер документа фио)'},

    {'command': 'add shelf', 'alias': 'as', 'handler': handlers.create_shelf_handler,
     'description': 'Спросит номер новой полки и добавит ее в перечень'},

    {'command': 'delete', 'alias': 'd', 'handler': handlers.delete_document_handler,
     'description': 'Спросит номер документа и удалит его из каталога и из перечня полок'},

    {'command': 'move', 'alias': 'm', 'handler': handlers.move_document_handler,
     'description': 'Спросит номер документа и целевую полку и переместит документ с текущей полки на целевую'},

    {'command': 'add', 'alias': 'a', 'handler': handlers.create_document_handler,
     'description': ('Добавит новый документ в каталог и в перечень полок, спросив его номер, тип, имя владельца '
                     'и номер полки, на котором он будет храниться')},

    {'command': 'exit', 'alias': 'exit', 'handler': handlers.program_exit_handler, 'description': 'Выход из программы'},

    {'command': '?', 'alias': '?', 'handler': handlers.show_all_commands_handler, 'description': 'Покажет список всех команд'},

    {'command': 'list directories', 'alias': 'ld', 'handler': handlers.show_all_directories_handler, 'description': 'Покажет список всех команд'},
]


def get_handler(input_string):
    for command in commands:
        if command.get(COMMAND_NAME_KEY) == input_string or command.get(COMMAND_ALIAS_KEY) == input_string:
            return command.get(COMMAND_HANDLER_KEY)

    return None


def show_all_commands():
    print()
    for command in commands:
        name = command.get(COMMAND_NAME_KEY)
        alias = command.get(COMMAND_ALIAS_KEY)
        description = command.get(COMMAND_DESCRIPTION_KEY)
        print(f'{name} ({alias}) : {description}')
