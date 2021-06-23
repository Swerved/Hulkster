"""
Database Drivers

Requires PySide2 plugins for sqldrivers:

SQLite --> QSQLITE --> qsqlite.dll
ODBC (Access Databases) --> QODBC --> qodbc.dll
Cipher (SQLite, password protected for PWP) --> SQLITECIPHER --> sqlitecipher.dll

More supported: https://doc.qt.io/qtforpython-5/overviews/sql-driver.html#sql-database-drivers

"""

from PySide2.QtCore import QStandardPaths
from Hulkster.swerve.core import paths, swerveos
from Hulkster.swerve.database import dbpassword
from Hulkster.swerve.database.gds import gdspassword
from shutil import copyfile

odbc = "QODBC"
sqlite = "QSQLITE"
cipher = "SQLITECIPHER"
hostname = "localhost"
accessdsn = "DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};FIL={MS Access};DBQ="

"""
Database Driver Connect Options

More Options: https://doc.qt.io/qt-5/qsqldatabase.html#setConnectOptions

"""
# Used for TEW Databases to allow read and write access
optionmdb: str = "SQL_ATTR_ACCESS_MODE=SQL_MODE_READ_WRITE"
# For Sqlite Databases, enable regex in queries
optionregex: str = "QSQLITE_ENABLE_REGEXP"


def type(file):
    if ".mdb" in file:
        return odbc
    if ".db" in file:
        return sqlite
    return cipher


def username(file):
    if ".mdb" in file:
        return "Admin"
    return ""


def dsn(file, id):
    ext = swerveos.file_extension(file)
    to = paths.temp() + id + "." + ext
    if swerveos.exists(file):
        copyfile(file, to)
    if ".mdb" in file:
        return accessdsn + to
    return file


def options(file):
    if ".mdb" in file:
        return optionmdb
    return optionregex


def password(file):
    if ".mdb" in file:
        return gdspassword.get(file)
    if ".pwp" in file:
        return dbpassword.pwp()
    return ""


def extractable(file):
    types = [".db", ".mdb"]
    for type in types:
        if type in file:
            return True
    return False


def convertible(file):
    types = ["TEW2016.mdb"]
    for type in types:
        if type in file:
            return True
    return False
