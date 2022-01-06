import os
import unittest
from unittest import mock
from unittest.mock import patch

from Loggers.NoneLogger import NoneLogger
from ModelGenerator.FileExistChecker import FileExistChecker
from ModelGenerator.Inheritance import Inheritance
from ModelGenerator.OSLOAttribuut import OSLOAttribuut
from ModelGenerator.OSLOClass import OSLOClass
from ModelGenerator.OSLOCollector import OSLOCollector
from ModelGenerator.OSLOInMemoryCreator import OSLOInMemoryCreator
from ModelGenerator.OSLOTypeLink import OSLOTypeLink
from ModelGenerator.OTLClassCreator import OTLClassCreator
from ModelGenerator.SQLDbReader import SQLDbReader


class ClassOSLOCollector(OSLOCollector):
    def __init__(self, reader):
        super().__init__(reader)

        self.classes = [
            OSLOClass('Gebouw', 'Gebouw', 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Gebouw',
                      'Elk bouwwerk, dat een voor mensen toegankelijke overdekte, geheel of gedeeltelijk met wanden omsloten ruimte vormt.',
                      '', 0, '')]
        self.attributes = [
            OSLOAttribuut('grondplan', 'grondplan',
                          'Plattegrond van het gebouw met aanduidingen van de verschillende aanwezige elementen zoals kelder, kasten met kastnummers, toegangscontrole en meer.',
                          'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Gebouw', '1', '1',
                          'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Gebouw.grondplan',
                          'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcDocument', 0, '', 0, '', '')]
        self.inheritances = [
            Inheritance('Behuizing', 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Behuizing',
                        'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Gebouw', 'Gebouw', '')
        ]

        self.typeLinks = [
            OSLOTypeLink("https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcDocument", "OSLODatatypeComplex",
                         "")
        ]

        self.expectedDataGebouw = ['# coding=utf-8',
                                   'from OTLModel.Classes.Behuizing import Behuizing',
                                   'from OTLModel.Datatypes.DtcDocument import DtcDocument',
                                   '',
                                   '',
                                   '# Generated with OTLClassCreator. To modify: extend, do not edit',
                                   'class Gebouw(Behuizing):',
                                   '    """Elk bouwwerk, dat een voor mensen toegankelijke overdekte, geheel of gedeeltelijk met wanden omsloten ruimte vormt."""',
                                   '',
                                   '    typeURI = "https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Gebouw"',
                                   '    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""',
                                   '',
                                   '    def __init__(self):',
                                   '        super().__init__()',
                                   '',
                                   '        self.grondplan = DtcDocument()',
                                   '        """Plattegrond van het gebouw met aanduidingen van de verschillende aanwezige elementen zoals kelder, kasten met kastnummers, toegangscontrole en meer."""',
                                   '        self.grondplan.naam = "grondplan"',
                                   '        self.grondplan.label = "grondplan"',
                                   '        self.grondplan.uri = "https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Gebouw.grondplan"',
                                   '        self.grondplan.definition = "Plattegrond van het gebouw met aanduidingen van de verschillende aanwezige elementen zoals kelder, kasten met kastnummers, toegangscontrole en meer."',
                                   '        self.grondplan.constraints = ""',
                                   '        self.grondplan.usagenote = ""',
                                   '        self.grondplan.deprecated_version = ""']


class TestOTLClassCreator(OTLClassCreator):
    def __init__(self, logger, collector):
        super().__init__(logger, collector)


