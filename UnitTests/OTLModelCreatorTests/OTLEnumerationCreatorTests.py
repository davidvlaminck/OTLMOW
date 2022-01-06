import os
import unittest
from unittest import mock
from unittest.mock import patch

from Loggers.NoneLogger import NoneLogger
from ModelGenerator.FileExistChecker import FileExistChecker
from ModelGenerator.OSLOCollector import OSLOCollector
from ModelGenerator.OSLOEnumeration import OSLOEnumeration
from ModelGenerator.OSLOInMemoryCreator import OSLOInMemoryCreator
from ModelGenerator.OTLEnumerationCreator import OTLEnumerationCreator
from ModelGenerator.SQLDbReader import SQLDbReader
from OTLModel.Datatypes.KeuzelijstWaarde import KeuzelijstWaarde


class EnumerationOSLOCollector(OSLOCollector):
    def __init__(self, reader):
        super().__init__(reader)

        self.enumerations = [
            OSLOEnumeration('KlAIMToestand', 'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#KlAIMToestand',
                            '',
                            'Keuzelijst met fasen uit de levenscyclus van een object om de toestand op een moment mee vast te leggen.',
                            'AIM toestand', 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlAIMToestand', '')]

        self.expectedDataKlAIMToestand = ['# coding=utf-8',
                                          'from OTLModel.Datatypes.Keuzelijst import Keuzelijst',
                                          '',
                                          '',
                                          '# Generated with OTLEnumerationCreator. To modify: extend, do not edit',
                                          'class KlAIMToestand(Keuzelijst):',
                                          '    """Keuzelijst met fasen uit de levenscyclus van een object om de toestand op een moment mee vast te leggen."""',
                                          '',
                                          '    def __init__(self):',
                                          '        super().__init__(naam="KlAIMToestand",',
                                          '                         label="AIM toestand",',
                                          '                         uri="https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#KlAIMToestand",',
                                          '                         definition="Keuzelijst met fasen uit de levenscyclus van een object om de toestand op een moment mee vast te leggen.",',
                                          '                         usagenote="",',
                                          '                         deprecated_version="",',
                                          '                         codelist="https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlAIMToestand")',
                                          '',
                                          '        self.add_option("in-ontwerp", "in ontwerp", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAIMToestand/in-ontwerp")',
                                          '        self.add_option("gepland", "gepland", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAIMToestand/gepland")',
                                          '        self.add_option("in-opbouw", "in opbouw", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAIMToestand/in-opbouw")',
                                          '        self.add_option("geannuleerd", "geannuleerd", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAIMToestand/geannuleerd")',
                                          '        self.add_option("in-gebruik", "in gebruik", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAIMToestand/in-gebruik")',
                                          '        self.add_option("overgedragen", "overgedragen", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAIMToestand/overgedragen")',
                                          '        self.add_option("uit-gebruik", "uit gebruik", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAIMToestand/uit-gebruik")',
                                          '        self.add_option("verwijderd", "verwijderd", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAIMToestand/verwijderd")']


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
        osloEnumeration = OSLOEnumeration(name='name', uri='', definition_nl='', label_nl='', usagenote_nl='',
                                          deprecated_version='', codelist='')

        with self.assertRaises(ValueError) as exception_empty_uri:
            creator.CreateBlockToWriteFromEnumerations(osloEnumeration)
        self.assertEqual(str(exception_empty_uri.exception), "OSLOEnumeration.uri is invalid. Value = ''")

    def test_InvalidOSLOEnumerationBadUri(self):
        logger = NoneLogger()
        collector = OSLOCollector(mock)
        creator = OTLEnumerationCreator(logger, collector)
        osloEnumeration = OSLOEnumeration(name='name', uri='Bad uri', definition_nl='', label_nl='', usagenote_nl='',
                                          deprecated_version='', codelist='')

        with self.assertRaises(ValueError) as exception_bad_uri:
            creator.CreateBlockToWriteFromEnumerations(osloEnumeration)
        self.assertEqual(str(exception_bad_uri.exception), "OSLOEnumeration.uri is invalid. Value = 'Bad uri'")

    def test_InvalidOSLOEnumerationEmptyName(self):
        logger = NoneLogger()
        collector = OSLOCollector(mock)
        creator = OTLEnumerationCreator(logger, collector)
        osloEnumeration = OSLOEnumeration(name='',
                                          uri='https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#KwantWrd',
                                          definition_nl='', label_nl='', usagenote_nl='',
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

    def test_KwantWrdInVoltOSLOEnumeration(self):
        logger = NoneLogger()
        collector = EnumerationOSLOCollector(mock)
        creator = OTLEnumerationCreator(logger, collector)
        KlAIMToestand = collector.FindEnumerationByUri(
            'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#KlAIMToestand')
        dataToWrite = creator.CreateBlockToWriteFromEnumerations(KlAIMToestand)

        self.assertEqual(collector.expectedDataKlAIMToestand, dataToWrite)

    def test_getKeuzelijstWaardesFromUri(self):
        logger = NoneLogger()
        collector = EnumerationOSLOCollector(mock)
        creator = OTLEnumerationCreator(logger, collector)
        KlAIMToestand = collector.FindEnumerationByUri(
            'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#KlAIMToestand')
        lijst = creator.getKeuzelijstWaardesFromUri(KlAIMToestand.name)

        self.assertTrue(len(lijst) >= 1)
        self.assertTrue(isinstance(lijst[0], KeuzelijstWaarde))

    def test_WriteToFileOSLOEnumeration(self):
        logger = NoneLogger()
        collector = EnumerationOSLOCollector(mock)
        creator = OTLEnumerationCreator(logger, collector)
        KlAIMToestand = collector.FindEnumerationByUri(
            'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#KlAIMToestand')
        dataToWrite = creator.CreateBlockToWriteFromEnumerations(KlAIMToestand)
        creator.writeToFile(KlAIMToestand, 'Datatypes', dataToWrite, '../../')

        self.assertTrue(os.path.isfile('../../OTLModel/Datatypes/KlAIMToestand.py'))

    def test_test_WriteToFileOSLOEnumeration2(self):
        logger = NoneLogger()

        file_location = '../../InputFiles/OTL.db'
        file_exist_checker = FileExistChecker(file_location)
        sql_reader = SQLDbReader(file_exist_checker)
        oslo_creator = OSLOInMemoryCreator(sql_reader)
        collector = OSLOCollector(oslo_creator)
        collector.collect()

        creator = OTLEnumerationCreator(logger, collector)
        KlAIMToestand = collector.FindEnumerationByUri(
            'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#KlAlgProvincie')
        dataToWrite = creator.CreateBlockToWriteFromEnumerations(KlAIMToestand)
        creator.writeToFile(KlAIMToestand, 'Datatypes', dataToWrite, '../../')

        self.assertTrue(os.path.isfile('../../OTLModel/Datatypes/KlAlgProvincie.py'))
