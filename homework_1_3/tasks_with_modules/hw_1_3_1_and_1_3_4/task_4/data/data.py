_data = ({
    'documents': [
        {'type': 'passport', 'number': '2207 876234', 'name': 'Василий Гупкин'},
        {'type': 'invoice', 'number': '11-2', 'name': 'Геннадий Покемонов'},
        {'type': 'insurance', 'number': '10006', 'name': 'Аристарх Павлов'}]
    ,

    'directories': {
        '1': ['2207 876234', '11-2', '5455 028765'],
        '2': ['10006', '5400 028765', '5455 002299'],
        '3': []
    }
})

get_data = lambda: _data
