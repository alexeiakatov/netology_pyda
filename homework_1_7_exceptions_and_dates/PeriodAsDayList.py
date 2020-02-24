from datetime import datetime, timedelta


class PeriodAsDayList:

    start_date: datetime = None
    end_date: datetime = None
    one_day_timedelta: timedelta = timedelta(1)

    #
    def __init__(self, start_date: str = None, end_date: str = None):
        """
        При создании объекта класса сразу преобразует даты, переданные в виде строк в объекты datetime

        start_date, end_date строки, содержащие даты в формате YYYY-MM-DD
        """

        self.start = self._parse_string_to_datetime(start_date) if start_date is not None else None
        self.end = self._parse_string_to_datetime(end_date) if end_date is not None else None

    #
    def _parse_string_to_datetime(self, date_string: str) -> datetime:
        return datetime.strptime(date_string, '%Y-%m-%d')

    #
    def period_as_day_list(self):
        if self.start_date is None or self.end_date is None:
            raise Exception('Не установлены значения начала или окончания периода')

        period_start, period_end = sorted([self.start_date, self.end_date])

        result = list()

        while period_start < period_end:
            result.append(period_start)
            period_start += self.one_day_timedelta

        return result

    #
    def set_start_date(self, start_date: datetime):
        if start_date is None or isinstance(start_date, datetime):
            self.start_date = start_date
        else:
            raise Exception('Неправильный тип параметра start_date')

    #
    def set_end_date(self, end_date: datetime):
        if end_date is None or isinstance(end_date, datetime):
            self.end_date = end_date
        else:
            raise Exception('Неправильный тип параметра end_date')
