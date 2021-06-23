"""
Project Hulkster
 Made with Qt for Python, licensed under LGPL v3
 QtforPy5 Documentation: https://doc.qt.io/qtforpython-5/index.html
 QML doc
 This Python file uses the following encoding: utf-8
"""

import sys


from swerve.core import application, logger, paths, pyside, swerveos
from swerve.database import dbextractor, dbpassword
from swerve.database.gds import gds

from PySide2 import QtQml
from PySide2.QtCore import QStandardPaths


def main():
    app = application.app_instance()
    engine = application.app_engine()
    # extractor = dbextractor.Extractor()
    # gds_ = gds.GDS()
    QtQml.qmlRegisterType(dbextractor.Extractor, "Hulkster", 1, 0, "Extractor")
    # engine.rootContext().setContextProperty("saves", gds_.data)
    engine.load(application.app_ui_file())
    if not engine.rootObjects():
        input("Error occurred")
        logger.info("main", "Couldn't load ui file")
        sys.exit(-1)
    logger.info("main", "Application Launched!")
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
