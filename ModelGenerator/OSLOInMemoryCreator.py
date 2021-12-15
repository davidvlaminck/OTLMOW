from ModelGenerator.Inheritance import Inheritance
from ModelGenerator.OSLOAttribuut import OSLOAttribuut
from ModelGenerator.OSLOClass import OSLOClass
from ModelGenerator.OSLODatatypePrimitive import OSLODatatypePrimitive
from ModelGenerator.OSLODatatypePrimitiveAttribuut import OSLODatatypePrimitiveAttribuut
from ModelGenerator.SQLDbReader import SQLDbReader


class OSLOInMemoryCreator:
    def __init__(self, sQLDbReader: SQLDbReader):
        self.sqlDbReader = sQLDbReader

    def getAllPrimitiveDatatypeAttributen(self):
        data = self.sqlDbReader.performReadQuery(
            "SELECT name, label_nl, definition_nl, class_uri, kardinaliteit_min, kardinaliteit_max, uri, type, overerving, "
            "constraints, readonly, usagenote_nl, deprecated_version FROM OSLODatatypePrimitiveAttributen",
            {})

        list = []
        for row in data:
            c = OSLODatatypePrimitiveAttribuut(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10], row[11], row[12])
            list.append(c)

        return list

    def getAllPrimitiveDatatypes(self):
        data = self.sqlDbReader.performReadQuery(
            "SELECT name, uri, definition_nl, label_nl, usagenote_nl, deprecated_version FROM OSLODatatypePrimitive",
            {})

        list = []
        for row in data:
            c = OSLODatatypePrimitive(row[0], row[1], row[2], row[3], row[4], row[5])
            list.append(c)

        return list

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

    def getInheritances(self):
        data = self.sqlDbReader.performReadQuery(
            "SELECT base_name, base_uri, class_uri, class_name, deprecated_version FROM InternalBaseClass",
            {})

        list = []
        for row in data:
            c = Inheritance(row[0], row[1], row[2], row[3], row[4])
            list.append(c)

        return list
