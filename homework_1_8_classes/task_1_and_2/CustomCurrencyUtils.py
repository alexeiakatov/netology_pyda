from netology_pyda.homework_1_8_classes.libs.Rate import Rate


class CustomCurrencyUtils(Rate):
    VALUE_KEY = 'Value'
    NAME_KEY = 'Name'
    CHAR_CODE_KEY = 'CharCode'

    #
    def __init__(self):
        # используем формат 'full' который поддерживает базовый класс
        super().__init__('full')

    #
    def get_sorted_by_rate(self, desc: bool) -> list:
        """
        Запрашивает данные о валютах у внешнего сервиса с помощью метода суперкласса.
        Возвращает список объект с информацией о различных валютах, отсортированный по значению курса валют.

        desc true - сортировать по убыванию, false - по возрастанию
        """

        all_currency_info = self.exchange_rates()
        self._validate_all_currency_info(all_currency_info)

        return self._sort_by_rate(all_currency_info, desc)

    #
    def get_currency_with_max_rate(self) -> dict:
        all_currency_info = self.exchange_rates()
        self._validate_all_currency_info(all_currency_info)

        return self._currency_with_max_rate(all_currency_info)

    #
    def get_currency_name_with_max_rate(self) -> str:
        all_currency_info = self.exchange_rates()
        self._validate_all_currency_info(all_currency_info)

        return self._currency_name_with_max_rate(all_currency_info)

    #
    def _validate_all_currency_info(self, all_currency_info: dict) -> None:

        if not isinstance(all_currency_info, dict):
            raise Exception('Метод сортировки валют должен получать объект dict')

        for currency_char_name, currency_info_obj in all_currency_info.items():
            if (not isinstance(currency_char_name, str)
                    or not isinstance(currency_info_obj, dict)
                    or self.VALUE_KEY not in currency_info_obj):
                raise Exception('Объект с данными валют должен иметь структуру: '
                                '{"currency_char_code": {"Value": float}, /* ... */}')

    #
    def _sort_by_rate(self, all_currency_info: dict, desc: bool) -> list:
        """
        Возвращает список объектов, содержащих информацию о валюте отсортированный по возрастанию или по убыванию
        значения Value.

        all_currency_info словарь со структурой '{"currency_char_code": {"Value": float}, /* ... */}')
        desc true - сортировать по убыванию, false - сортировать по возрастанию
        """

        return sorted(
            all_currency_info.values(),
            key=lambda currency: currency.get(self.VALUE_KEY, 0),
            reverse=desc)

    #
    def _currency_with_max_rate(self, all_currency_info: dict) -> dict:
        """
        Возвращает объект с данными о валюте у которой самое больше значение курса на момент запроса.

        all_currency_info словарь со структурой '{"currency_char_code": {"Value": float}, /* ... */}')
        """

        sorted_by_rate_desc = self._sort_by_rate(all_currency_info, True)

        if sorted_by_rate_desc is None or len(sorted_by_rate_desc) == 0:
            raise Exception('Передан пустой словарь с данными о валютах')

        return sorted_by_rate_desc[0]

    #
    def _currency_name_with_max_rate(self, all_currency_info: dict) -> str:
        """
        Возвращает название валюты у которой на момент запроса самое большое значение курса на момент запроса

        all_currency_info словарь со структурой '{"currency_char_code": {"Value": float}, /* ... */}')
        """

        currency_with_max_rate = self._currency_with_max_rate(all_currency_info)

        return currency_with_max_rate.get(self.NAME_KEY, '')
