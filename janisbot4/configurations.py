import os
import configparser

from janisbot4.singleton import Singleton

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))


class Configurations(metaclass=Singleton):
    parser = configparser.ConfigParser(
        interpolation=configparser.ExtendedInterpolation())

    observers = []

    def __init__(self, filepath):
        self.read(filepath)

    def read(self, filepath):
        self.parser.read(filepath)

    def get(self, setting, section='DEFAULT', default=None):
        return self.parser.get(section, setting, fallback=default)
