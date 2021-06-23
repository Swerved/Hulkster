"""
swerveos.py

Some useful extensions and operations on import os and command line interface

"""


import os
import shutil
import re
from PySide2.QtGui import QDesktopServices

from datetime import datetime

from Hulkster.swerve.core import commandline


def is_bundled_app():
    """ Return True if cwd matches library file directory """
    lfd = os.path.dirname(__file__)
    cwd = os.getcwd()
    if lfd == cwd:
        return True
    else:
        return False


def date_time():
    """ Return Formatted Date Time """
    now = datetime.now()
    time = now.strftime("%d/%m/%Y %H:%M:%S")
    return time


def file_extension(file):
    """ Returns File Extension without trailing period."""
    filename_, file_extension_ = os.path.splitext(file)
    # ext
    return file_extension_[1:]


def filename(file, include_extension):
    """ Get the File Name including extension, or just the name of the file """
    if include_extension:
        # file.ext
        return os.path.basename(file)
    else:
        # file
        filename_, file_extension_ = os.path.splitext(file)
        return os.path.basename(filename_)


def is_console_app():
    """ Return True if --console specified """
    args = commandline.cli_arguments()
    if "--console" in args:
        return True
    return False

def regexContains(regex, value):
    contains = re.findall(regex, value)
    if contains:
        return True
    return False


def exists(file):
    ok = os.path.exists(file)
    return ok


def clean_folder(path):
    shutil.rmtree(path)
    os.mkdir(path)


def remove(file):
    """ Remove a file if it exists """
    if os.path.exists(file):
        print("Removing " + file + "...")
        os.remove(file)


def write(file, lines):
    """ Write file from an array """
    with open(file, 'w') as f:
        bytes_ = f.write('\n'.join(lines[0:]) + '\n')
        return bytes_


def open_local_file(file):
    path = "file:///" + file
    QDesktopServices.openUrl(path)