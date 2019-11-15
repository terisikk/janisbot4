import configparser
from singleton import Singleton
from itertools import filterfalse
import os

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))


class Configurations(metaclass=Singleton):
    parser = configparser.ConfigParser(
        interpolation=configparser.ExtendedInterpolation())

    observers = []

    def __init__(self, filepath):
        self.read(filepath)
        return

    def register_observer(self, observer):
        self.observers.append(observer)
        return

    def notify_observers(self):
        error = False
        for observer in self.observers:
            try:
                observer._on_configurations_changed()
            except (AttributeError, TypeError) as e:
                observer = None
                error = True
                print("Error in notify_observers: ", e)  # TODO: logging
        if error:
            self. _clean_failed_observers()

    def _clean_failed_observers(self):
        self.observers[:] = list(filterfalse(
            lambda item: item is not None, self.observers))
        return

    def read(self, filepath):
        self.parser.read(filepath)
        return

    def sections(self):
        return self.parser.sections()

    def get(self, setting, section='DEFAULT', default=None):
        return self.parser.get(section, setting, fallback=default)

    def set(self, section, setting, value):
        self.parser.set(section, setting, value)
        return
