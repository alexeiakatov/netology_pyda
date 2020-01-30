import os
from netology_pyda.homework_1_5.task_2.regex_rules import get_parted_rules
from netology_pyda.homework_1_5.task_2.test_emails import get_test_email_addresses
from netology_pyda.homework_1_5.task_2.main import has_email_rule_violation, log_found_violation


def _log_test_report(report_name, report):
    print('***************************')
    print(report_name + ': ')
    print()

    for k, v in report.items():
        print(k)
        print(v)
        print()


def _test_regex_rule(rule_name):
    rule = get_parted_rules()[rule_name]
    emails = get_test_email_addresses()[rule_name]

    report = {'invalid': [], 'valid': []}

    for email in emails:
        has_violation = has_email_rule_violation(rule, email)['status']

        if has_violation:
            report['invalid'].append(email)

        elif not has_violation:
            report['valid'].append(email)

    _log_test_report(rule_name, report)


def test_contains_forbidden_symbols():
    _test_regex_rule('forbidden_symbols')


def test_mail_symbol_duplication():
    _test_regex_rule('mail_symbol_duplication')


def test_mail_symbol_missing():
    _test_regex_rule('mail_symbol_missing')


def test_dots_duplication():
    _test_regex_rule('dots_duplication')


def test_min_local_part_length():
    _test_regex_rule('min_local_part_length')


def test_max_local_part_length():
    _test_regex_rule('max_local_part_length')


def test_digits_after_last_dot():
    _test_regex_rule('digits_after_last_dot')


def test_length_after_last_dot():
    _test_regex_rule('length_after_last_dot')


def test_no_dots():
    _test_regex_rule('no_dots')


def test_domain_part_length_from_start_to_last_dot():
    _test_regex_rule('domain_part_length_from_start_to_last_dot')


def main():
    print('********************************')
    print('1 - запрещенные символы')
    print('2 - дублирование символа @')
    print('3 - отсутствие символа @')
    print('4 - дублирование точек')
    print('5 - минимальная длина локальной части')
    print('6 - максимальная длина локальной части')
    print('7 - цифры после последней точки')
    print('8 - длина после последней точки')
    print('9 - отсутствие точек')
    print('10 - длина от символа @ до последней точки')
    print('********************************')

    while True:
        command = input('Введите номер теста для запуска (exit - выход): ').strip()

        if command == 'exit':
            print('Выход')
            break

        elif command == '1':
            test_contains_forbidden_symbols()

        elif command == '2':
            test_mail_symbol_duplication()

        elif command == '3':
            test_mail_symbol_missing()

        elif command == '4':
            test_dots_duplication()

        elif command == '5':
            test_min_local_part_length()

        elif command == '6':
            test_max_local_part_length()

        elif command == '7':
            test_digits_after_last_dot()

        elif command == '8':
            test_length_after_last_dot()

        elif command == '9':
            test_no_dots()

        elif command == '10':
            test_domain_part_length_from_start_to_last_dot()


if __name__ == '__main__':
    main()
