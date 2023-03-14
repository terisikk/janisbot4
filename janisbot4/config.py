import os

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

# TODO: Refactor to just use os.environ directly
cfg = os.environ
