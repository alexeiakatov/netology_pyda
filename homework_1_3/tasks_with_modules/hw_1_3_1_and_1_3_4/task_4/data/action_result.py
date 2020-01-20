INVALID_PARAM_MESSAGE = '[action_result#is_arguments_valid] invalid {:s} param'


def validate_arguments(status, message):
    if status is None or type(status) is not bool:
        raise Exception(INVALID_PARAM_MESSAGE.format('status'))

    if message is None or type(message) is not str:
        raise Exception(INVALID_PARAM_MESSAGE.format('message'))

    return True


def get_action_result_cb(status, message, result = None):
    validate_arguments(status, message)
    return lambda: {'status': status, 'message': message, 'result': result}

