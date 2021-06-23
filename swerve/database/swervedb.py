"""
Database class

"""

import os
from PySide2.QtSql import QSqlDatabase, QSqlQuery, QSqlRecord
from swerve.core import logger
from swerve.database import dbdriver
from swerve.database.gds import gdspassword


class Database:

    # session is used for the connection name of the database
    session = -1
    # track sessions and filepaths
    sessions = []
    files = []
    current_database = None
    second_database = None

    def __del__(self):
        for id in QSqlDatabase.connectionNames():
            db = QSqlDatabase.database(id)
            db.close()

    def db_print_info(self):
        db = QSqlDatabase.database(self.session)
        print("Database Information:")
        print("Connection Names:")
        print(QSqlDatabase.connectionNames())
        print("Hostname: " + db.hostName())
        print("Driver: " + db.driverName())
        print("Connection Name: " + db.connectionName())
        print("Connection Options: " + db.connectOptions())
        print("DSN: " + db.databaseName())
        print("Username: " + db.userName())
        print("Password: " + db.password())
        # print("Version: " + str(self.version))

    def db_id(self):
        self.session = len(QSqlDatabase.connectionNames()) + 1
        id_ = "ID" + str(self.session)
        return id_

    def db_open(self, file):
        dbid = self.db_id()
        db = QSqlDatabase.addDatabase(dbdriver.type(file), dbid)
        db.setHostName(dbdriver.hostname)
        db.setConnectOptions(dbdriver.options(file))
        db.setUserName(dbdriver.username(file))
        db.setPassword(dbdriver.password(file))
        filepath = dbdriver.dsn(file, dbid)
        db.setDatabaseName(filepath)
        ok = db.open()
        if ok:
            self.files.append(filepath)
            self.sessions.append(self.session)
            print("Database opened: " + filepath)
        else:
            message = "Unable to open database " + filepath
            print(message)
            logger.info("Database", message)
        self.current_database = db
        return db


# Shared instance of Database()
_database = None


def get():
    global _database
    if _database is None:
        _database = Database()
    return _database
