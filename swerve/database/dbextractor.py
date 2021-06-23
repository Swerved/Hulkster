# This Python file uses the following encoding: utf-8
# This file contains a QObject class for QML. Therefore function names do not follow PEP 8 standard.
import threading
import time
from PySide2.QtCore import QObject, Slot, QThread, Signal, QElapsedTimer, Property, QRegExp
from PySide2.QtSql import QSqlDatabase, QSqlQuery, QSqlRecord
from swerve.core import commandline, qml, swerveos, paths
from swerve.database import swervedb
from swerve.database.gds import gds


class Extractor(QObject, metaclass=qml.PropertyMeta):

    type = "all"
    """ Type 
    Type define what tables are extracted
    Type is all by default
    Can be set as a command line argument via --type
    """

    version = 0


    def __init__(self):
        super().__init__()
        arg = commandline.cli_get_value_for_argument("type")
        gds_ = gds.GDS()
        self.data = gds_.files
        self._model = gds_.data
        self._busy = False
        self._progress = 0
        self.worker = Process()
        self.worker.updateProgress.connect(self.setProgress)
        if arg is not None:
            self.type = arg

    @Slot()
    def close(self):
        # TODO: app cleanup
        print("Extractor deleted")

    @Signal
    def modelChanged(self):
        pass

    def getModel(self):
        return self._model

    def setModel(self, model):
        self._model = model

    model = Property(list, getModel, setModel, notify=modelChanged)

    @Signal
    def busyChanged(self):
        pass

    def getBusy(self):
        return self._busy

    def setBusy(self, busy):
        self._busy = busy

    busy = Property(int, getBusy, setBusy, notify=busyChanged)

    @Signal
    def progressChanged(self):
        pass

    def getProgress(self):
        return self._progress

    def setProgress(self, progress):
        self._progress = progress / 100
        self.progressChanged.emit()
        if self._progress == 1.0:
            self.setBusy(False)
            self.busyChanged.emit()
            self._progress = 0
            self.progressChanged.emit()
            swerveos.open_local_file(paths.app_data_location_persistent_data_dump())

    progress = Property(float, getProgress, setProgress, notify=progressChanged)


    @Slot(result=str)
    def extractorVersion(self):
        return "1.0"

    @Slot(int)
    def extract(self, index):
        self.worker.file = self.data[index]
        self.busy = True
        self.busyChanged.emit()
        self.worker.start()


