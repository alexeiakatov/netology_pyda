from tasks_with_modules.hw_1_3_1_and_1_3_4.task_4.data.data import get_data
import tasks_with_modules.hw_1_3_1_and_1_3_4.task_4.data.data_functions as data_functions


# api методы
def get_document_by_number(document_number):
    action_result_cb = data_functions.get_document_by_number(document_number, get_data())
    return action_result_cb()


def get_directory_id_by_document_number(document_number):
    action_result_cb = data_functions.get_directory_id_by_document_number(document_number, get_data())
    return action_result_cb()


def create_directory(directory_id):
    action_result_cb = data_functions.create_directory(directory_id, get_data())
    return action_result_cb()


def delete_document_from_directories(document_number):
    return data_functions.delete_document_from_directories(document_number, get_data())


def delete_document_by_number(document_number):
    action_result_cb = data_functions.delete_document_by_number(document_number, get_data())
    return action_result_cb()


def create_new_document(new_document, target_directory_id):
    action_result_cb = data_functions.create_new_document(new_document, target_directory_id, get_data())
    return action_result_cb()


def move_document_to_another_directory(document_number, target_directory_id):
    action_result_cb = data_functions.move_document_to_another_directory(document_number, target_directory_id, get_data())
    return action_result_cb()


def show_all_documents():
    data_functions.show_all_documents(get_data())


def show_all_directories():
    data_functions.show_all_directories(get_data())
