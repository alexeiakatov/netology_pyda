_test_email_adresses = {

    'forbidden_symbols': [
        'john smith@mail.ru', 'john  smith@mail.ru', 'john   smith@mail.ru', 'john,smith@mail.ru',
        'john\\smith@mail.ru', 'john/smith@mail.ru', 'john:smith@mail.ru', 'john|smith@mail.ru',
        'john;smith@mail.ru', 'john\'smith@mail.ru', 'john!smith@mail.ru', 'john#smith@mail.ru',
        'john%smith@mail.ru', 'john*smith@mail.ru', 'john)smith@mail.ru', 'john(smith@mail.ru',
        'john=smith@mail.ru', 'john+smith@mail.ru', 'john{smith@mail.ru', 'john}smith@mail.ru',
        'john[smith@mail.ru', 'john]smith@mail.ru', 'john$smith@mail.ru', 'john"smith@mail.ru',
        'john^smith@mail.ru', 'john~smith@mail.ru', 'john`smith@mail.ru', 'john`smith@mail.ru',
        'john&smith@mail.ru', 'john?smith@mail.ru', 'john-smith@mail.ru',
    ],

    'mail_symbol_duplication': [
        'john@smith@mail.ru', 'john_smith@@mail.ru', '@john_smith_AT_mail@.ru', 'john_smith@mail.ru@',
        'john_smith_AT_mail.ru@@', 'john@@@@smith@mail.ru'
    ],

    'mail_symbol_missing': [
        'john_smith_at_mail.ru', 'john_smith_at_yandex.mail.ru'
    ],

    'dots_duplication': [
        'john..smith@mail.ru', 'john...smith@mail.ru', '..john_smith@mail.ru', 'john_smith@mail..ru',
        'john_smith..@mail.ru', 'john_smith@..mail.ru', 'john_smith@mail.ru..'
    ],

    'min_local_part_length': [
        '@mail.ru', 'j@mail.ru', 'jo@mail.ru', 'joh@mail.ru'
    ],

    'max_local_part_length': [
        'john_smith_with_max_length_of_local_part_violation_@mail.ru'
    ],

    'digits_after_last_dot': [
        'john_smith@mail.co3', 'john_smith@mail.2co', 'john_smith@mail.h2o', 'john_smith@mail.333',
        'john_smith@mail.33x', 'john_smith@mail.x33', 'john_smith@mail.a2', 'john_smith@domain.2a',
        'john_smith@domain.22',
    ],

    'length_after_last_dot': [
        'john_smith@mail.', 'john_smith@mail.a', 'john_smith@mail.long_'
    ],

    'no_dots': [
        'john_smith@no_dots_in_domain'
    ],

    'domain_part_length_from_start_to_last_dot': [
        'john_smith@.com', 'john_smith@s.hort', 'john_smith@sh.ort', 'john_smith@sho.rt'
    ]
}

get_test_email_addresses = lambda: _test_email_adresses
