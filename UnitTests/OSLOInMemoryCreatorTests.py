import unittest
from unittest.mock import Mock

from ModelGenerator.FileExistChecker import FileExistChecker
from ModelGenerator.Inheritance import Inheritance
from ModelGenerator.OSLOAttribuut import OSLOAttribuut
from ModelGenerator.OSLOClass import OSLOClass
from ModelGenerator.OSLOInMemoryCreator import OSLOInMemoryCreator
from ModelGenerator.SQLDbReader import SQLDbReader


class OSLOInMemoryCreatorTests(unittest.TestCase):
    def mockPerformReadQuery(self, query, arg_dict):
        if query == 'SELECT label_nl, name, typeURI, definition_nl, usagenote_nl, abstract, deprecated_version FROM OSLOClass where typeURI=:uriclass' \
                and arg_dict['uriclass'] == 'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#NaampadObject':
            return [['Naampad object', 'NaampadObject',
                     'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#NaampadObject'
                        , 'Abstracte als de basisklasse voor elk OTL object dat gebruik maakt van een naampad.', '', 1, '']]
        elif query == 'SELECT label_nl, name, typeURI, definition_nl, usagenote_nl, abstract, deprecated_version FROM OSLOClass' and arg_dict == {}:
            return [['Naampad object', 'NaampadObject',
                     'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#NaampadObject'
                        , 'Abstracte als de basisklasse voor elk OTL object dat gebruik maakt van een naampad.', '', 1, '']]
        elif query == 'SELECT name, label_nl, definition_nl, class_uri, kardinaliteit_min, kardinaliteit_max, typeURI, type, ' \
                      'overerving, constraints, readonly, usagenote_nl, deprecated_version FROM OSLOAttributen WHERE ' \
                      'class_uri=:uriclass AND overerving = 0' \
                and arg_dict[
            'uriclass'] == 'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#NaampadObject':
            return [[
                'naampad', 'naampad',
                'Een set van objecten (bv. collecties) die aanduiden waar het object zich bevindt in de objectenboom (EM-Infra).'
                , 'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#NaampadObject', '1', '1',
                'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#NaampadObject.naampad',
                'http://www.w3.org/2001/XMLSchema#string', 0, '', 0, '', ''
            ]]
        elif query == 'SELECT name, label_nl, definition_nl, class_uri, kardinaliteit_min, kardinaliteit_max, typeURI, type, ' \
                      'overerving, constraints, readonly, usagenote_nl, deprecated_version FROM OSLOAttributen WHERE ' \
                      'overerving = 0' and arg_dict == {}:
            return [[
                'naampad', 'naampad',
                'Een set van objecten (bv. collecties) die aanduiden waar het object zich bevindt in de objectenboom (EM-Infra).'
                , 'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#NaampadObject', '1', '1',
                'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#NaampadObject.naampad',
                'http://www.w3.org/2001/XMLSchema#string', 0, '', 0, '', ''
            ]]
        elif query == "SELECT base_name, base_uri, class_uri, class_name, deprecated_version FROM InternalBaseClass" and arg_dict == {}:
            return [['AIMNaamObject', "https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#AIMNaamObject",
                     "https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#NaampadObject", "NaampadObject", ""]]
        return []

    def test_FileNotFound(self):
        file_location = ''
        file_exist_checker = FileExistChecker(file_location)
        sql_reader = SQLDbReader(file_exist_checker)
        oslo_creator = OSLOInMemoryCreator(sql_reader)
        self.assertRaises(FileNotFoundError, oslo_creator.getAllClasses)

    def test_OTLDbClass(self):
        file_location = '../InputFiles/OTL.db'
        file_exist_checker = FileExistChecker(file_location)
        sql_reader = SQLDbReader(file_exist_checker)
        oslo_creator = OSLOInMemoryCreator(sql_reader)
        listOfClasses = oslo_creator.getAllClasses()

        self.assertTrue(len(listOfClasses) > 0)
        first = next(c for c in listOfClasses)
        self.assertEqual(type(first), OSLOClass)

    def test_Mock_getAllClasses(self):
        mock = Mock()
        oSLOCreator = OSLOInMemoryCreator(mock)
        mock.performReadQuery = self.mockPerformReadQuery
        uri = 'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#NaampadObject'
        listOfClasses = oSLOCreator.getAllClasses()

        self.assertTrue(len(listOfClasses) >= 1)
        first = next(c for c in listOfClasses)
        self.assertEqual(type(first), OSLOClass)
        self.assertEqual(first.typeURI, uri)

    def test_Mock_getClassByUri(self):
        mock = Mock()
        oSLOCreator = OSLOInMemoryCreator(mock)
        mock.performReadQuery = self.mockPerformReadQuery
        uri = 'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#NaampadObject'
        listOfClasses = oSLOCreator.getClassByUri(uri)

        self.assertTrue(len(listOfClasses) == 1)
        first = next(c for c in listOfClasses)
        self.assertEqual(type(first), OSLOClass)
        self.assertEqual(first.typeURI, uri)

    def test_Mock_getAttributeByClassUri(self):
        mock = Mock()
        oSLOCreator = OSLOInMemoryCreator(mock)
        mock.performReadQuery = self.mockPerformReadQuery
        uri = 'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#NaampadObject'
        attributeUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#NaampadObject.naampad'
        listOfAttributes = oSLOCreator.getAttributeByClassUri(uri)

        self.assertTrue(len(listOfAttributes) == 1)
        first = next(c for c in listOfAttributes)
        self.assertEqual(type(first), OSLOAttribuut)
        self.assertEqual(first.typeURI, attributeUri)

    def test_Mock_getAttributes(self):
        mock = Mock()
        oSLOCreator = OSLOInMemoryCreator(mock)
        mock.performReadQuery = self.mockPerformReadQuery
        attributeUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#NaampadObject.naampad'
        listOfAttributes = oSLOCreator.getAttributes()

        self.assertTrue(len(listOfAttributes) >= 1)
        first = next(c for c in listOfAttributes)
        self.assertEqual(type(first), OSLOAttribuut)
        self.assertEqual(first.typeURI, attributeUri)

    def test_Mock_getInheritances(self):
        mock = Mock()
        oSLOCreator = OSLOInMemoryCreator(mock)
        mock.performReadQuery = self.mockPerformReadQuery
        listOfInheritances = oSLOCreator.getInheritances()
        class_uri = 'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#NaampadObject'

        self.assertTrue(len(listOfInheritances) >= 1)
        first = next(c for c in listOfInheritances)
        self.assertEqual(type(first), Inheritance)
        self.assertEqual(first.class_uri, class_uri)
