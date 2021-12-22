import unittest
from unittest.mock import Mock

from ModelGenerator.FileExistChecker import FileExistChecker
from ModelGenerator.Inheritance import Inheritance
from ModelGenerator.OSLOAttribuut import OSLOAttribuut
from ModelGenerator.OSLOClass import OSLOClass
from ModelGenerator.OSLODatatypeComplex import OSLODatatypeComplex
from ModelGenerator.OSLODatatypeComplexAttribuut import OSLODatatypeComplexAttribuut
from ModelGenerator.OSLODatatypePrimitive import OSLODatatypePrimitive
from ModelGenerator.OSLODatatypePrimitiveAttribuut import OSLODatatypePrimitiveAttribuut
from ModelGenerator.OSLOEnumeration import OSLOEnumeration
from ModelGenerator.OSLOInMemoryCreator import OSLOInMemoryCreator
from ModelGenerator.SQLDbReader import SQLDbReader


class OSLOInMemoryCreatorTests(unittest.TestCase):
    def mockPerformReadQuery(self, query, arg_dict):
        if query == 'SELECT label_nl, name, uri, definition_nl, usagenote_nl, abstract, deprecated_version FROM OSLOClass where uri=:uriclass' \
                and arg_dict['uriclass'] == 'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#NaampadObject':
            return [['Naampad object', 'NaampadObject',
                     'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#NaampadObject'
                        , 'Abstracte als de basisklasse voor elk OTL object dat gebruik maakt van een naampad.', '', 1, '']]
        elif query == 'SELECT label_nl, name, uri, definition_nl, usagenote_nl, abstract, deprecated_version FROM OSLOClass' and arg_dict == {}:
            return [['Naampad object', 'NaampadObject',
                     'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#NaampadObject'
                        , 'Abstracte als de basisklasse voor elk OTL object dat gebruik maakt van een naampad.', '', 1, '']]
        elif query == 'SELECT name, label_nl, definition_nl, class_uri, kardinaliteit_min, kardinaliteit_max, uri, fieldType, ' \
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
        elif query == 'SELECT name, label_nl, definition_nl, class_uri, kardinaliteit_min, kardinaliteit_max, uri, fieldType, ' \
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
        elif query == "SELECT name, uri, definition_nl, label_nl, usagenote_nl, deprecated_version FROM OSLODatatypePrimitive" and arg_dict == {}:
            return [["DteKleurRAL", "https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DteKleurRAL",
                     "Beschrijft een kleur volgens het RAL classificatiesysteem. De waarde is een natuurlijk getal tussen 1000 en 9999.",
                     "RAL-kleur", "", ""],
                    ["KwantWrdInWatt", "https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#KwantWrdInWatt",
                     "Een kwantitatieve waarde die een getal in watt uitdrukt.", "Kwantitatieve waarde in watt", "", ""],
                    ["Time", "http://www.w3.org/2001/XMLSchema#time",
                     "Beschrijft een tijd volgens http://www.w3.org/2001/XMLSchema#time.", "Tijd",
                     "https://www.w3.org/TR/xmlschema-2/#time", ""],
                    ["Date", "http://www.w3.org/2001/XMLSchema#date",
                     "Beschrijft een datum volgens http://www.w3.org/2001/XMLSchema#date.", "Datum",
                     "https://www.w3.org/TR/xmlschema-2/#date", ""],
                    ["NonNegativeInteger", "http://www.w3.org/2001/XMLSchema#nonNegativeInteger",
                     "Beschrijft een natuurlijk getal volgens http://www.w3.org/2001/XMLSchema#nonNegativeInteger.",
                     "Natuurlijk getal", "https://www.w3.org/TR/xmlschema-2/#nonNegativeInteger", ""],
                    ["AnyURI", "http://www.w3.org/2001/XMLSchema#anyURI",
                     "Een tekstwaarde die een verwijzing naar meer informatie van het element bevat volgens http://www.w3.org/2001/XMLSchema#anyURI .",
                     "URI", "https://www.w3.org/TR/xmlschema-2/#anyURI", ""],
                    ["String", "http://www.w3.org/2001/XMLSchema#string",
                     "Beschrijft een tekstregel volgens http://www.w3.org/2001/XMLSchema#string.", "String",
                     "https://www.w3.org/TR/xmlschema-2/#string", ""],
                    ["Boolean", "http://www.w3.org/2001/XMLSchema#boolean",
                     "Beschrijft een boolean volgens http://www.w3.org/2001/XMLSchema#boolean.", "Boolean",
                     "https://www.w3.org/TR/xmlschema-2/#boolean", ""],
                    ["Literal", "http://www.w3.org/2000/01/rdf-schema#Literal", "Beschrijft een constante.", "Literal",
                     "http://www.w3.org/2000/01/rdf-schema#Literal", ""],
                    ["DateTime", "http://www.w3.org/2001/XMLSchema#dateTime",
                     "Beschrijft een datumtijd volgens http://www.w3.org/2001/XMLSchema#dateTime.", "Datumtijd",
                     "https://www.w3.org/TR/xmlschema-2/#dateTime", ""],
                    ["Integer", "http://www.w3.org/2001/XMLSchema#integer",
                     "Beschrijft een geheel getal volgens http://www.w3.org/2001/XMLSchema#integer.", "Geheel getal",
                     "https://www.w3.org/TR/xmlschema-2/#integer", ""],
                    ["Decimal", "http://www.w3.org/2001/XMLSchema#decimal",
                     "Beschrijft een decimaal getal volgens http://www.w3.org/2001/XMLSchema#decimal.", "Decimaal getal",
                     "https://www.w3.org/TR/xmlschema-2/#decimal", ""]]
        elif query == "SELECT name, label_nl, definition_nl, class_uri, kardinaliteit_min, kardinaliteit_max, uri, fieldType, overerving, constraints, readonly, usagenote_nl, deprecated_version FROM OSLOAttributen" and arg_dict == {}:
            return [["waarde", "waarde", "Beschrijft een kleur volgens het RAL classificatiesysteem.",
                     "https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DteKleurRAL", "1", "1",
                     "https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DteKleurRAL.waarde",
                     "http://www.w3.org/2001/XMLSchema#string", "0", "", "0",
                     "De waarde moet voldoen aan volgende regex: [1-9]\d{3}", ""],
                    ["standaardEenheid", "standaard eenheid", "De standaard eenheid bij dit datatype is uitgedrukt in Watt.",
                     "https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#KwantWrdInWatt",
                     "1", "1",
                     "https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#KwantWrdInWatt.standaardEenheid",
                     "http://www.w3.org/2000/01/rdf-schema#Literal", "0", "\"W\"^^cdt:ucumunit", "1", "\"W\"^^cdt:ucumunit", ""],
                    ["waarde", "waarde", "Bevat een getal die bij het datatype hoort.",
                     "https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#KwantWrdInWatt",
                     "1", "1", "https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#KwantWrdInWatt.waarde",
                     "http://www.w3.org/2001/XMLSchema#decimal", "0", "", "0", "", ""]]
        elif query == "SELECT name, label_nl, definition_nl, class_uri, kardinaliteit_min, kardinaliteit_max, uri, fieldType, overerving, constraints, readonly, usagenote_nl, deprecated_version FROM OSLODatatypePrimitiveAttributen" and arg_dict == {}:
            return [['waarde', 'waarde', 'Beschrijft een kleur volgens het RAL classificatiesysteem.',
                     'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DteKleurRAL', '1', '1',
                     'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DteKleurRAL.waarde',
                     'http://www.w3.org/2001/XMLSchema#string', '0', '', '0',
                     'De waarde moet voldoen aan volgende regex: [1-9]\d{3}', '']]
        elif query == "SELECT name, label_nl, definition_nl, class_uri, kardinaliteit_min, kardinaliteit_max, uri, fieldType, overerving, constraints, readonly, usagenote_nl, deprecated_version FROM OSLODatatypeComplexAttributen" and arg_dict == {}:
            return [['identificator', 'identificator', 'Een groep van tekens om een AIM object te identificeren of te benoemen.',
                     'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcIdentificator', '1', '1',
                     'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcIdentificator.identificator',
                     'http://www.w3.org/2001/XMLSchema#string', '0', '', '0', '', ''],
                    ['toegekendDoor', 'toegekend door', 'Gegevens van de organisatie die de toekenning deed.',
                     'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcIdentificator', '1', '1',
                     'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcIdentificator.toegekendDoor',
                     'http://www.w3.org/2001/XMLSchema#string', '0', '', '0', '', '']]

        elif query == "SELECT name, uri, definition_nl, label_nl, usagenote_nl, deprecated_version FROM OSLODatatypeComplex" and arg_dict == {}:
            return [['DtcIdentificator', 'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcIdentificator', '',
                     'Complex datatype voor de identificator van een AIM object volgens de bron van de identificator.',
                     'Identificator', '']]

        elif query == "SELECT name, uri, usagenote_nl, definition_nl, label_nl, codelist, deprecated_version FROM OSLOEnumeration" and arg_dict == {}:
            return [['KlAIMToestand', 'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#KlAIMToestand', '',
                     'Keuzelijst met fasen uit de levenscyclus van een object om de toestand op een moment mee vast te leggen.',
                     'AIM toestand', 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlAIMToestand', '']]

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

    def test_OTLDbPrimitiveDatatypes(self):
        file_location = '../InputFiles/OTL.db'
        file_exist_checker = FileExistChecker(file_location)
        sql_reader = SQLDbReader(file_exist_checker)
        oslo_creator = OSLOInMemoryCreator(sql_reader)
        listOfPrimitiveDatatypes = oslo_creator.getAllPrimitiveDatatypes()

        self.assertTrue(len(listOfPrimitiveDatatypes) > 0)
        first = next(c for c in listOfPrimitiveDatatypes)
        self.assertEqual(type(first), OSLODatatypePrimitive)

    def test_OTLDbPrimitiveDatatypeAttributen(self):
        file_location = '../InputFiles/OTL.db'
        file_exist_checker = FileExistChecker(file_location)
        sql_reader = SQLDbReader(file_exist_checker)
        oslo_creator = OSLOInMemoryCreator(sql_reader)
        listOfPrimitiveDatatypeAttributen = oslo_creator.getAllPrimitiveDatatypeAttributen()

        self.assertTrue(len(listOfPrimitiveDatatypeAttributen) > 0)
        first = next(c for c in listOfPrimitiveDatatypeAttributen)
        self.assertEqual(type(first), OSLODatatypePrimitiveAttribuut)

    def test_Mock_getAllClasses(self):
        mock = Mock()
        oSLOCreator = OSLOInMemoryCreator(mock)
        mock.performReadQuery = self.mockPerformReadQuery
        uri = 'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#NaampadObject'
        listOfClasses = oSLOCreator.getAllClasses()

        self.assertTrue(len(listOfClasses) >= 1)
        first = next(c for c in listOfClasses)
        self.assertEqual(type(first), OSLOClass)
        self.assertEqual(first.uri, uri)

    def test_Mock_getClassByUri(self):
        mock = Mock()
        oSLOCreator = OSLOInMemoryCreator(mock)
        mock.performReadQuery = self.mockPerformReadQuery
        uri = 'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#NaampadObject'
        listOfClasses = oSLOCreator.getClassByUri(uri)

        self.assertTrue(len(listOfClasses) == 1)
        first = next(c for c in listOfClasses)
        self.assertEqual(type(first), OSLOClass)
        self.assertEqual(first.uri, uri)

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
        self.assertEqual(first.uri, attributeUri)

    def test_Mock_getAttributes(self):
        mock = Mock()
        oSLOCreator = OSLOInMemoryCreator(mock)
        mock.performReadQuery = self.mockPerformReadQuery
        attributeUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#NaampadObject.naampad'
        listOfAttributes = oSLOCreator.getAttributes()

        self.assertTrue(len(listOfAttributes) >= 1)
        first = next(c for c in listOfAttributes)
        self.assertEqual(type(first), OSLOAttribuut)
        self.assertEqual(first.uri, attributeUri)

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

    def test_Mock_getAllPrimitiveDatatypes(self):
        mock = Mock()
        oSLOCreator = OSLOInMemoryCreator(mock)
        mock.performReadQuery = self.mockPerformReadQuery
        listOfPrimitiveDatatypes = oSLOCreator.getAllPrimitiveDatatypes()
        class_uri = 'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DteKleurRAL'

        self.assertTrue(len(listOfPrimitiveDatatypes) >= 1)
        first = next(c for c in listOfPrimitiveDatatypes)
        self.assertEqual(type(first), OSLODatatypePrimitive)
        self.assertEqual(first.uri, class_uri)

    def test_Mock_getAllPrimitiveDatatypeAttributen(self):
        mock = Mock()
        oSLOCreator = OSLOInMemoryCreator(mock)
        mock.performReadQuery = self.mockPerformReadQuery
        listOfPrimitiveDatatypeAttributen = oSLOCreator.getAllPrimitiveDatatypeAttributen()
        class_uri = 'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DteKleurRAL.waarde'

        self.assertTrue(len(listOfPrimitiveDatatypeAttributen) >= 1)
        first = next(c for c in listOfPrimitiveDatatypeAttributen)
        self.assertEqual(type(first), OSLODatatypePrimitiveAttribuut)
        self.assertEqual(first.uri, class_uri)

    def test_Mock_getAllComplexDatatypes(self):
        mock = Mock()
        oSLOCreator = OSLOInMemoryCreator(mock)
        mock.performReadQuery = self.mockPerformReadQuery
        listOfComplexDatatypes = oSLOCreator.getAllComplexDatatypes()
        class_uri = 'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcIdentificator'

        self.assertTrue(len(listOfComplexDatatypes) >= 1)
        first = next(c for c in listOfComplexDatatypes)
        self.assertEqual(type(first), OSLODatatypeComplex)
        self.assertEqual(first.uri, class_uri)

    def test_Mock_getAllComplexDatatypeAttributen(self):
        mock = Mock()
        oSLOCreator = OSLOInMemoryCreator(mock)
        mock.performReadQuery = self.mockPerformReadQuery
        listOfComplexDatatypeAttributen = oSLOCreator.getAllComplexDatatypeAttributen()
        attribuut_uri = 'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcIdentificator.identificator'

        self.assertTrue(len(listOfComplexDatatypeAttributen) >= 1)
        first = next(c for c in listOfComplexDatatypeAttributen)
        self.assertEqual(type(first), OSLODatatypeComplexAttribuut)
        self.assertEqual(first.uri, attribuut_uri)

    def test_Mock_getAllEnumerations(self):
        mock = Mock()
        oSLOCreator = OSLOInMemoryCreator(mock)
        mock.performReadQuery = self.mockPerformReadQuery
        listOfEnumerations = oSLOCreator.getEnumerations()
        class_uri = 'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#KlAIMToestand'

        self.assertTrue(len(listOfEnumerations) >= 1)
        first = next(c for c in listOfEnumerations)
        self.assertEqual(type(first), OSLOEnumeration)
        self.assertEqual(first.uri, class_uri)
