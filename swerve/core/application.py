# This Python file uses the following encoding: utf-8

# if __name__ == "__main__":
#     pass

import sys
import os

from PySide2.QtWidgets import QApplication
from PySide2.QtCore import QStandardPaths, QDir
from PySide2.QtGui import QIcon
from PySide2.QtQml import QQmlApplicationEngine

from Hulkster.swerve.core import pyside, assets, paths, swerveos

app_name = "Hulkster"
_engine = None


def app_instance():
    sys.argv += ['--style', 'material']
    app = QApplication(sys.argv)
    app.setApplicationName(app_name)
    icon = QIcon(assets.app_icon())
    app.setWindowIcon(icon)
    dir_ = QDir()
    dir_.mkpath(paths.temp())
    dir_.mkpath(paths.logs())
    return app


def app_engine():
    global _engine
    if _engine is None:
        _engine = QQmlApplicationEngine()
    return _engine


def app_ui_file():
    return os.getcwd() + "\\data\\ui\\main.qml"


def app_is_valid():
    ok = os.path.isfile(app_ui_file())
    return ok