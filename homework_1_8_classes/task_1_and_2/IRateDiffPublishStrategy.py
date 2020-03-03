
class IRateDiffPublishStrategy:
    """
    Интерфейс стратегии, выполняющей публикацию разницы курса валюты. Наследники должны реализовывать метод publish(**params)
    """

    #
    def publish(self, **params):
        pass
