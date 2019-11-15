import threading


def singleton(theclass):
    instances = {}
    # theclass._shared_state = {}
    lock = threading.Lock()

    def get_instance(*args, **kwargs):
        with lock:
            if theclass not in instances:
                instances[theclass] = theclass(*args, **kwargs)
        return instances[theclass]
    return get_instance


class Singleton(type):
    _instances = {}
    lock = threading.Lock()

    def __call__(cls, *args, **kwargs):
        with cls.lock:
            if cls not in cls._instances:
                instance = super(Singleton, cls).__call__(*args, **kwargs)
                cls._instances[cls] = instance
        return cls._instances[cls]
