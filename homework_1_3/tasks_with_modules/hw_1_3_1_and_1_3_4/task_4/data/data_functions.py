from tasks_with_modules.hw_1_3_1_and_1_3_4.task_4.data.action_result import get_action_result_cb
import tasks_with_modules.hw_1_3_1_and_1_3_4.task_4.rules.add_new_document_rule as add_new_document_rule


DATA_DOCUMENTS_KEY = 'documents'
DATA_DIRECTORIES_KEY = 'directories'

DOCUMENT_NUMBER_KEY = 'number'
DOCUMENT_TYPE_KEY = 'type'
DOCUMENT_NAME_KEY = 'name'

ACTION_RESULT_STATUS_KEY = 'status'
ACTION_RESULT_KEY = 'result'

DOCUMENT_NOT_FOUND = 'document not found'
DIRECTORY_NOT_FOUND = 'directory not found'

INVALID_DOCUMENT_NUMBER = 'invalid document number'
INVALID_DIRECTORY_ID = 'invalid directory id'

FOUND = 'found'
DELETED = 'deleted'
CREATED = 'created'
ALREADY_EXISTS = 'already exists'
UPDATED = 'updated'

DOCUMENTS_DATA_NOT_FOUND = 'documents data not found'
DIRECTORIES_DATA_NOT_FOUND = 'directories data not found'


_is_directory_id_valid = lambda directory_id: (directory_id is not None
                                               and type(directory_id) is str
                                               and len(directory_id) > 0
                                               and directory_id.isnumeric())

_is_directory_exist = lambda directory_id, directories: directory_id in directories.keys()

_is_document_number_valid = lambda document_number: (document_number is not None
                                                     and type(document_number) is str
                                                     and len(document_number) > 0)

_is_directory_element_valid = lambda element: (element is not None
                                               and type(element) == str
                                               and len(element) > 0)


def if_none_exception(element, message):
    if element is None:
        raise Exception(message)


def get_document_by_number(document_number, data):
    documents = data.get(DATA_DOCUMENTS_KEY)
    if_none_exception(documents, DOCUMENTS_DATA_NOT_FOUND)

    if not _is_document_number_valid(document_number):
        return get_action_result_cb(False, INVALID_DOCUMENT_NUMBER)

    for document in documents:
        if document is not None and document.get(DOCUMENT_NUMBER_KEY) == document_number:
            return get_action_result_cb(True, FOUND, document)

    return get_action_result_cb(False, DOCUMENT_NOT_FOUND)


def get_directory_id_by_document_number(document_number, data):
    directories = data.get(DATA_DIRECTORIES_KEY)
    if_none_exception(directories, DIRECTORIES_DATA_NOT_FOUND)

    if not _is_document_number_valid(document_number):
        return get_action_result_cb(False, INVALID_DOCUMENT_NUMBER)

    action_result_cb = get_document_by_number(document_number, data)
    search_document_action_result = action_result_cb()

    if not search_document_action_result.get('status'):
        return action_result_cb

    for directory_id, directory in directories.items():
        if (directory_id is not None
                and directory is not None
                and type(directory) == list
                and document_number in directory):

            return get_action_result_cb(True, FOUND, directory_id)

    return get_action_result_cb(False, DIRECTORY_NOT_FOUND)


def create_directory(directory_id, data):
    directories = data.get(DATA_DIRECTORIES_KEY)
    if_none_exception(directories, DIRECTORIES_DATA_NOT_FOUND)

    if not _is_directory_id_valid(directory_id):
        return get_action_result_cb(False, INVALID_DIRECTORY_ID)

    if _is_directory_exist(directory_id, directories):
        return get_action_result_cb(False, ALREADY_EXISTS, directory_id)

    directories.setdefault(directory_id, [])
    return get_action_result_cb(True, CREATED, directory_id)


def delete_document_from_directories(document_number, data):
    directories = data.get(DATA_DIRECTORIES_KEY)
    if_none_exception(directories, DIRECTORIES_DATA_NOT_FOUND)

    if not _is_document_number_valid(document_number):
        return get_action_result_cb(False, INVALID_DOCUMENT_NUMBER)

    for directory_id, directory in directories.items():
        if directory is not None and document_number in directory:
            
            directories[directory_id] = list(filter(lambda el: el != document_number, directory))
            
            return get_action_result_cb(True, DELETED, directory_id)

    return get_action_result_cb(False, DIRECTORY_NOT_FOUND)


