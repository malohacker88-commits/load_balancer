class BalancerCounter:
    """
    Singleton каунтера.

    По хорошему так как у нас может быть много инстансов приложения каунтер нужно перенести например в Redis
    Написать общий интерфейс каунтера и в настройках указывать какой использовать, синглтон, редис
    или что угодно другое с таким же интерфейсом
    """

    _instance = None

    def __init__(self, default_count=1):
        self.default_count = default_count
        self.count = default_count

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls, *args, **kwargs)
        return cls._instance

    def increment(self):
        """Увеличить счетчик"""
        self.count += 1

    def refresh(self):
        """Обнулить счетчик"""
        self.count = self.default_count


counter = BalancerCounter()
