from netology_pyda.homework_1_8_classes.libs.Rate import Rate
from datetime import datetime
import time
from netology_pyda.homework_1_8_classes.task_1_and_2.DefaultRateDiffPublishStrategy import DefaultRateDiffPublishStrategy
from netology_pyda.homework_1_8_classes.task_1_and_2.IRateDiffPublishStrategy import IRateDiffPublishStrategy


class RateDiffMonitor(Rate):
    """
    Расширяет класс Rate для реализации возможности в реальном времени отслеживать изменения курса конкретной валюты.
    Предполагается, что курс может достаточно часто изменяться на небольшие значения. Поэтому объект сохраняет предыдущий
    результат и на основании него вычисляет разницу с текущим курсом.

    Вариант использования: создаются несколько объектов RateDiffMonitor (каждый в отдельном потоке выполнения).
    Каждый такой объект в реальном времени следит за разницей курса какой-то конкретной валюты. С помощью требуемой
    реалзиации publisher, например, они могут отправлять значение разницы на развернутый веб сервер, где будет
    происходить сбор, анализ и обработка разниц курса.
    """

    _last_value = None

    _update_period = None
    _stop_monitor_flag = False
    _monitor_currency_char_code = None

    _rate_diff_publish_strategy = None

    #
    def __init__(
            self,
            monitor_currency_char_code: str,
            update_period: int = 60,
            publisher: IRateDiffPublishStrategy = DefaultRateDiffPublishStrategy()):
        """
        update_period - интервал между запросами курса валюты. По умолчанию делается 1 запрос в минуту.
        monitor_currency - передает char_code валюты, изменения курса которой нужно отслеживать.
        publisher - объект, выполняющий публикацию изменения курса валют в процессе работы монитора. Объект должен
        реализовать интерфейс IRateDiffPublishStrategy. По умолчанию используется реализация - DefaultRateDiffPublishStrategy.

        Для работы монитора явно устанавливаем нужные нам параметры в базовом классе с помощью super().__init__(...)
        """

        super().__init__(format_='value', diff=False)

        if monitor_currency_char_code is None:
            raise Exception('Монитору нужно передать char_code той валюты, курс которой он будет отслеживать. ')

        self._monitor_currency_char_code = monitor_currency_char_code
        self._rate_diff_publish_strategy = publisher
        self._update_period = update_period

    #
    def run_monitor(self) -> None:
        """
        Запускает монитор. Который в реальном времени отслеживает курс валюты, установленной при инициализации объект.
        Запрос делается в соответствии с периодом обновления, установленном при инициализации объекта.
        Получение текущего курса делается с помощью методов базового класса.
        Разница вычисляется как результат предыдущего запроса минус результат текущего запроса.
        Начальное значение последнего сохраненного курса = None (инициализируется при создании объекта). Поэтому первая
        разница всегда будет равна None.
        Полученная разница передается объекту-публикатору.
        """

        start_monitor_datetime = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        print(f'Монитор запущен: {start_monitor_datetime}')

        while not self._stop_monitor_flag:
            time.sleep(self._update_period)

            rate_delta = self._get_diff()
            char_code = self._monitor_currency_char_code

            self._rate_diff_publish_strategy.publish(char_code=char_code, rate_delta=rate_delta)

    #
    def _get_diff(self) -> 'float | None':
        """
        Запрашивает текущее значение курса отслеживаемой валюты с помощью методов базового класса. Проверяет валидность
        типа полученного значения. Если тип валидный, то пытается вычислить разницу текущего курса и предыдущего,
        который хранится в поле _last_value. После этого сохраняет текущий курс в это поле. Если это было = None, то не
        делает вычисления, а просто сохраняет в него текущий полученный курс.
        """
        currency_value = super().make_format(self._monitor_currency_char_code)
        self._check_currency_rate_type(self._monitor_currency_char_code, currency_value)

        if self._last_value is None:
            self._last_value = currency_value
            return None

        rate_delta = currency_value - self._last_value
        self._last_value = currency_value

        return rate_delta

    #
    def _check_currency_rate_type(self, currency_char_code: str, currency_rate: float):
        """
        Проверяет тип полученного значения курса валюты. Генерирует исключение, если тип не float.
        """
        if type(currency_rate) != float:
            raise Exception(f'Неверный тип данных у курса {currency_char_code}. Для корректной работы д.б. float.')
