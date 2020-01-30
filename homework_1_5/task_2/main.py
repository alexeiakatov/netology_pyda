import re
from netology_pyda.homework_1_5.task_2.regex_rules import get_composite_rule, get_parted_rules


show_module_logs = True


def log_found_violation(email, result_object):
    result_status = result_object.get('status')
    result_message = result_object.get('message')

    print(f'email: {email}')
    print(f'is_valid: {not result_status}')
    print(f'message: {result_message}')
    print()


def has_email_rule_violation(check_violation_rule, email):
    regex = check_violation_rule['regex']
    message = check_violation_rule['message']

    result_object = {}

    match = re.search(regex, email)

    if match:
        result_object['status'] = True
        result_object['message'] = message

        if show_module_logs:
            log_found_violation(email, result_object)

        return result_object

    result_object['status'] = False
    return result_object


def is_valid_by_composite_rule(email):
    return False if re.match(get_composite_rule(), email) is None else True


def validate_email(email):

    has_rule_violation = False
    for rule in get_parted_rules().values():
        if has_email_rule_violation(rule, email)['status']:
            has_rule_violation = True

    if has_rule_violation:
        print('По отдельным правилам - невалидный адрес')
    elif not has_rule_violation:
        print('По отдельным правилам - валидный адрес')

    valid_by_composite_rule = is_valid_by_composite_rule(email)

    if valid_by_composite_rule:
        print('По сборному правилу - валидный адрес')
    elif not valid_by_composite_rule:
        print('По сборному правилу - невалидный адрес')


def main():
    while True:
        print()
        print('----------------------------')
        email = input('Введите дрес эл. почты (exit - длявыхода): ').strip()
        print()

        if email == 'exit':
            break
        else:
            validate_email(email)

    print('Выход')


if __name__ == '__main__':
    main()