def delete_document_by_number(document_number, data):
    documents = data.get(DATA_DOCUMENTS_KEY)
    if_none_exception(documents, DOCUMENTS_DATA_NOT_FOUND)
    
    if not _is_document_number_valid(document_number):
        return get_action_result_cb(False, INVALID_DOCUMENT_NUMBER)

    for document in documents:
        if document is not None and document.get(DOCUMENT_NUMBER_KEY) == document_number:
            
            data[DATA_DOCUMENTS_KEY] = list(filter(lambda el: el[DOCUMENT_NUMBER_KEY] != document_number, documents))
            delete_document_from_directories(document_number, data)
            return get_action_result_cb(True, DELETED, document_number)

    return get_action_result_cb(False, DOCUMENT_NOT_FOUND)


def create_new_document(new_document, target_directory_id, data):
    """
    new_document - dict (должен сдоержать ключи 'name', 'type', 'number')
    """

    documents = data.get(DATA_DOCUMENTS_KEY)
    directories = data.get(DATA_DIRECTORIES_KEY)
    
    if_none_exception(documents, DOCUMENTS_DATA_NOT_FOUND)
    if_none_exception(directories, DIRECTORIES_DATA_NOT_FOUND)
    
    try:
        add_new_document_rule.apply(new_document)
    except Exception as ex:
        return get_action_result_cb(False, str(ex))

    if not _is_directory_id_valid(target_directory_id):
        return get_action_result_cb(False, INVALID_DIRECTORY_ID)

    if not _is_directory_exist(target_directory_id, directories):
        return get_action_result_cb(False, DIRECTORY_NOT_FOUND)

    if new_document in documents:
        return get_action_result_cb(False, ALREADY_EXISTS)

    documents.append(new_document)
    directories[target_directory_id].append(new_document[DOCUMENT_NUMBER_KEY])
    return get_action_result_cb(True, CREATED)


def move_document_to_another_directory(document_number, target_directory_id, data):
    documents = data.get(DATA_DOCUMENTS_KEY)
    directories = data.get(DATA_DIRECTORIES_KEY)

    if_none_exception(documents, DOCUMENTS_DATA_NOT_FOUND)
    if_none_exception(directories, DIRECTORIES_DATA_NOT_FOUND)

    if not _is_document_number_valid(document_number):
        return get_action_result_cb(False, INVALID_DOCUMENT_NUMBER)

    if not _is_directory_id_valid(target_directory_id):
        return get_action_result_cb(False, INVALID_DIRECTORY_ID)

    action_result_cb = get_document_by_number(document_number, data)
    document_search_response = action_result_cb()

    if not document_search_response[ACTION_RESULT_STATUS_KEY]:
        return action_result_cb

    if not _is_directory_exist(target_directory_id, directories):
        return get_action_result_cb(False, DIRECTORY_NOT_FOUND)

    document_number = document_search_response[ACTION_RESULT_KEY][DOCUMENT_NUMBER_KEY]

    delete_document_from_directories(document_number, data)
    directories[target_directory_id].append(document_number)

    return get_action_result_cb(True, UPDATED, target_directory_id)


def show_all_documents(data):
    documents = data.get(DATA_DOCUMENTS_KEY)
    if_none_exception(documents, DOCUMENTS_DATA_NOT_FOUND)

    print()
    for document in documents:
        document_type = document.get(DOCUMENT_TYPE_KEY)
        document_number = document.get(DOCUMENT_NUMBER_KEY)
        name = document.get(DOCUMENT_NAME_KEY)

        print(f'{document_type} "{document_number}" {name}')


def show_all_directories(data):
    directories = data.get(DATA_DIRECTORIES_KEY)
    if_none_exception(directories, DIRECTORIES_DATA_NOT_FOUND)

    print()
    for directory_id, directory in directories.items():
        print(f'{directory_id} : {directory}')
