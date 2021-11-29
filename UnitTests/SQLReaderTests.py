import os
import sqlite3
import unittest

from ModelGenerator.OSLOClass import OSLOClass


class SQLReader:
    def __init__(self, path):
        self.path = path

    def getClasses(self):
        if not(os.path.isfile(self.path)):
            raise FileNotFoundError()

        con = sqlite3.connect(self.path)
        cur = con.cursor()
        list = []
        for row in cur.execute(
                "SELECT label_nl, name, uri, definition_nl, usagenote_nl, abstract, deprecated_version FROM OSLOClass where uri=:uriclass",
                {"uriclass": 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#AansluitendeConstructie'}):
            c = OSLOClass(row[0], row[1], row[2], row[3], row[4], row[5], row[6])
            list.append(c)
        con.close()
        return list


class SQLReaderTests(unittest.TestCase):
    def test_FileNotFound(self):
        fileLocation = ''
        sqlReader = SQLReader(fileLocation)
        self.assertRaises(FileNotFoundError, sqlReader.getClasses)

    def test_GetAtLeastOneOSLOClass(self):
        fileLocation = '../InputFiles/OTL.db'
        sqlReader = SQLReader(fileLocation)
        listOfClasses = sqlReader.getClasses()

        self.assertTrue(len(listOfClasses) > 0)
        first = next(c for c in listOfClasses)
        self.assertEqual(type(first), OSLOClass)

