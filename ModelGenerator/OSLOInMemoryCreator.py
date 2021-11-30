from ModelGenerator.OSLOAttribuut import OSLOAttribuut
from ModelGenerator.OSLOClass import OSLOClass
from ModelGenerator.SQLDbReader import SQLDbReader


class OSLOInMemoryCreator:
    def __init__(self, SQLDbReader: SQLDbReader):
        self.sqlDbReader = SQLDbReader

    def getAllClasses(self):
        data = self.sqlDbReader.performReadQuery(
            "SELECT label_nl, name, uri, definition_nl, usagenote_nl, abstract, deprecated_version FROM OSLOClass",
            {})

        list = []
        for row in data:
            c = OSLOClass(row[0], row[1], row[2], row[3], row[4], row[5], row[6])
            list.append(c)

        return list

    def getClassByUri(self, class_uri: str):
        data = self.sqlDbReader.performReadQuery(
            "SELECT label_nl, name, uri, definition_nl, usagenote_nl, abstract, deprecated_version FROM OSLOClass where uri=:uriclass",
            {"uriclass": class_uri})

        list = []
        for row in data:
            c = OSLOClass(row[0], row[1], row[2], row[3], row[4], row[5], row[6])
            list.append(c)

        return list

    def getAttributeByClassUri(self, class_uri):
        data = self.sqlDbReader.performReadQuery(
            "SELECT name, label_nl, definition_nl, class_uri, kardinaliteit_min, kardinaliteit_max, uri, type, overerving, constraints, readonly, usagenote_nl, deprecated_version FROM OSLOAttributen WHERE class_uri=:uriclass AND overerving = 0",
            {"uriclass": class_uri})

        list = []
        for row in data:
            c = OSLOAttribuut(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10],
                              row[11], row[12])
            list.append(c)

        return list

    def getAttributes(self):
        data = self.sqlDbReader.performReadQuery(
            "SELECT name, label_nl, definition_nl, class_uri, kardinaliteit_min, kardinaliteit_max, uri, type, overerving, constraints, readonly, usagenote_nl, deprecated_version FROM OSLOAttributen WHERE overerving = 0",
            {})

        list = []
        for row in data:
            c = OSLOAttribuut(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10],
                              row[11], row[12])
            list.append(c)

        return list
