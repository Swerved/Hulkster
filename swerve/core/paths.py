import os
from PySide2.QtCore import QStandardPaths, QDir
from Hulkster.swerve.core import application


def app_data():
    dir_ = QStandardPaths.writableLocation(QStandardPaths.AppDataLocation)
    return dir_


def temp():
    dir_ = QStandardPaths.writableLocation(QStandardPaths.TempLocation) + "\\" + application.app_name + "\\"
    return dir_


def logs():
    dir_ = temp() + "Logs\\"
    return dir_

def app_data_location_persistent():
    dir_ = app_data() + "/Persistent"
    return dir_

def app_data_location_persistent_data_dump():
    dir_ = app_data_location_persistent() + "/ExtractedDB"
    qdir = QDir()
    qdir.mkpath(dir_)
    return dir_