class OTLClassCreatorTests(unittest.TestCase):
    @patch.object(NoneLogger, "log")
    def test_InitOTLModelCreator(self, mock):
        logger = NoneLogger()
        collector = OSLOCollector(mock)
        creator = OTLClassCreator(logger, collector)
        self.assertTrue(mock.called)

    def test_InvalidOSLOClassEmptyUri(self):
        logger = NoneLogger()
        collector = OSLOCollector(mock)
        creator = OTLClassCreator(logger, collector)
        osloClass = OSLOClass(name='name', uri='', definition_nl='', label_nl='', usagenote_nl='', abstract=1,
                              deprecated_version='')

        with self.assertRaises(ValueError) as exception_empty_uri:
            creator.CreateBlockToWriteFromClasses(osloClass)
        self.assertEqual(str(exception_empty_uri.exception), "OSLOClass.uri is invalid. Value = ''")

    def test_InvalidOSLODatatypeComplexBadUri(self):
        logger = NoneLogger()
        collector = OSLOCollector(mock)
        creator = OTLClassCreator(logger, collector)
        osloClass = OSLOClass(name='name', uri='Bad uri', definition_nl='', label_nl='', usagenote_nl='', abstract=1,
                              deprecated_version='')

        with self.assertRaises(ValueError) as exception_bad_uri:
            creator.CreateBlockToWriteFromClasses(osloClass)
        self.assertEqual(str(exception_bad_uri.exception), "OSLOClass.uri is invalid. Value = 'Bad uri'")

    def test_InvalidOSLODatatypeComplexEmptyName(self):
        logger = NoneLogger()
        collector = OSLOCollector(mock)
        creator = OTLClassCreator(logger, collector)
        osloClass = OSLOClass(name='',
                              uri='https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcIdentificator',
                              definition_nl='', label_nl='', usagenote_nl='', abstract=1,
                              deprecated_version='')

        with self.assertRaises(ValueError) as exception_bad_name:
            creator.CreateBlockToWriteFromClasses(osloClass)
        self.assertEqual(str(exception_bad_name.exception), "OSLOClass.name is invalid. Value = ''")

    def test_InValidType(self):
        bad_Class = True
        logger = NoneLogger()
        collector = OSLOCollector(mock)
        creator = OTLClassCreator(logger, collector)
        with self.assertRaises(ValueError) as exception_bad_name:
            creator.CreateBlockToWriteFromClasses(bad_Class)
        self.assertEqual(str(exception_bad_name.exception), "Input is not a OSLOClass")

    expectedDataContainerBuis = ['# coding=utf-8',
                                 'from abc import abstractmethod, ABC',
                                 'from OTLModel.Datatypes.KardinaliteitField import KardinaliteitField',
                                 'from OTLModel.Datatypes.StringField import StringField',
                                 '',
                                 '',
                                 '# Generated with OTLClassCreator. To modify: extend, do not edit',
                                 'class ContainerBuis(ABC):',
                                 '    """Abstracte voor het groeperen van eigenschappen en relaties van buisvormige container elementen. Dit zijn buizen die kabels of andere leidingen kunnen bevatten."""',
                                 '',
                                 '    typeURI = "https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#ContainerBuis"',
                                 '    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""',
                                 '',
                                 '    @abstractmethod',
                                 '    def __init__(self):',
                                 '        kleurField = StringField(naam="kleur",',
                                 '                                 label="kleur",',
                                 '                                 uri="https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#ContainerBuis.kleur",',
                                 '                                 definition="De kleur van de coating.",',
                                 '                                 constraints="",',
                                 '                                 usagenote="",',
                                 '                                 deprecated_version="")',
                                 '        self.kleur = KardinaliteitField(minKardinaliteit="1", maxKardinaliteit="*", fieldToMultiply=kleurField)',
                                 '        """De kleur van de coating."""']

    def test_ContainerBuis(self):
        logger = NoneLogger()

        file_location = '../../InputFiles/OTL.db'
        file_exist_checker = FileExistChecker(file_location)
        sql_reader = SQLDbReader(file_exist_checker)
        oslo_creator = OSLOInMemoryCreator(sql_reader)
        collector = OSLOCollector(oslo_creator)
        collector.collect()

        creator = OTLClassCreator(logger, collector)
        containerBuis = collector.FindClassByUri('https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#ContainerBuis')
        dataToWrite = creator.CreateBlockToWriteFromClasses(containerBuis)

        self.assertEqual(self.expectedDataContainerBuis, dataToWrite)

    def test_Gebouw_DtcKardMax1(self):
        logger = NoneLogger()
        collector = ClassOSLOCollector(mock)
        creator = OTLClassCreator(logger, collector)
        gebouw = collector.FindClassByUri(
            'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Gebouw')
        dataToWrite = creator.CreateBlockToWriteFromClasses(gebouw)

        self.assertEqual(collector.expectedDataGebouw, dataToWrite)

    def test_WriteToFileContainerBuis(self):
        logger = NoneLogger()

        file_location = '../../InputFiles/OTL.db'
        file_exist_checker = FileExistChecker(file_location)
        sql_reader = SQLDbReader(file_exist_checker)
        oslo_creator = OSLOInMemoryCreator(sql_reader)
        collector = OSLOCollector(oslo_creator)
        collector.collect()

        creator = OTLClassCreator(logger, collector)
        containerBuis = collector.FindClassByUri('https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#ContainerBuis')
        dataToWrite = creator.CreateBlockToWriteFromClasses(containerBuis)
        creator.writeToFile(containerBuis, 'Classes', dataToWrite, '../../')

        self.assertTrue(os.path.isfile('../../OTLModel/Classes/ContainerBuis.py'))

    def test_WriteToFileBuis(self):
        logger = NoneLogger()

        file_location = '../../InputFiles/OTL.db'
        file_exist_checker = FileExistChecker(file_location)
        sql_reader = SQLDbReader(file_exist_checker)
        oslo_creator = OSLOInMemoryCreator(sql_reader)
        collector = OSLOCollector(oslo_creator)
        collector.collect()

        creator = OTLClassCreator(logger, collector)
        buis = collector.FindClassByUri('https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Buis')
        dataToWrite = creator.CreateBlockToWriteFromClasses(buis)
        creator.writeToFile(buis, 'Classes', dataToWrite, '../../')

        self.assertTrue(os.path.isfile('../../OTLModel/Classes/Buis.py'))

    def test_WriteToFileGebouw(self):
        logger = NoneLogger()

        file_location = '../../InputFiles/OTL.db'
        file_exist_checker = FileExistChecker(file_location)
        sql_reader = SQLDbReader(file_exist_checker)
        oslo_creator = OSLOInMemoryCreator(sql_reader)
        collector = OSLOCollector(oslo_creator)
        collector.collect()

        creator = OTLClassCreator(logger, collector)
        containerBuis = collector.FindClassByUri('https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Gebouw')
        dataToWrite = creator.CreateBlockToWriteFromClasses(containerBuis)
        creator.writeToFile(containerBuis, 'Classes', dataToWrite, '../../')

        self.assertTrue(os.path.isfile('../../OTLModel/Classes/Gebouw.py'))
