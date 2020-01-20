import tasks_with_modules.hw_1_3_1_and_1_3_4.task_4.data.data_api as data_api
import tasks_with_modules.hw_1_3_1_and_1_3_4.task_4.app_modules.user_commands as user_commands

RESPONSE_STATUS_KEY = 'status'
RESPONSE_RESULT_KEY = 'result'
RESPONSE_MESSAGE_KEY = 'message'

DOCUMENT_NAME_KEY = 'name'


def delete_document_handler():
    print()
    document_number = input('Введите номер документа: ').strip().lower()
    result = data_api.delete_document_by_number(document_number)

    print(result.get(RESPONSE_MESSAGE_KEY))


def get_person_name_handler():
    print()
    document_number = input('Введите номер документа: ').strip().lower()
    result = data_api.get_document_by_number(document_number)

    if result.get(RESPONSE_STATUS_KEY):
        print(result.get(RESPONSE_RESULT_KEY).get(DOCUMENT_NAME_KEY))
    else:
        print(result.get(RESPONSE_MESSAGE_KEY))


def get_shelf_id_handler():
    print()
    document_number = input('Введите номер документа: ').strip().lower()
    result = data_api.get_directory_id_by_document_number(document_number)

    if result.get(RESPONSE_STATUS_KEY):
        print(result.get(RESPONSE_RESULT_KEY))
    else:
        print(result.get(RESPONSE_MESSAGE_KEY))


def create_shelf_handler():
    print()
    shelf_id = input('Введите номер новой полки: ').strip().lower()
    result = data_api.create_directory(shelf_id)

    if result.get(RESPONSE_STATUS_KEY):
        print(result.get(RESPONSE_MESSAGE_KEY))
        print(f'id новой полки: {result.get(RESPONSE_RESULT_KEY)}')

    else:
        print(result.get(RESPONSE_MESSAGE_KEY))


def create_document_handler():
    print()
    document_number = input('Введите номер документа: ').strip().lower()
    document_type = input('Введите тип документа: ').strip().lower()
    name = input('Введите имя владельца документа: ').strip().lower()
    target_directory_id = input('Введите номер полки где будет храниться документ: ').strip().lower()

    new_document = {'type': document_type, 'number': document_number, 'name': name}

    result = data_api.create_new_document(new_document, target_directory_id)

    print(result[RESPONSE_MESSAGE_KEY])


def move_document_handler():
    print()
    document_number = input('Введите номер документа, который нужно перенести: ').strip().lower()
    target_directory_id = input('Введите номер полки куда нужно перенести: ').strip().lower()
    result = data_api.move_document_to_another_directory(document_number, target_directory_id)

    if result.get(RESPONSE_RESULT_KEY):
        print(result.get(RESPONSE_MESSAGE_KEY))
        print(f'Документ перенесен на полку № {result.get(RESPONSE_RESULT_KEY)}')

    else:
        print(result.get(RESPONSE_MESSAGE_KEY))


def show_all_documents_handler():
    data_api.show_all_documents()


def program_exit_handler():
    exit('Программа завершила работу')


def show_all_commands_handler():
    user_commands.show_all_commands()


def show_all_directories_handler():
    data_api.show_all_directories()
