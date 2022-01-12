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
from ModelGenerator.OSLODatatypeUnion import OSLODatatypeUnion
from ModelGenerator.OSLODatatypeUnionAttribuut import OSLODatatypeUnionAttribuut
from ModelGenerator.OSLOEnumeration import OSLOEnumeration
from ModelGenerator.OSLOInMemoryCreator import OSLOInMemoryCreator
from ModelGenerator.OSLORelatie import OSLORelatie
from ModelGenerator.SQLDbReader import SQLDbReader


class OSLOInMemoryCreatorTests(unittest.TestCase):
    def mockPerformReadQuery(self, query, arg_dict):
        if query == 'SELECT label_nl, name, uri, definition_nl, usagenote_nl, abstract, deprecated_version FROM OSLOClass where objectUri=:uriclass' \
                and arg_dict['uriclass'] == 'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#NaampadObject':
            return [['Naampad object', 'NaampadObject',
                     'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#NaampadObject'
                        , 'Abstracte als de basisklasse voor elk OTL object dat gebruik maakt van een naampad.', '', 1, '']]
        elif query == 'SELECT label_nl, name, uri, definition_nl, usagenote_nl, abstract, deprecated_version FROM OSLOClass' and arg_dict == {}:
            return [['Naampad object', 'NaampadObject',
                     'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#NaampadObject'
                        , 'Abstracte als de basisklasse voor elk OTL object dat gebruik maakt van een naampad.', '', 1, '']]
        elif query == 'SELECT name, label_nl, definition_nl, class_uri, kardinaliteit_min, kardinaliteit_max, uri, type, overerving, constraints, readonly, usagenote_nl, deprecated_version FROM OSLOAttributen WHERE class_uri=:uriclass AND overerving = 0 and name <> \'typeURI\'' and \
                arg_dict['uriclass'] == 'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#NaampadObject':
            return [[
                'naampad', 'naampad',
                'Een set van objecten (bv. collecties) die aanduiden waar het object zich bevindt in de objectenboom (EM-Infra).'
                , 'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#NaampadObject', '1', '1',
                'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#NaampadObject.naampad',
                'http://www.w3.org/2001/XMLSchema#string', 0, '', 0, '', ''
            ]]
        elif query == 'SELECT name, label_nl, definition_nl, class_uri, kardinaliteit_min, kardinaliteit_max, uri, type, ' \
                      'overerving, constraints, readonly, usagenote_nl, deprecated_version FROM OSLOAttributen WHERE overerving ' \
                      '= 0 and name <> \'typeURI\'' and arg_dict == {}:
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
        elif query == "SELECT name, label_nl, definition_nl, class_uri, kardinaliteit_min, kardinaliteit_max, uri, type, overerving, constraints, readonly, usagenote_nl, deprecated_version FROM OSLOAttributen" and arg_dict == {}:
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
        elif query == "SELECT name, label_nl, definition_nl, class_uri, kardinaliteit_min, kardinaliteit_max, uri, type, overerving, constraints, readonly, usagenote_nl, deprecated_version FROM OSLODatatypePrimitiveAttributen" and arg_dict == {}:
            return [['waarde', 'waarde', 'Beschrijft een kleur volgens het RAL classificatiesysteem.',
                     'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DteKleurRAL', '1', '1',
                     'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DteKleurRAL.waarde',
                     'http://www.w3.org/2001/XMLSchema#string', '0', '', '0',
                     'De waarde moet voldoen aan volgende regex: [1-9]\d{3}', '']]
        elif query == "SELECT name, label_nl, definition_nl, class_uri, kardinaliteit_min, kardinaliteit_max, uri, type, overerving, constraints, readonly, usagenote_nl, deprecated_version FROM OSLODatatypeComplexAttributen" and arg_dict == {}:
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

        elif query == "SELECT * FROM OSLORelaties ORDER BY uri, bron_uri, doel_uri" and arg_dict == {}:
            return [['', 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Fundering',
                     'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#AansluitendeConstructie',
                     'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Betonfundering',
                     'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', 'Unspecified',
                     'Klasse uit gebruik sinds versie 2.0.0', '2.0.0']]

        elif query == "SELECT * FROM OSLORelaties WHERE bron_overerving = '' AND doel_overerving = '' ORDER BY uri, bron_uri, " \
                      "doel_uri" and arg_dict == {}:
            return [['', '', 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Behuizing',
                     'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Contactor',
                     'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', 'Unspecified', '', ''],
                    ['', '', 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Contactor',
                     'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Behuizing',
                     'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', 'Unspecified', '', ''],
                    ['', '', 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Contactor',
                     'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Laagspanningsbord',
                     'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', 'Unspecified', '', ''],
                    ['', '', 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Laagspanningsbord',
                     'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Contactor',
                     'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', 'Unspecified', '', ''],
                    ['', '', 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Contactor',
                     'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#IOKaart',
                     'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Sturing', 'Unspecified', '', ''],
                    ['', '', 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#IOKaart',
                     'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Contactor',
                     'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Sturing', 'Unspecified', '', ''],
                    ['', '', 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Contactor',
                     'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Contactor',
                     'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Voedt', 'Source -> Destination', '', ''],
                    ['', '', 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Stroomkring',
                     'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Contactor',
                     'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Voedt', 'Source -> Destination', '', ''],
                    ['', '', 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Contactor',
                     'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Seinlantaarn',
                     'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#VoedtAangestuurd', 'Source -> Destination', '', ''],
                    ['', '', 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Contactor',
                     'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Ventilatie',
                     'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#VoedtAangestuurd', 'Source -> Destination', '', ''],
                    ['', '', 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Contactor',
                     'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Calamiteitendoorsteek',
                     'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#VoedtAangestuurd', 'Source -> Destination', '', ''],
                    ['', '', 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Contactor',
                     'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#SlagboomarmVerlichting',
                     'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#VoedtAangestuurd', 'Source -> Destination', '', ''],
                    ['', '', 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Contactor',
                     'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Slagboomkolom',
                     'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#VoedtAangestuurd', 'Source -> Destination', '', '']]

        elif query == "SELECT name, label_nl, definition_nl, class_uri, kardinaliteit_min, kardinaliteit_max, uri, type, overerving, constraints, readonly, usagenote_nl, deprecated_version FROM OSLODatatypeUnionAttributen" and arg_dict == {}:
            return [['afwijkendeHoogte', 'afwijkende hoogte', 'De afwijkende hoogte van de mast in meter.',
                     'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DtuLichtmastMasthoogte', '0', '1',
                     'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DtuLichtmastMasthoogte.afwijkendeHoogte',
                     'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#KwantWrdInMeter', 0, '', 0, '', ''],
                    ['standaardHoogte', 'standaard hoogte', 'Bepaling van de standaard hoogte van een mast.',
                     'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DtuLichtmastMasthoogte', '0', '1',
                     'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DtuLichtmastMasthoogte.standaardHoogte',
                     'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlLichtmastMasthoogte', 0, '', 0, '', '']]

        elif query == "SELECT name, uri, definition_nl, label_nl, usagenote_nl, deprecated_version FROM OSLODatatypeUnion" and arg_dict == {}:
            return [['DtuLichtmastMasthoogte', 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DtuLichtmastMasthoogte',
                     'Union datatype om een standaard of afwijkende masthoogte te bepalen.', 'Masthoogte', '', '']]

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
        self.assertEqual(first.objectUri, uri)

    def test_Mock_getClassByUri(self):
        mock = Mock()
        oSLOCreator = OSLOInMemoryCreator(mock)
        mock.performReadQuery = self.mockPerformReadQuery
        uri = 'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#NaampadObject'
        listOfClasses = oSLOCreator.getClassByUri(uri)

        self.assertTrue(len(listOfClasses) == 1)
        first = next(c for c in listOfClasses)
        self.assertEqual(type(first), OSLOClass)
        self.assertEqual(first.objectUri, uri)

    def test_Mock_getAttributeByClassUri(self):
        mock = Mock()
        oSLOCreator = OSLOInMemoryCreator(mock)
        mock.performReadQuery = self.mockPerformReadQuery
        uri = 'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#NaampadObject'
        attributeUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#NaampadObject.naampad'
        listOfAttributes = oSLOCreator.getAttributes()
        attributes = oSLOCreator.getAttributeByClassUri(uri)

        self.assertTrue(len(listOfAttributes) == 1)
        first = next(c for c in listOfAttributes)
        self.assertEqual(type(first), OSLOAttribuut)
        self.assertEqual(first.objectUri, attributeUri)

    def test_Mock_getAttributes(self):
        mock = Mock()
        oSLOCreator = OSLOInMemoryCreator(mock)
        mock.performReadQuery = self.mockPerformReadQuery
        attributeUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#NaampadObject.naampad'
        listOfAttributes = oSLOCreator.getAttributes()

        self.assertTrue(len(listOfAttributes) >= 1)
        first = next(c for c in listOfAttributes)
        self.assertEqual(type(first), OSLOAttribuut)
        self.assertEqual(first.objectUri, attributeUri)

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
        self.assertEqual(first.objectUri, class_uri)

    def test_Mock_getAllPrimitiveDatatypeAttributen(self):
        mock = Mock()
        oSLOCreator = OSLOInMemoryCreator(mock)
        mock.performReadQuery = self.mockPerformReadQuery
        listOfPrimitiveDatatypeAttributen = oSLOCreator.getAllPrimitiveDatatypeAttributen()
        class_uri = 'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DteKleurRAL.waarde'

        self.assertTrue(len(listOfPrimitiveDatatypeAttributen) >= 1)
        first = next(c for c in listOfPrimitiveDatatypeAttributen)
        self.assertEqual(type(first), OSLODatatypePrimitiveAttribuut)
        self.assertEqual(first.objectUri, class_uri)

    def test_Mock_getAllComplexDatatypes(self):
        mock = Mock()
        oSLOCreator = OSLOInMemoryCreator(mock)
        mock.performReadQuery = self.mockPerformReadQuery
        listOfComplexDatatypes = oSLOCreator.getAllComplexDatatypes()
        class_uri = 'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcIdentificator'

        self.assertTrue(len(listOfComplexDatatypes) >= 1)
        first = next(c for c in listOfComplexDatatypes)
        self.assertEqual(type(first), OSLODatatypeComplex)
        self.assertEqual(first.objectUri, class_uri)

    def test_Mock_getAllComplexDatatypeAttributen(self):
        mock = Mock()
        oSLOCreator = OSLOInMemoryCreator(mock)
        mock.performReadQuery = self.mockPerformReadQuery
        listOfComplexDatatypeAttributen = oSLOCreator.getAllComplexDatatypeAttributen()
        attribuut_uri = 'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcIdentificator.identificator'

        self.assertTrue(len(listOfComplexDatatypeAttributen) >= 1)
        first = next(c for c in listOfComplexDatatypeAttributen)
        self.assertEqual(type(first), OSLODatatypeComplexAttribuut)
        self.assertEqual(first.objectUri, attribuut_uri)

    def test_Mock_getAllEnumerations(self):
        mock = Mock()
        oSLOCreator = OSLOInMemoryCreator(mock)
        mock.performReadQuery = self.mockPerformReadQuery
        listOfEnumerations = oSLOCreator.getEnumerations()
        class_uri = 'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#KlAIMToestand'

        self.assertTrue(len(listOfEnumerations) >= 1)
        first = next(c for c in listOfEnumerations)
        self.assertEqual(type(first), OSLOEnumeration)
        self.assertEqual(first.objectUri, class_uri)

    def test_Mock_getAllRelations(self):
        mock = Mock()
        oSLOCreator = OSLOInMemoryCreator(mock)
        mock.performReadQuery = self.mockPerformReadQuery
        listOfRelations = oSLOCreator.getAllRelations()

        self.assertTrue(len(listOfRelations) >= 1)
        first = next(c for c in listOfRelations)
        self.assertEqual(type(first), OSLORelatie)
        self.assertEqual(first.objectUri, "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging")

    def test_Mock_getAllUnionDatatypes(self):
        mock = Mock()
        oSLOCreator = OSLOInMemoryCreator(mock)
        mock.performReadQuery = self.mockPerformReadQuery
        listOfUnionDatatypes = oSLOCreator.getAllUnionDatatypes()
        class_uri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DtuLichtmastMasthoogte'

        self.assertTrue(len(listOfUnionDatatypes) >= 1)
        first = next(c for c in listOfUnionDatatypes)
        self.assertEqual(type(first), OSLODatatypeUnion)
        self.assertEqual(first.objectUri, class_uri)

    def test_Mock_getAllUnionDatatypeAttributen(self):
        mock = Mock()
        oSLOCreator = OSLOInMemoryCreator(mock)
        mock.performReadQuery = self.mockPerformReadQuery
        listOfUnionDatatypeAttributen = oSLOCreator.getAllUnionDatatypeAttributen()
        attribuut_uri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DtuLichtmastMasthoogte.afwijkendeHoogte'

        self.assertTrue(len(listOfUnionDatatypeAttributen) >= 1)
        first = next(c for c in listOfUnionDatatypeAttributen)
        self.assertEqual(type(first), OSLODatatypeUnionAttribuut)
        self.assertEqual(first.objectUri, attribuut_uri)
