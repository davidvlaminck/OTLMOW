import unittest

from ModelGenerator.OSLOClass import OSLOClass
from ModelGenerator.SQLReader import SQLReader


class SQLReaderTests(unittest.TestCase):
    def test_FileNotFound(self):
        fileLocation = ''
        sqlReader = SQLReader(fileLocation)
        self.assertRaises(FileNotFoundError, sqlReader.getAllClasses)

    def test_GetAtLeastOneOSLOClassWithGetAllClasses(self):
        fileLocation = '../InputFiles/OTL.db'
        sqlReader = SQLReader(fileLocation)
        listOfClasses = sqlReader.getAllClasses()

        self.assertTrue(len(listOfClasses) > 0)
        first = next(c for c in listOfClasses)
        self.assertEqual(type(first), OSLOClass)

    def test_GetOneOSLOClassWithgetClassByUri(self):
        fileLocation = '../InputFiles/OTL.db'
        sqlReader = SQLReader(fileLocation)
        uri = 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#AansluitendeConstructie'
        listOfClasses = sqlReader.getClassByUri(uri)

        self.assertTrue(len(listOfClasses) == 1)
        first = next(c for c in listOfClasses)
        self.assertEqual(type(first), OSLOClass)
        self.assertEqual(first.uri, uri)


