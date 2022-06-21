import sys
from os.path import abspath, dirname, normpath


PREFIX = normpath(dirname(dirname(abspath(__file__))))
if PREFIX not in sys.path:
    sys.path = [PREFIX] + sys.path
