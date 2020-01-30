_email_regex_rules = {

    'forbidden_symbols': {
        'regex': '([\\s,\\/:;\\\\|#%*\\(\\)=+!?\\{\\}\\[\\]$"\\^~`\'&-]+)',
        'message': 'адрес не должен содержать запрещенные символы'
    },

    'mail_symbol_duplication': {
        'regex': '^[^@]*@+[^@]*@+[^@]*$',
        'message': 'в адресе д.б. не более одного символа @'
    },

    'mail_symbol_missing': {
        'regex': '^[^@]*$',
        'message': 'в адресе должен быть хотя бы один символ @'
    },

    'dots_duplication': {
        'regex': '(\\.{2,})',
        'message': 'адрес не должен содержать пследовательность точек какой-либо длины'
    },

    'min_local_part_length': {
        'regex': '(^.{0,3}@.*$)',
        'message': 'длина локальной части д.б. не менее 4х символов'
    },

    'max_local_part_length': {
        'regex': '(^.{50,}@.*$)',
        'message': 'длина локальной части д.б. не более 50 символов'
    },

    'digits_after_last_dot': {
        'regex': '(@.*\\.[^.]*\\d+[^.]*$)',
        'message': 'доменная часть от последней точки и до конца не должна содержать цифры'
    },

    'length_after_last_dot': {
        'regex': '(?:(?:@.*\\.[^.]?$)|(?:@.*\\.[^.]{5,}$))',
        'message': 'доменная часть от последней точки и до конца адреса д.б. не менее 2х симвовло и не более 4х символов'
    },

    'no_dots': {
        'regex': '(@[^\\.]*$)',
        'message': 'доменная часть должна содержать хотя бы одну точку'
    },

    'domain_part_length_from_start_to_last_dot': {
        'regex': '(@.{0,3}\\.[^\\.]*$)',
        'message': 'часть от @ до последней точки д.б. не менее 4х символов'
    }
}

_composite_email_regex_rule = '^[a-zA-Z0-9_]{4,50}@([a-z0-9]([a-z0-9_]*[a-z0-9])?\\.)+[a-z]{2,4}$'

get_parted_rules = lambda: _email_regex_rules
get_composite_rule = lambda: _composite_email_regex_rule