class Process(QThread):
    updateProgress = Signal(int)
    updateStatus = Signal(str)
    database = None
    importsql = []
    file = None
    version = None
    tables = None

    def __init__(self):
        QThread.__init__(self)
        self.timer = QElapsedTimer()
        self.database = swervedb.get()
        self.schema = gds.get_import_schema()
        self._value = 0

    def getVersion(self):
        if "TEW2013" in self.file:
            return 13
        if "TEW2016" in self.file:
            return 16
        if "TEW2020" in self.file:
            return 20

    def isValid(self):
        versions = [13, 16, 20]
        if self.version in versions:
            return True
        return False

    def getTables(self):
        tables = gds.get_extraction_tables(self.version)
        return tables

    def progress(self, value):
        self.updateProgress.emit(value)

    def status(self, value):
        self.updateStatus.emit(value)
        print(value)

    def example(self):
        self.timer.start()
        # self.updateStatus("Extracting, please wait...")
        for i in range(1, 101):
            #Emit the signal so it can be received on the UI side.
            self.updateProgress.emit(i)
            self.msleep(10)
        print("Finished: "+str(self.timer.elapsed()))

    def combined(self):
        self.timer.start()
        exists = swerveos.exists(paths.app_data_location_persistent_data_dump() + "/audit.txt")
        if exists:
            swerveos.clean_folder(paths.app_data_location_persistent_data_dump())
        self.version = self.getVersion()
        if not self.isValid():
            return
        self.tables = self.getTables()
        steps = len(self.tables) + 140
        increment = 100 / steps
        self.status("Extracting, please wait... ")
        self.database.db_open(self.file)
        filename = paths.app_data_location_persistent_data_dump() + "/extractor.csv"
        data = [str(self.version)]
        self.status("Writing to Extractor " + filename)
        step = 1
        swerveos.write(filename, data)
        self.progress(increment * step)
        extraction = QSqlQuery(self.database.current_database)
        filename = paths.app_data_location_persistent_data_dump() + "/script.txt"
        stream = []
        for table in self.tables:
            step += 1
            self.progress(increment * step)
            self.status("Reading table " + table)
            data.clear()
            extraction.exec_("SELECT * FROM "+table)
            current_table = table.replace("tbl", "")
            tbl = table.replace("tbl", "imported_")
            tablefile = paths.app_data_location_persistent_data_dump() + "/" + table + ".csv"
            tablefilestream = []
            self.status("Exporting " + table)
            # Exporting tbl
            record_id = 1
            comma = ","
            while extraction.next():
                position = extraction.at()
                record = QSqlRecord(extraction.record())
                fieldnames = []
                tablefilefields = []
                columns = record.count()
                row = []
                tablefilerow = []
                if position == 0:
                    for field in range(0, columns):
                        fieldnames.append(record.fieldName(field))
                    fields = "(" + comma.join(fieldnames) + ")"
                    tablefilefields = comma.join(fieldnames)
                for field in range(0, columns):
                    value = str(extraction.value(field))
                    csv = value
                    alpha = swerveos.regexContains("[a-z]", value)
                    alphacaps = swerveos.regexContains("[A-Z]", value)
                    numbers = swerveos.regexContains("[0-9]", value)
                    whitespace = swerveos.regexContains("[a-z]", value)
                    if whitespace and not alpha and not alphacaps:
                        value = ""
                    if alpha or alphacaps:
                        value = value.replace(",", ";;")
                        value = value.replace("'", "''")
                        value = value.replace("\"", "::")
                        value = value.replace("\n", " ")
                        value = value.replace("\r", " ")
                        value = "'" + value + "'"
                    else:
                        value = value.replace(".", "")
                        if value.startswith("-"):
                            value = value.replace("-", "0 - ")
                    if field == 0:
                        row.append("INSERT INTO ")
                        row.append(tbl)
                        row.append(fields)
                        row.append(" VALUES(")
                        if ("Generate" in table) or ("CV" in table) or ("EraProduct" in table):
                            row.append(str(record_id))
                            tablefilerow.append(str(record_id))
                            record_id += 1
                            row.append(",")
                            tablefilerow.append(",")
                        if position == 0:
                            tablefilerow.append(tablefilefields)
                            tablefilerow.append("\n")
                    row.append(value)
                    tablefilerow.append(csv)
                    if field < columns - 1:
                        row.append(",")
                        tablefilerow.append(",")
                    else:
                        row.append(");")
                stream.append("".join(row))
                tablefilestream.append("".join(tablefilerow))
                swerveos.write(tablefile, tablefilestream)
        swerveos.write(filename, stream)
        extraction.clear()
        debug = commandline.cli_has_argument("debug=True")
        if debug:
            audit_query = QSqlQuery(self.database.current_database)
            filename = paths.app_data_location_persistent_data_dump() + "/audit.txt"
            stream = []
            for table in self.tables:
                self.status("Auditing " + table)
                audit_query.exec_("SELECT count(*) FROM " + table)
                while audit_query.next():
                    result = table
                    result += "',"
                    result += str(audit_query.value(0))
                    result += ")"
                    result = "INSERT INTO _audit (org_table, org_count) VALUES('" + result + "\n"
                    stream.append(result)
                audit_query.clear()
            self.status("Writing to audit " + filename)
            swerveos.write(filename, stream)
        self.database.current_database.close()
        step += 1
        self.progress(increment * step)
        self.database.db_open(paths.app_data_location_persistent_data_dump() + "/exported.db")
        self.status("Creating database... ")
        for sql in self.schema:
            insert = QSqlQuery(self.database.current_database)
            insert.exec_(sql)
        step += 1
        self.progress(increment * step)
        ## Increment progress at each percent of the conversion script
        ## This takes a while
        streamsteps = int(len(stream) / 100)
        streamstep = 0
        for sql in stream:
            index = stream.index(sql)
            insert = QSqlQuery(self.database.current_database)
            self.status("Importing record " + str(index) + " of " + str(len(stream)))
            insert.exec_(sql)
            streamstep += 1
            if streamstep == streamsteps:
                step += 1
                self.progress(increment * step)
                streamstep = 0
        self.database.current_database.close()
        print("Finished: "+str(self.timer.elapsed()))
        self.progress(100)

    def run(self):
        self.combined()
