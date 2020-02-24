# coding: utf-8
import requests


class Rate:

    last_values = {'EUR': float(0), 'USD': float(0)}

    format_ = None
    diff = None

    SELF_FORMAT_JUST_VALUE = 'value'
    SELF_FORMAT_FULL = 'full'

    EURO_CHAR_CODE = 'EUR'
    DOLLAR_CHAR_CODE = 'USD'

    # вложенный мап с данными о всех валютах
    RESPONSE_VALUTE_KEY = 'Valute'

    # поле со стоимостью валюты в мапе с данными о конкретной валюты
    RESPONSE_VALUE_KEY = 'Value'

    REQUEST_ADDRESS = 'https://www.cbr-xml-daily.ru/daily_json.js'

    #
    def __init__(self,
                 format_: str = SELF_FORMAT_JUST_VALUE,
                 diff: bool = False):

        self.format_ = format_
        self.diff = diff

    #
    def exchange_rates(self):
        """
        Возвращает ответ сервиса с информацией о валютах в виде:

        {
            'AMD': {
                'CharCode': 'AMD',
                'ID': 'R01060',
                'Name': 'Армянских драмов',
                'Nominal': 100,
                'NumCode': '051',
                'Previous': 14.103,
                'Value': 14.0879
                },
            ...
        }
        """
        r = requests.get(self.REQUEST_ADDRESS)
        return r.json()[self.RESPONSE_VALUTE_KEY]

    def make_format(self, currency):
        """
        Возвращает информацию о валюте currency в двух вариантах:
        - полная информация о валюте при self.format_ = 'full':
        Rate('full').make_format('EUR')
        {
            'CharCode': 'EUR',
            'ID': 'R01239',
            'Name': 'Евро',
            'Nominal': 1,
            'NumCode': '978',
            'Previous': 79.6765,
            'Value': 79.4966
        }

        Rate('value').make_format('EUR')
        79.4966
        """
        response = self.exchange_rates()

        if currency in response:
            if self.format_ == self.SELF_FORMAT_FULL:
                return response[currency]

            if self.format_ == self.SELF_FORMAT_JUST_VALUE:
                return response[currency][self.RESPONSE_VALUE_KEY]

        return 'Error'

    def eur(self):
        """Возвращает курс евро на сегодня в формате self.format_"""

        currency_obj = self.make_format(self.EURO_CHAR_CODE)

        if self.format_ == self.SELF_FORMAT_JUST_VALUE and self.diff:

            self.check_currency_rate_type(self.EURO_CHAR_CODE, currency_obj)
            return self.get_diff(self.EURO_CHAR_CODE, currency_obj)

        return currency_obj

    def usd(self):
        """Возвращает курс доллара на сегодня в формате self.format_"""

        currency_obj = self.make_format(self.DOLLAR_CHAR_CODE)

        if self.format_ == self.SELF_FORMAT_JUST_VALUE and self.diff:

            self.check_currency_rate_type(self.DOLLAR_CHAR_CODE, currency_obj)
            return self.get_diff(self.DOLLAR_CHAR_CODE, currency_obj)

        return currency_obj

    def AZN(self):
        """Возвращает курс азербайджанского маната на сегодня в формате self.format_"""
        return self.make_format('AZN')

    #
    def get_diff(self, currency_char_code: str, currency_obj: float) -> float:
        rate_delta = currency_obj - self.last_values[currency_char_code]
        self.last_values[currency_char_code] = currency_obj

        return rate_delta

    #
    def check_currency_rate_type(self, currency_char_code: str, currency_rate: float):
        if type(currency_rate) != float:
            raise Exception(f'Неверный тип данных у курса {currency_char_code}')
