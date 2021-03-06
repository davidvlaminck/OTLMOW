# -*- coding: utf-8 -*-
import os
import unittest
from unittest.mock import Mock

from OTLMOW.ModelGenerator.OSLOCollector import OSLOCollector
from OTLMOW.ModelGenerator.OSLOInMemoryCreator import OSLOInMemoryCreator
from OTLMOW.ModelGenerator.OTLGeldigeRelatieCreator import OTLGeldigeRelatieCreator
from OTLMOW.ModelGenerator.SQLDbReader import SQLDbReader


class OTLClassCreatorTests(unittest.TestCase):

    def mockPerformReadQuery(self, query, arg_dict):
        if query == 'SELECT label_nl, name, uri, definition_nl, usagenote_nl, abstract, deprecated_version FROM OSLOClass where uri=:uriclass' \
                and arg_dict['uriclass'] == 'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#NaampadObject':
            return [['Naampad object', 'NaampadObject',
                     'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#NaampadObject'
                        , 'Abstracte als de basisklasse voor elk OTL object dat gebruik maakt van een naampad.', '', 1, '']]
        elif query == 'SELECT label_nl, name, uri, definition_nl, usagenote_nl, abstract, deprecated_version FROM OSLOClass' and arg_dict == {}:
            return [['Naampad object', 'NaampadObject',
                     'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#NaampadObject'
                        , 'Abstracte als de basisklasse voor elk OTL object dat gebruik maakt van een naampad.', '', 1, ''],
                    ['Behuizing', 'Behuizing', 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Behuizing',
                     'Abstracte voor alle types van behuizing voor het beschermen van technieken.', '', '1', ''],
                    ['Seinlantaarn', 'Seinlantaarn', 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Seinlantaarn',
                     'Abstracte voor het geheel van één of meerdere verkeerslichten die boven elkaar worden opgesteld en worden bevestigd op een steun,teneinde de beweging van een weggebruiker die een bepaald traject volgt,te verhinderen of toe te laten.',
                     '', '1', ''],
                    ['Ventilatie', 'Ventilatie', 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Ventilatie',
                     'Abstracte voor attributen die gemeenschappelijk zijn voor verschillende types van ventilatie.', '', '1',
                     ''],
                    ['Bevestiging', 'Bevestiging', 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging',
                     'Deze relatie geeft aan dat twee onderdelen direct fysiek op elkaar bevestigd zijn. Dit kan zowel aan de buitenkant als aan de binnenkant zijn zoals bv. een camera aan een paal of een laagspanningsbord in een kast. Deze relatie heeft geen richting.',
                     '', '0', ''],
                    ['Calamiteitendoorsteek', 'Calamiteitendoorsteek',
                     'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Calamiteitendoorsteek',
                     'Een calamiteitendoorsteek, afgekort CADO, is een mechanische constructie voor het opklappen van een deel van de vangrail in de middenberm van een weg. Het primaire doel van de calamiteitendoorsteek is het doorlaten van hulpverleningsvoertuigen.',
                     '', '0', ''],
                    ['Contactor', 'Contactor', 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Contactor',
                     'Toestel dat ter plaatse of op afstand aangestuurd wordt om (grote) vermogensstromen af te schakelen.', '',
                     '0', ''],
                    ['IO-Kaart', 'IOKaart', 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#IOKaart',
                     'Een kaart of module die gebruikt wordt voor de ingang of uitgang van een verwerkingseenheid (bv. een PLC). Op de IO-kaart worden perifere toestellen en sensoren aangesloten.',
                     '', '0', ''],
                    ['Laagspanningsbord', 'Laagspanningsbord',
                     'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Laagspanningsbord',
                     'Verzameling van alle elektrische componenten nodig voor de voeding en sturing van applicaties die erop aangesloten zijn. Omvat onder andere automaten,klemmenblokken,...',
                     '', '0', ''],
                    ['Slagboomarm verlichting', 'SlagboomarmVerlichting',
                     'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#SlagboomarmVerlichting',
                     'Verlichting bevestigd aan de slagboomarm om de zichtbaarheid van die arm te verhogen.', '', '0', ''],
                    ['Slagboomkolom', 'Slagboomkolom', 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Slagboomkolom',
                     'De koker van een slagboominstallatie die de motor bevat en waaraan de slagboomarm bevestigd is.', '', '0',
                     ''],
                    ['Stroomkring', 'Stroomkring', 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Stroomkring',
                     'Ook wel vertrek of vertrekkende kabel genoemd. Afgezekerde elektrische geleiders waarmee de applicaties voorzien worden van de nodige voeding.',
                     '', '0', ''],
                    ['Sturing', 'Sturing', 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Sturing',
                     'Deze relatie geeft aan of er een of andere vorm van dataverkeer is tussen 2 onderdelen. Een wegverlichtingstoestel dat aan staat wordt ook als sturing beschouwd, in dit geval is het een lang ononderbroken elektrisch aan-signaal. Deze relatie heeft geen richting.',
                     '', '0', ''],
                    ['Voedt', 'Voedt', 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Voedt',
                     'Deze relatie wordt enkel gelegd naar onderdelen die permanent onder spanning staan in normaal bedrijf. Aan deze relatie wordt steeds een richting toegekend van de voedinggever naar de ontvanger.',
                     '', '0', ''],
                    ['Voedt aangestuurd', 'VoedtAangestuurd',
                     'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#VoedtAangestuurd',
                     'Deze relatie wordt enkel gelegd naar objecttypes die typisch een groot vermogen vereisen en onder spanning komen nadat het voedend element aangestuurd is om die spanning door te sturen.',
                     '', '0', '']]
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

        elif query == "SELECT * FROM OSLORelaties ORDER BY uri, bron_uri, " \
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
        return []

    def setUp(self) -> OSLOCollector:
        base_dir = os.path.dirname(os.path.realpath(__file__))
        file_location = f'{base_dir}/../OTL_AllCasesTestClass.db'
        sql_reader = SQLDbReader(file_location)
        oslo_creator = OSLOInMemoryCreator(sql_reader)
        collector = OSLOCollector(oslo_creator)
        collector.collect()
        return collector

    def test_write(self):
        expected_data = ['# coding=utf-8',
                         'from OTLMOW.ModelGenerator.BaseClasses.GeldigeRelatie import GeldigeRelatie',
                         '',
                         '',
                         'class GeldigeRelatieLijst:',
                         '    def __init__(self):',
                         '        self.lijst = [',
                         '            GeldigeRelatie("https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#AllCasesTestClass", "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#AnotherTestClass", "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging", ""),',
                         '            GeldigeRelatie("https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#AllCasesTestClass", "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#AnotherTestClass", "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Voedt", "")',
                         '        ]']

        collector = self.setUp()
        creator = OTLGeldigeRelatieCreator(collector)
        data_to_write = creator.create_block_to_write_from_relations()
        self.assertListEqual(expected_data, data_to_write)
