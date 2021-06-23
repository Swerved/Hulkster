import os
import PySide2


def pyside_path():
    """ Return Path to Pyside Lib"""
    return print(os.path.dirname(PySide2.__file__))
