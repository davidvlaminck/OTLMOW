import os
import unittest
from unittest import mock
from unittest.mock import patch

from OTLMOW.GeometrieArtefact.GeometrieArtefactCollector import GeometrieArtefactCollector
from OTLMOW.GeometrieArtefact.GeometrieType import GeometrieType
from OTLMOW.Loggers.NoneLogger import NoneLogger
from OTLMOW.ModelGenerator.Inheritance import Inheritance
from OTLMOW.ModelGenerator.OSLOAttribuut import OSLOAttribuut
from OTLMOW.ModelGenerator.OSLOClass import OSLOClass
from OTLMOW.ModelGenerator.OSLOCollector import OSLOCollector
from OTLMOW.ModelGenerator.OSLOInMemoryCreator import OSLOInMemoryCreator
from OTLMOW.ModelGenerator.OSLOTypeLink import OSLOTypeLink
from OTLMOW.ModelGenerator.OTLClassCreator import OTLClassCreator
from OTLMOW.ModelGenerator.SQLDbReader import SQLDbReader

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


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
                                   'from OTLMOW.OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut',
                                   'from OTLMOW.OTLModel.Classes.Behuizing import Behuizing',
                                   'from OTLMOW.OTLModel.Datatypes.DtcDocument import DtcDocument',
                                   'from OTLMOW.GeometrieArtefact.VlakGeometrie import VlakGeometrie',
                                   '',
                                   '',
                                   '# Generated with OTLClassCreator. To modify: extend, do not edit',
                                   "class Gebouw(Behuizing, VlakGeometrie):",
                                   '    """Elk bouwwerk, dat een voor mensen toegankelijke overdekte, geheel of gedeeltelijk met wanden omsloten ruimte vormt."""',
                                   "",
                                   "    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Gebouw'",
                                   '    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""',
                                   "",
                                   "    def __init__(self):",
                                   '        Behuizing.__init__(self)',
                                   '        VlakGeometrie.__init__(self)',
                                   "",
                                   "        self._grondplan = OTLAttribuut(field=DtcDocument,",
                                   "                                       naam='grondplan',",
                                   "                                       label='grondplan',",
                                   "                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Gebouw.grondplan',",
                                   "                                       definition='Plattegrond van het gebouw met aanduidingen van de verschillende aanwezige elementen zoals kelder, kasten met kastnummers, toegangscontrole en meer.',",
                                   "                                       owner=self)",
                                   "",
                                   "    @property",
                                   "    def grondplan(self):",
                                   '        """Plattegrond van het gebouw met aanduidingen van de verschillende aanwezige elementen zoals kelder, kasten met kastnummers, toegangscontrole en meer."""',
                                   "        return self._grondplan.waarde",
                                   "",
                                   "    @grondplan.setter",
                                   "    def grondplan(self, value):",
                                   "        self._grondplan.set_waarde(value, owner=self)"]


class TestOTLClassCreator(OTLClassCreator):
    def __init__(self, logger, collector):
        super().__init__(logger, collector)


