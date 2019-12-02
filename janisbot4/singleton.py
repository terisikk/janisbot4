import threading


class Singleton(type):
    _instances = {}
    lock = threading.Lock()

    def __call__(cls, *args, **kwargs):
        with cls.lock:
            if cls not in cls._instances:
                instance = super(Singleton, cls).__call__(*args, **kwargs)
                cls._instances[cls] = instance
        return cls._instances[cls]
