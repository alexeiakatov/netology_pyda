from netology_pyda.homework_1_8_classes.task_1_and_2.IRateDiffPublishStrategy import IRateDiffPublishStrategy
from datetime import datetime


class DefaultRateDiffPublishStrategy(IRateDiffPublishStrategy):
    """
    Дефолтная стратегия публикации разницы курса валюты. Реазилует интерфейс IRateDiffPublishStrategy.
    Публикует разницу курса валюты в консоль.
    """

    #
    def publish(self, **params) -> None:
        currency_char_code = params['char_code']
        currency_rate_delta = params['rate_delta']
        now_ = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        print(f'{currency_char_code} : {now_} : {currency_rate_delta}')
