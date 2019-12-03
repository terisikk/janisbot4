import os
import json

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

cfg = {}

with open(os.environ.get('JANISBOT_CONFIG')) as f:
    cfg = json.loads(f.read())
