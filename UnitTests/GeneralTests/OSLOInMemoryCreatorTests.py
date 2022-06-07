import os
import unittest

from OTLMOW.ModelGenerator.Inheritance import Inheritance
from OTLMOW.ModelGenerator.OSLOAttribuut import OSLOAttribuut
from OTLMOW.ModelGenerator.OSLOClass import OSLOClass
from OTLMOW.ModelGenerator.OSLODatatypeComplex import OSLODatatypeComplex
from OTLMOW.ModelGenerator.OSLODatatypeComplexAttribuut import OSLODatatypeComplexAttribuut
from OTLMOW.ModelGenerator.OSLODatatypePrimitive import OSLODatatypePrimitive
from OTLMOW.ModelGenerator.OSLODatatypePrimitiveAttribuut import OSLODatatypePrimitiveAttribuut
from OTLMOW.ModelGenerator.OSLODatatypeUnion import OSLODatatypeUnion
from OTLMOW.ModelGenerator.OSLODatatypeUnionAttribuut import OSLODatatypeUnionAttribuut
from OTLMOW.ModelGenerator.OSLOEnumeration import OSLOEnumeration
from OTLMOW.ModelGenerator.OSLOInMemoryCreator import OSLOInMemoryCreator
from OTLMOW.ModelGenerator.OSLORelatie import OSLORelatie
from OTLMOW.ModelGenerator.OSLOTypeLink import OSLOTypeLink
from OTLMOW.ModelGenerator.SQLDbReader import SQLDbReader


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

    def test_file_not_found(self):
        file_location = ''
        with self.assertRaises(FileNotFoundError):
            sql_reader = SQLDbReader(file_location)

    def test_get_all_classes(self):
        base_dir = os.path.dirname(os.path.realpath(__file__))
        file_location = f'{base_dir}/../OTL_AllCasesTestClass.db'
        sql_reader = SQLDbReader(file_location)
        oslo_creator = OSLOInMemoryCreator(sql_reader)
        list_of_classes = oslo_creator.get_all_classes()

        self.assertEqual(10, len(list_of_classes))
        self.assertTrue(isinstance(list_of_classes[0], OSLOClass))

    def test_get_all_primitive_datatypes(self):
        base_dir = os.path.dirname(os.path.realpath(__file__))
        file_location = f'{base_dir}/../OTL_AllCasesTestClass.db'
        sql_reader = SQLDbReader(file_location)
        oslo_creator = OSLOInMemoryCreator(sql_reader)
        list_of_primitive_datatypes = oslo_creator.get_all_primitive_datatypes()

        self.assertEqual(13, len(list_of_primitive_datatypes))
        self.assertTrue(isinstance(list_of_primitive_datatypes[0], OSLODatatypePrimitive))

    def test_get_all_primitive_datatype_attributes(self):
        base_dir = os.path.dirname(os.path.realpath(__file__))
        file_location = f'{base_dir}/../OTL_AllCasesTestClass.db'
        sql_reader = SQLDbReader(file_location)
        oslo_creator = OSLOInMemoryCreator(sql_reader)
        list_of_primitive_datatypes_attributes = oslo_creator.get_all_primitive_datatype_attributes()

        self.assertEqual(5, len(list_of_primitive_datatypes_attributes))
        self.assertTrue(isinstance(list_of_primitive_datatypes_attributes[0], OSLODatatypePrimitiveAttribuut))

    def test_get_class_by_uri(self):
        base_dir = os.path.dirname(os.path.realpath(__file__))
        file_location = f'{base_dir}/../OTL_AllCasesTestClass.db'
        sql_reader = SQLDbReader(file_location)
        oslo_creator = OSLOInMemoryCreator(sql_reader)
        uri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#AllCasesTestClass'
        specific_class = oslo_creator.get_class_by_uri(uri)

        self.assertTrue(isinstance(specific_class, OSLOClass))
        self.assertEqual(uri, specific_class.objectUri)

    def test_get_attributes_by_class_uri(self):
        base_dir = os.path.dirname(os.path.realpath(__file__))
        file_location = f'{base_dir}/../OTL_AllCasesTestClass.db'
        sql_reader = SQLDbReader(file_location)
        oslo_creator = OSLOInMemoryCreator(sql_reader)
        uri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#AllCasesTestClass'
        attribute_uri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#AllCasesTestClass.testBooleanField'
        attributes = oslo_creator.get_attributes_by_class_uri(uri)

        self.assertTrue(isinstance(attributes[0], OSLOAttribuut))
        self.assertEqual(attribute_uri, attributes[0].objectUri)
        self.assertEqual(uri, attributes[0].class_uri)

    def test_get_all_attributes(self):
        base_dir = os.path.dirname(os.path.realpath(__file__))
        file_location = f'{base_dir}/../OTL_AllCasesTestClass.db'
        sql_reader = SQLDbReader(file_location)
        oslo_creator = OSLOInMemoryCreator(sql_reader)
        attributes = oslo_creator.get_all_attributes()
        attribute_uri = 'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#AIMDBStatus.isActief'

        self.assertTrue(isinstance(attributes[0], OSLOAttribuut))
        self.assertEqual(attribute_uri, attributes[0].objectUri)

    def test_get_all_inheritances(self):
        base_dir = os.path.dirname(os.path.realpath(__file__))
        file_location = f'{base_dir}/../OTL_AllCasesTestClass.db'
        sql_reader = SQLDbReader(file_location)
        oslo_creator = OSLOInMemoryCreator(sql_reader)
        inheritances = oslo_creator.get_all_inheritances()

        self.assertEqual(9, len(inheritances))
        self.assertTrue(isinstance(inheritances[0], Inheritance))
        self.assertEqual('https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#AIMDBStatus', inheritances[0].base_uri)
        self.assertEqual('https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#AIMObject', inheritances[0].class_uri)

    def test_get_all_complex_datatypes(self):
        base_dir = os.path.dirname(os.path.realpath(__file__))
        file_location = f'{base_dir}/../OTL_AllCasesTestClass.db'
        sql_reader = SQLDbReader(file_location)
        oslo_creator = OSLOInMemoryCreator(sql_reader)
        list_of_complex_datatypes = oslo_creator.get_all_complex_datatypes()

        self.assertEqual(3, len(list_of_complex_datatypes))
        self.assertTrue(isinstance(list_of_complex_datatypes[0], OSLODatatypeComplex))
        self.assertEqual('https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcIdentificator',
                         list_of_complex_datatypes[0].objectUri)

    def test_get_all_complex_datatype_attributes(self):
        base_dir = os.path.dirname(os.path.realpath(__file__))
        file_location = f'{base_dir}/../OTL_AllCasesTestClass.db'
        sql_reader = SQLDbReader(file_location)
        oslo_creator = OSLOInMemoryCreator(sql_reader)
        list_of_complex_datatypes_attributes = oslo_creator.get_all_complex_datatype_attributes()

        self.assertEqual(13, len(list_of_complex_datatypes_attributes))
        self.assertTrue(isinstance(list_of_complex_datatypes_attributes[0], OSLODatatypeComplexAttribuut))
        self.assertEqual('https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcIdentificator.identificator',
                         list_of_complex_datatypes_attributes[0].objectUri)

    def test_get_all_enumerations(self):
        base_dir = os.path.dirname(os.path.realpath(__file__))
        file_location = f'{base_dir}/../OTL_AllCasesTestClass.db'
        sql_reader = SQLDbReader(file_location)
        oslo_creator = OSLOInMemoryCreator(sql_reader)
        enumerations = oslo_creator.get_all_enumerations()

        self.assertEqual(2, len(enumerations))
        self.assertTrue(isinstance(enumerations[0], OSLOEnumeration))
        self.assertEqual('https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#KlTestKeuzelijst', enumerations[0].objectUri)

    def test_get_all_relations(self):
        base_dir = os.path.dirname(os.path.realpath(__file__))
        file_location = f'{base_dir}/../OTL_AllCasesTestClass.db'
        sql_reader = SQLDbReader(file_location)
        oslo_creator = OSLOInMemoryCreator(sql_reader)
        relations = oslo_creator.get_all_relations()

        self.assertEqual(2, len(relations))
        self.assertTrue(isinstance(relations[0], OSLORelatie))
        self.assertEqual('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', relations[0].objectUri)
        self.assertEqual('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#AnotherTestClass', relations[0].doel_uri)
        self.assertEqual('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#AllCasesTestClass', relations[0].bron_uri)

    def test_get_all_union_datatypes(self):
        base_dir = os.path.dirname(os.path.realpath(__file__))
        file_location = f'{base_dir}/../OTL_AllCasesTestClass.db'
        sql_reader = SQLDbReader(file_location)
        oslo_creator = OSLOInMemoryCreator(sql_reader)
        list_of_union_datatypes = oslo_creator.get_all_union_datatypes()

        self.assertEqual(1, len(list_of_union_datatypes))
        self.assertTrue(isinstance(list_of_union_datatypes[0], OSLODatatypeUnion))
        self.assertEqual('https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtuTestUnionType',
                         list_of_union_datatypes[0].objectUri)

    def test_get_all_union_datatype_attributes(self):
        base_dir = os.path.dirname(os.path.realpath(__file__))
        file_location = f'{base_dir}/../OTL_AllCasesTestClass.db'
        sql_reader = SQLDbReader(file_location)
        oslo_creator = OSLOInMemoryCreator(sql_reader)
        list_of_union_datatypes_attributes = oslo_creator.get_all_union_datatype_attributes()

        self.assertEqual(2, len(list_of_union_datatypes_attributes))
        self.assertTrue(isinstance(list_of_union_datatypes_attributes[0], OSLODatatypeUnionAttribuut))
        self.assertEqual('https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtuTestUnionType.unionKwantWrd',
                         list_of_union_datatypes_attributes[0].objectUri)

    def test_get_all_typelinks(self):
        base_dir = os.path.dirname(os.path.realpath(__file__))
        file_location = f'{base_dir}/../OTL_AllCasesTestClass.db'
        sql_reader = SQLDbReader(file_location)
        oslo_creator = OSLOInMemoryCreator(sql_reader)
        type_links = oslo_creator.get_all_typelinks()

        self.assertEqual(19, len(type_links))
        self.assertTrue(isinstance(type_links[0], OSLOTypeLink))
        self.assertEqual('http://www.w3.org/2000/01/rdf-schema#Literal',
                         type_links[0].item_uri)