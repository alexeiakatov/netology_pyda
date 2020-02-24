from netology_pyda.homework_1_8_classes.task_1_and_2.CustomCurrencyUtils import CustomCurrencyUtils
import traceback as traceback


class CustomCurrencyUtilsTest(CustomCurrencyUtils):
    """
    Наследуем от класса, методы которого будем тестировать для того, чтоб иметь возможность работать
    с protected членами класса.
    """

    VALUE_KEY = 'Value'
    NAME_KEY = 'Name'

    TEST_DATA = test_data = {
            'currency_char_code_1': {NAME_KEY: 'currency_name_1', VALUE_KEY: 10.11},
            'currency_char_code_4': {NAME_KEY: 'currency_name_4', VALUE_KEY: 20.44},
            'currency_char_code_2': {NAME_KEY: 'currency_name_2', VALUE_KEY: 10.22},
            'currency_char_code_3': {NAME_KEY: 'currency_name_3', VALUE_KEY: 20.33}}

    #
    def run_tests(self):
        try:
            self.test_sort_by_rate_asc()
            self.test_sort_by_rate_desc()
            self.test_currency_with_max_rate()
            self.test_currency_name_with_max_rate()

        except Exception as ex:
            print(ex)

    #
    def test_sort_by_rate_asc(self):
        success_result = [
            self.TEST_DATA['currency_char_code_1'],
            self.TEST_DATA['currency_char_code_2'],
            self.TEST_DATA['currency_char_code_3'],
            self.TEST_DATA['currency_char_code_4'],
        ]

        actual_result = super()._sort_by_rate(self.TEST_DATA, False)

        if actual_result != success_result:
            raise Exception('Тест не пройден: test_get_sorted_by_rate_asc')

    #
    def test_sort_by_rate_desc(self):
        success_result = [
            self.TEST_DATA['currency_char_code_4'],
            self.TEST_DATA['currency_char_code_3'],
            self.TEST_DATA['currency_char_code_2'],
            self.TEST_DATA['currency_char_code_1'],
        ]

        actual_result = super()._sort_by_rate(self.TEST_DATA, True)

        if actual_result != success_result:
            raise Exception('Тест не пройден: test_get_sorted_by_rate_desc')

    #
    def test_currency_with_max_rate(self):
        success_result = self.TEST_DATA['currency_char_code_4']
        actual_result = super()._currency_with_max_rate(self.TEST_DATA)

        if actual_result != success_result:
            raise Exception('Тест не пройден: test_currency_with_max_rate')

    #
    def test_currency_name_with_max_rate(self):
        success_result = self.TEST_DATA['currency_char_code_4'][self.NAME_KEY]
        actual_result = super()._currency_name_with_max_rate(self.TEST_DATA)

        if actual_result != success_result:
            raise Exception('Тесет не пройден: test_currency_name_with_max_rate')