class GeometrieArtefactCollectorDouble:
    def __init__(self):
        self.geometrie_types = [GeometrieType(objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Gebouw',
                                              label_nl='Gebouw',
                                              geen_geometrie=0, punt3D=0, lijn3D=0,
                                              polygoon3D=1)]


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
        osloClass = OSLOClass(name='name', objectUri='', definition='', label='', usagenote='', abstract=1,
                              deprecated_version='')

        with self.assertRaises(ValueError) as exception_empty_uri:
            creator.create_blocks_to_write_from_classes(osloClass)
        self.assertEqual(str(exception_empty_uri.exception), "OSLOClass.objectUri is invalid. Value = ''")

    def test_InvalidOSLODatatypeComplexBadUri(self):
        logger = NoneLogger()
        collector = OSLOCollector(mock)
        creator = OTLClassCreator(logger, collector)
        osloClass = OSLOClass(name='name', objectUri='Bad objectUri', definition='', label='', usagenote='', abstract=1,
                              deprecated_version='')

        with self.assertRaises(ValueError) as exception_bad_uri:
            creator.create_blocks_to_write_from_classes(osloClass)
        self.assertEqual(str(exception_bad_uri.exception), "OSLOClass.objectUri is invalid. Value = 'Bad objectUri'")

    def test_InvalidOSLODatatypeComplexEmptyName(self):
        logger = NoneLogger()
        collector = OSLOCollector(mock)
        creator = OTLClassCreator(logger, collector)
        osloClass = OSLOClass(name='',
                              objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcIdentificator',
                              definition='', label='', usagenote='', abstract=1,
                              deprecated_version='')

        with self.assertRaises(ValueError) as exception_bad_name:
            creator.create_blocks_to_write_from_classes(osloClass)
        self.assertEqual(str(exception_bad_name.exception), "OSLOClass.name is invalid. Value = ''")

    def test_InValidType(self):
        bad_Class = True
        logger = NoneLogger()
        collector = OSLOCollector(mock)
        creator = OTLClassCreator(logger, collector)
        with self.assertRaises(ValueError) as exception_bad_name:
            creator.create_blocks_to_write_from_classes(bad_Class)
        self.assertEqual(str(exception_bad_name.exception), "Input is not a OSLOClass")

    expectedDataContainerBuis = ['# coding=utf-8',
                                 'from OTLMOW.OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut',
                                 'from abc import abstractmethod, ABC',
                                 'from OTLMOW.OTLModel.Datatypes.StringField import StringField',
                                 '',
                                 '',
                                 '# Generated with OTLClassCreator. To modify: extend, do not edit',
                                 'class ContainerBuis(ABC):',
                                 '    """Abstracte voor het groeperen van eigenschappen en relaties van buisvormige container elementen. Dit zijn buizen die kabels of andere leidingen kunnen bevatten."""',
                                 '',
                                 "    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#ContainerBuis'",
                                 '    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""',
                                 '',
                                 '    @abstractmethod',
                                 '    def __init__(self):',
                                 '        self._kleur = OTLAttribuut(field=StringField,',
                                 "                                   naam='kleur',",
                                 "                                   label='kleur',",
                                 "                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#ContainerBuis.kleur',",
                                 "                                   kardinaliteit_max='*',",
                                 "                                   definition='De kleur van de coating.',",
                                 "                                   owner=self)",
                                 '',
                                 '    @property',
                                 '    def kleur(self):',
                                 '        """De kleur van de coating."""',
                                 '        return self._kleur.waarde',
                                 '',
                                 '    @kleur.setter',
                                 '    def kleur(self, value):',
                                 '        self._kleur.set_waarde(value, owner=self)']

    def test_ContainerBuis(self):
        collector, creator = self.set_up_real_collector_and_creator()
        containerBuis = collector.find_class_by_uri('https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#ContainerBuis')
        dataToWrite = creator.create_blocks_to_write_from_classes(containerBuis)

        self.assertEqual(self.expectedDataContainerBuis, dataToWrite)

    def test_Gebouw_DtcKardMax1(self):
        logger = NoneLogger()
        collector = ClassOSLOCollector(mock)
        geo_collector = GeometrieArtefactCollectorDouble()
        creator = OTLClassCreator(logger, collector, None)
        creator.geometry_types = geo_collector.geometrie_types
        gebouw = collector.find_class_by_uri('https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Gebouw')
        dataToWrite = creator.create_blocks_to_write_from_classes(gebouw)

        self.assertEqual(collector.expectedDataGebouw, dataToWrite)

    def test_WriteToFileContainerBuis(self):
        collector, creator = self.set_up_real_collector_and_creator()
        containerBuis = collector.find_class_by_uri('https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#ContainerBuis')
        dataToWrite = creator.create_blocks_to_write_from_classes(containerBuis)
        creator.writeToFile(containerBuis, 'Classes', dataToWrite, '../../src/OTLMOW/')

        filelocation = os.path.abspath(os.path.join(os.sep, ROOT_DIR, 'src/OTLMOW/OTLModel/Classes/ContainerBuis.py'))
        self.assertTrue(os.path.isfile(filelocation))

    def test_WriteToFileBuis(self):
        collector, creator = self.set_up_real_collector_and_creator()
        buis = collector.find_class_by_uri('https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Buis')
        dataToWrite = creator.create_blocks_to_write_from_classes(buis)
        creator.writeToFile(buis, 'Classes', dataToWrite, '../../src/OTLMOW/')

        filelocation = os.path.abspath(os.path.join(os.sep, ROOT_DIR, 'src/OTLMOW/OTLModel/Classes/Buis.py'))
        self.assertTrue(os.path.isfile(filelocation))

    def test_WriteToFileGebouw(self):
        collector, creator = self.set_up_real_collector_and_creator()
        containerBuis = collector.find_class_by_uri('https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Gebouw')
        dataToWrite = creator.create_blocks_to_write_from_classes(containerBuis)
        creator.writeToFile(containerBuis, 'Classes', dataToWrite, '../../src/OTLMOW/')

        filelocation = os.path.abspath(os.path.join(os.sep, ROOT_DIR, 'src/OTLMOW/OTLModel/Classes/Gebouw.py'))
        self.assertTrue(os.path.isfile(filelocation))

    def test_CheckInheritances_Agent(self):
        collector, creator = self.set_up_real_collector_and_creator()

        agent = collector.find_class_by_uri('http://purl.org/dc/terms/Agent')
        dataToWrite = creator.create_blocks_to_write_from_classes(agent)
        inheritanceLine = "class Agent(AttributeInfo, OTLObject, RelatieInteractor):"

        self.assertEqual(inheritanceLine, dataToWrite[11])

    def test_CheckInheritances_AIMObject(self):
        collector, creator = self.set_up_real_collector_and_creator()

        aimObject = collector.find_class_by_uri('https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#AIMObject')
        dataToWrite = creator.create_blocks_to_write_from_classes(aimObject)
        inheritanceLine = "class AIMObject(AIMToestand, AIMDBStatus, AttributeInfo, OTLAsset, RelatieInteractor):"

        self.assertEqual(inheritanceLine, dataToWrite[15])

    def test_CheckInheritances_RelatieObject(self):
        collector, creator = self.set_up_real_collector_and_creator()

        relatieObject = collector.find_class_by_uri(
            'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#RelatieObject')
        dataToWrite = creator.create_blocks_to_write_from_classes(relatieObject)
        inheritanceLine = "class RelatieObject(AIMDBStatus, AttributeInfo, OTLObject):"

        self.assertEqual(inheritanceLine, dataToWrite[10])

    def test_CheckInheritances_DerdenObject(self):
        collector, creator = self.set_up_real_collector_and_creator()

        derdenobject = collector.find_class_by_uri('https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#Derdenobject')
        dataToWrite = creator.create_blocks_to_write_from_classes(derdenobject)
        inheritanceLine = "class Derdenobject(AIMToestand, AIMDBStatus, AttributeInfo, OTLAsset, RelatieInteractor):"

        self.assertEqual(inheritanceLine, dataToWrite[14])

    @staticmethod
    def set_up_real_collector_and_creator():
        logger = NoneLogger()
        base_dir = os.path.dirname(os.path.realpath(__file__))
        file_location = f'{base_dir}/../../src/OTLMOW/InputFiles/OTL.db'
        sql_reader = SQLDbReader(file_location)
        oslo_creator = OSLOInMemoryCreator(sql_reader)
        collector = OSLOCollector(oslo_creator)
        collector.collect()
        creator = OTLClassCreator(logger, collector)
        return collector, creator
