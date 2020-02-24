from netology_pyda.homework_1_6_dates.PeriodAsDayList import PeriodAsDayList
from datetime import datetime, timedelta


class PeriodAsDayListTest(PeriodAsDayList):
    """
    Наследуем от суперкласса для возможности тестировать protected члены суперкласса.
    """

    def __init__(self):
        super().__init__(None, None)

    def run_tests(self):
        try:
            # self.test_parse_string_to_datetime_fail()
            self.test_period_as_day_list_fail_if_start_or_end_missing()
            self.test_parse_string_to_datetime_fail()
            self.test_parse_string_to_datetime_success()
            self.test_number_of_returned_days()
            self.test_dates_of_returned_days()

        except Exception as ex:
            print(ex)

    #
    def test_parse_string_to_datetime_fail(self):
        fail_dates = ['20-02-24',
                      '2020, 02, 24',
                      '2020.02.24',
                      '2020/02/24',
                      '2020 02 24',
                      '2020_02_24',
                      '2020%02%24',
                      '2-4',
                      '02-24',
                      '2020-02',
                      'yyyy-mm-dd',
                      '020-02-24',
                      '2020',
                      '02',
                      '24']

        success_parse = list()

        for fail_date in fail_dates:
            try:
                parsed_datetime = super()._parse_string_to_datetime(fail_date)
                success_parse.append(parsed_datetime)
            except Exception as ex:
                print(ex)

        if len(success_parse) > 0:
            raise Exception('Тест не пройден: test_parse_string_to_datetime_fail')

    #
    def test_parse_string_to_datetime_success(self):
        correct_datetime_strings = {
            '2019-12-31': datetime(2019, 12, 31),
            '2020-02-24': datetime(2020, 2, 24),
            '2020-01-20': datetime(2020, 1, 20)
        }

        for k, v in correct_datetime_strings.items():
            if super()._parse_string_to_datetime(k) != v:
                raise Exception('Тест не пройден: test_parse_string_to_datetime_success')

    #
    def test_period_as_day_list_fail_if_start_or_end_missing(self):

        super().set_start_date(datetime(2020, 2, 24))
        super().set_end_date(None)

        has_exception = False
        try:
            super().period_as_day_list()
        except:
            has_exception = True

        if not has_exception:
            raise Exception('Тест не пройден (end_date): test_period_as_day_list_fail_if_any_param_missing')

        super().set_start_date(None)
        super().set_end_date(datetime(2020, 2, 24))

        has_exception = False

        try:
            super().period_as_day_list()
        except:
            has_exception = True

        if not has_exception:
            raise Exception('Тест не пройден (end_date): test_period_as_day_list_fail_if_any_param_missing')

        self._clean_super_fields()

    #
    def test_number_of_returned_days(self):
        period_start = datetime(2020, 2, 24)
        period_end = datetime(2020, 2, 26)

        super().set_start_date(period_start)
        super().set_end_date(period_end)

        success_day_count = (period_end - period_start).days
        actual_day_count = len(super().period_as_day_list())

        if success_day_count != actual_day_count:
            raise Exception('Тест не пройден: test_number_of_returned_days')

    #
    def test_dates_of_returned_days(self):
        period_start = datetime(2020, 2, 24)
        period_end = datetime(2020, 2, 26)

        super().set_start_date(period_start)
        super().set_end_date(period_end)

        actual_day_1, actual_day_2 = super().period_as_day_list()

        if (actual_day_1 != period_start
                or actual_day_2 != period_start + timedelta(days=1)):

            raise Exception('Тесе не пройден: test_dates_of_returned_days')

        self._clean_super_fields()

    #
    def _clean_super_fields(self):
        super().set_start_date(None)
        super().set_end_date(None)



