import os
import sqlite3

from ModelGenerator.OSLOClass import OSLOClass


class SQLReader:
    def __init__(self, path):
        self.path = path

    def performReadQuery(self, query: str, params: dict):
        if not(os.path.isfile(self.path)):
            raise FileNotFoundError()

        con = sqlite3.connect(self.path)
        cur = con.cursor()
        data = []
        for row in cur.execute(query, params):
            data.append(row)
        con.close()
        return data

    def getAllClasses(self):
        emptyDict = {}
        data = self.performReadQuery("SELECT label_nl, name, uri, definition_nl, usagenote_nl, abstract, deprecated_version FROM OSLOClass", emptyDict)

        list = []
        for row in data:
            c = OSLOClass(row[0], row[1], row[2], row[3], row[4], row[5], row[6])
            list.append(c)

        return list

    def getClassByUri(self, class_uri: str):
        data = self.performReadQuery("SELECT label_nl, name, uri, definition_nl, usagenote_nl, abstract, deprecated_version FROM OSLOClass where uri=:uriclass",
                                     {"uriclass": 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#AansluitendeConstructie'})

        list = []
        for row in data:
            c = OSLOClass(row[0], row[1], row[2], row[3], row[4], row[5], row[6])
            list.append(c)

        return list