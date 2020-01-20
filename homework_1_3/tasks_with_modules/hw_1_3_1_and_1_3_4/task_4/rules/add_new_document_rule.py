mandatory_fields = ['type', 'number', 'name']


def is_all_mandatory_fields(document):
    for mandatory_field in mandatory_fields:
        if mandatory_field not in document:
            return False

    return True


def validate_fields_values(document):

    for field in mandatory_fields:
        if document[field] is None or type(document[field]) != str:
            raise Exception('incorrect value object')

        elif len(document[field].strip()) == 0:
            raise Exception(f'{field} cannot be empty')


def apply(document):

    if document is None or type(document) != dict:
        raise Exception('incorrect document object')

    if not is_all_mandatory_fields(document):
        raise Exception('not all mandatory fields')

    validate_fields_values(document)
