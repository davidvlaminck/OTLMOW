import os
import unittest
from unittest import mock
from unittest.mock import patch

import rdflib

from OTLMOW.Loggers.NoneLogger import NoneLogger
from OTLMOW.ModelGenerator.OSLOCollector import OSLOCollector
from OTLMOW.ModelGenerator.OSLOEnumeration import OSLOEnumeration
from OTLMOW.ModelGenerator.OSLOInMemoryCreator import OSLOInMemoryCreator
from OTLMOW.ModelGenerator.OTLEnumerationCreator import OTLEnumerationCreator
from OTLMOW.ModelGenerator.SQLDbReader import SQLDbReader
from OTLMOW.OTLModel.Datatypes.KeuzelijstWaarde import KeuzelijstWaarde

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


class EnumerationOSLOCollector(OSLOCollector):
    def __init__(self, reader):
        super().__init__(reader)

        self.enumerations = [
            OSLOEnumeration('KlAIMToestand', 'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#KlAIMToestand',
                            '',
                            'Keuzelijst met fasen uit de levenscyclus van een object om de toestand op een moment mee vast te leggen.',
                            'AIM toestand', 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlAIMToestand', '')]

        self.expectedDataKlAIMToestand = [
            "# coding=utf-8",
            "from OTLMOW.OTLModel.Datatypes.KeuzelijstField import KeuzelijstField",
            "from OTLMOW.OTLModel.Datatypes.KeuzelijstWaarde import KeuzelijstWaarde",
            "",
            "",
            "# Generated with OTLEnumerationCreator. To modify: extend, do not edit",
            "class KlAIMToestand(KeuzelijstField):",
            '    """Keuzelijst met fasen uit de levenscyclus van een object om de toestand op een moment mee vast te leggen."""',
            "    naam = 'KlAIMToestand'",
            "    label = 'AIM toestand'",
            "    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#KlAIMToestand'",
            "    definition = 'Keuzelijst met fasen uit de levenscyclus van een object om de toestand op een moment mee vast te leggen.'",
            "    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlAIMToestand'",
            "    options = {",
            "        'geannuleerd': KeuzelijstWaarde(invulwaarde='geannuleerd',",
            "                                        label='geannuleerd',",
            "                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAIMToestand/geannuleerd'),",
            "        'gepland': KeuzelijstWaarde(invulwaarde='gepland',",
            "                                    label='gepland',",
            "                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAIMToestand/gepland'),",
            "        'in-gebruik': KeuzelijstWaarde(invulwaarde='in-gebruik',",
            "                                       label='in gebruik',",
            "                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAIMToestand/in-gebruik'),",
            "        'in-ontwerp': KeuzelijstWaarde(invulwaarde='in-ontwerp',",
            "                                       label='in ontwerp',",
            "                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAIMToestand/in-ontwerp'),",
            "        'in-opbouw': KeuzelijstWaarde(invulwaarde='in-opbouw',",
            "                                      label='in opbouw',",
            "                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAIMToestand/in-opbouw'),",
            "        'overgedragen': KeuzelijstWaarde(invulwaarde='overgedragen',",
            "                                         label='overgedragen',",
            "                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAIMToestand/overgedragen'),",
            "        'uit-gebruik': KeuzelijstWaarde(invulwaarde='uit-gebruik',",
            "                                        label='uit gebruik',",
            "                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAIMToestand/uit-gebruik'),",
            "        'verwijderd': KeuzelijstWaarde(invulwaarde='verwijderd',",
            "                                       label='verwijderd',",
            "                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAIMToestand/verwijderd')",
            "    }",
            ""]


class TestOTLEnumerationCreator(OTLEnumerationCreator):
    def __init__(self, logger, collector):
        super().__init__(logger, collector)


class OTLEnumerationCreatorTests(unittest.TestCase):
    @patch.object(NoneLogger, "log")
    def test_InitOTLModelCreator(self, mock):
        logger = NoneLogger()
        collector = OSLOCollector(mock)
        creator = OTLEnumerationCreator(logger, collector)
        self.assertTrue(mock.called)

    def test_InvalidOSLOEnumerationEmptyUri(self):
        logger = NoneLogger()
        collector = OSLOCollector(mock)
        creator = OTLEnumerationCreator(logger, collector)
        osloEnumeration = OSLOEnumeration(name='name', objectUri='', definition='', label='', usagenote='',
                                          deprecated_version='', codelist='')

        with self.assertRaises(ValueError) as exception_empty_uri:
            creator.CreateBlockToWriteFromEnumerations(osloEnumeration)
        self.assertEqual(str(exception_empty_uri.exception), "OSLOEnumeration.objectUri is invalid. Value = ''")

    def test_InvalidOSLOEnumerationBadUri(self):
        logger = NoneLogger()
        collector = OSLOCollector(mock)
        creator = OTLEnumerationCreator(logger, collector)
        osloEnumeration = OSLOEnumeration(name='name', objectUri='Bad objectUri', definition='', label='', usagenote='',
                                          deprecated_version='', codelist='')

        with self.assertRaises(ValueError) as exception_bad_uri:
            creator.CreateBlockToWriteFromEnumerations(osloEnumeration)
        self.assertEqual(str(exception_bad_uri.exception), "OSLOEnumeration.objectUri is invalid. Value = 'Bad objectUri'")

    def test_InvalidOSLOEnumerationEmptyName(self):
        logger = NoneLogger()
        collector = OSLOCollector(mock)
        creator = OTLEnumerationCreator(logger, collector)
        osloEnumeration = OSLOEnumeration(name='',
                                          objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#KwantWrd',
                                          definition='', label='', usagenote='',
                                          deprecated_version='', codelist='')

        with self.assertRaises(ValueError) as exception_bad_name:
            creator.CreateBlockToWriteFromEnumerations(osloEnumeration)
        self.assertEqual(str(exception_bad_name.exception), "OSLOEnumeration.name is invalid. Value = ''")

    def test_InValidType(self):
        bad_primitive = True
        logger = NoneLogger()
        collector = OSLOCollector(mock)
        creator = OTLEnumerationCreator(logger, collector)
        with self.assertRaises(ValueError) as exception_bad_name:
            creator.CreateBlockToWriteFromEnumerations(bad_primitive)
        self.assertEqual(str(exception_bad_name.exception), "Input is not a OSLOEnumeration")

    def test_KlAIMToestandOSLOEnumeration(self):
        logger = NoneLogger()
        collector = EnumerationOSLOCollector(mock)
        creator = OTLEnumerationCreator(logger, collector)
        KlAIMToestand = collector.find_enumeration_by_uri(
            'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#KlAIMToestand')
        dataToWrite = creator.CreateBlockToWriteFromEnumerations(KlAIMToestand)

        self.assertEqual(collector.expectedDataKlAIMToestand, dataToWrite)

    def test_getKeuzelijstWaardesFromUri(self):
        logger = NoneLogger()
        collector = EnumerationOSLOCollector(mock)
        creator = OTLEnumerationCreator(logger, collector)
        KlAIMToestand = collector.find_enumeration_by_uri(
            'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#KlAIMToestand')
        lijst = creator.get_keuzelijstwaardes_by_name(KlAIMToestand.name)

        self.assertTrue(len(lijst) >= 1)
        self.assertTrue(isinstance(lijst[0], KeuzelijstWaarde))

    def test_WriteToFileOSLOEnumeration(self):
        logger = NoneLogger()
        collector = EnumerationOSLOCollector(mock)
        creator = OTLEnumerationCreator(logger, collector)
        KlAIMToestand = collector.find_enumeration_by_uri(
            'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#KlAIMToestand')
        dataToWrite = creator.CreateBlockToWriteFromEnumerations(KlAIMToestand)
        creator.writeToFile(KlAIMToestand, 'Datatypes', dataToWrite, '../../src/OTLMOW/')

        filelocation = os.path.abspath(os.path.join(os.sep, ROOT_DIR, 'src/OTLMOW/OTLModel/Datatypes/KlAIMToestand.py'))
        self.assertTrue(os.path.isfile(filelocation))

    def test_WriteToFileOSLOEnumeration2(self):
        logger = NoneLogger()

        base_dir = os.path.dirname(os.path.realpath(__file__))
        file_location = f'{base_dir}/../../src/OTLMOW/InputFiles/OTL.db'
        sql_reader = SQLDbReader(file_location)
        oslo_creator = OSLOInMemoryCreator(sql_reader)
        collector = OSLOCollector(oslo_creator)
        collector.collect()

        creator = OTLEnumerationCreator(logger, collector)
        KlAIMToestand = collector.find_enumeration_by_uri(
            'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#KlAlgProvincie')
        dataToWrite = creator.CreateBlockToWriteFromEnumerations(KlAIMToestand)
        creator.writeToFile(KlAIMToestand, 'Datatypes', dataToWrite, '../../src/OTLMOW/')

        filelocation = os.path.abspath(os.path.join(os.sep, ROOT_DIR, 'src/OTLMOW/OTLModel/Datatypes/KlAlgProvincie.py'))
        self.assertTrue(os.path.isfile(filelocation))

    def test_getKeuzelijstWaardesFromUri2(self):
        logger = NoneLogger()

        base_dir = os.path.dirname(os.path.realpath(__file__))
        file_location = f'{base_dir}/../../src/OTLMOW/InputFiles/OTL.db'
        sql_reader = SQLDbReader(file_location)
        oslo_creator = OSLOInMemoryCreator(sql_reader)
        collector = OSLOCollector(oslo_creator)
        collector.collect()

        creator = OTLEnumerationCreator(logger, collector)
        keuzelijst = creator.get_keuzelijstwaardes_by_name("KlAIMToestand")

        self.assertTrue(len(keuzelijst) > 0)
        inontwerp_waarde = next(k for k in keuzelijst if k.invulwaarde == 'in-ontwerp')
        self.assertEqual('in-ontwerp', inontwerp_waarde.invulwaarde)
        self.assertEqual('in ontwerp', inontwerp_waarde.label)
        self.assertEqual('', inontwerp_waarde.definitie)
        self.assertEqual('https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAIMToestand/in-ontwerp', inontwerp_waarde.objectUri)
        pass

    def test_get_keuzelijstwaardes_from_graph(self):
        base_dir = os.path.dirname(os.path.realpath(__file__))
        file_location = f'{base_dir}/AntiParkeerpaalType.ttl'
        g = rdflib.Graph()
        g.parse(file_location, format="turtle")
        list = OTLEnumerationCreator.get_keuzelijstwaardes_from_graph(g)
        self.assertEqual(2, len(list))

    def test_get_keuzelijstwaardes_from_graph_new_format(self):
        base_dir = os.path.dirname(os.path.realpath(__file__))
        file_location = f'{base_dir}/new_format_ttl.ttl'
        g = rdflib.Graph()
        g.parse(file_location, format="turtle")
        list = OTLEnumerationCreator.get_keuzelijstwaardes_from_graph(g)
        self.assertEqual(2, len(list))
        pass

