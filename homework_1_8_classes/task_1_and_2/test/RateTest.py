from netology_pyda.homework_1_8_classes.libs.Rate import Rate


class RateTest(Rate):

    #
    def __init__(self):
        format_ = super().SELF_FORMAT_JUST_VALUE
        super().__init__(format_, True)

    #
    def run_tests(self):
        self.test_check_currency_rate_type_fail()
        self.test_check_currency_rate_type_success()
        self.test_get_diff_when_first_request()
        self.test_get_diff_when_second_request()

    #
    def test_check_currency_rate_type_fail(self):
        """
        Если переданный объект с курсом не является float должен генерировать исключение
        """

        # {'currency_char_code': 'value', ... }
        fail_data_list = [
            {super().DOLLAR_CHAR_CODE: '69.75',
             super().EURO_CHAR_CODE: '79.93'},

            {super().DOLLAR_CHAR_CODE: {},
             super().EURO_CHAR_CODE: {}},

            {super().DOLLAR_CHAR_CODE: None,
             super().EURO_CHAR_CODE: None}
        ]

        success_attempts = 0
        for fail_data in fail_data_list:
            for currency_char_code, currency_rate in fail_data.items():
                try:
                    super().check_currency_rate_type(currency_char_code, currency_rate)
                    success_attempts += 1
                except:
                    pass

        if success_attempts > 0:
            raise Exception('Тест не пройден: test_check_currency_rate_type')

    #
    def test_check_currency_rate_type_success(self):
        """
        Если переданный объект с курсом является float НЕ должен генерировать исключение
        """

        success_data = {
            super().DOLLAR_CHAR_CODE: float(69.75),
            super().EURO_CHAR_CODE: float(79.93)
        }

        fail_attempts = 0
        for currency_char_code, currency_rate in success_data.items():
            try:
                super().check_currency_rate_type(currency_char_code, currency_rate)
            except:
                fail_attempts += 1

        if fail_attempts > 0:
            raise Exception('Тест не пройден: test_check_currency_rate_type_success')

    #
    def test_get_diff_when_first_request(self):
        euro_char_code = super().EURO_CHAR_CODE
        last_values = super().last_values

        last_values[euro_char_code] = 0

        new_rate = 23.23

        actual_rate_delta = super().get_diff(euro_char_code, new_rate)

        if actual_rate_delta != new_rate or last_values[euro_char_code] != new_rate:
            raise Exception('Тест не пройден: test_get_diff_when_first_request')

        self._clear_super_last_values()

    def test_get_diff_when_second_request(self):
        euro_char_code = super().EURO_CHAR_CODE
        last_values = super().last_values

        previous_rate = 23.23
        new_rate = 18.0

        last_values[euro_char_code] = previous_rate

        success_rate_delta = new_rate - previous_rate
        actual_rate_delta = super().get_diff(euro_char_code, new_rate)

        if actual_rate_delta != success_rate_delta or last_values[euro_char_code] != new_rate:
            raise Exception('Тест не пройден: test_get_diff_when_second_request')

    #
    def _clear_super_last_values(self):
        for key in super().last_values.keys():
            super().last_values[key] = float(0)


