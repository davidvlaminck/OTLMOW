import os
import unittest
from unittest import mock

from OTLMOW.ModelGenerator.OSLOCollector import OSLOCollector
from OTLMOW.ModelGenerator.OSLODatatypeComplex import OSLODatatypeComplex
from OTLMOW.ModelGenerator.OSLOInMemoryCreator import OSLOInMemoryCreator
from OTLMOW.ModelGenerator.OTLComplexDatatypeCreator import OTLComplexDatatypeCreator
from OTLMOW.ModelGenerator.SQLDbReader import SQLDbReader

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

expectedDtc = ["# coding=utf-8",
               "from OTLMOW.OTLModel.BaseClasses.AttributeInfo import AttributeInfo",
               "from OTLMOW.OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut",
               "from OTLMOW.OTLModel.Datatypes.ComplexField import ComplexField",
               "from OTLMOW.OTLModel.Datatypes.StringField import StringField",
               "",
               "",
               "# Generated with OTLComplexDatatypeCreator. To modify: extend, do not edit",
               "class DtcIdentificatorWaarden(AttributeInfo):",
               "    def __init__(self, parent=None):",
               "        AttributeInfo.__init__(self, parent)",
               "        self._identificator = OTLAttribuut(field=StringField,",
               "                                           naam='identificator',",
               "                                           label='identificator',",
               "                                           objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcIdentificator.identificator',",
               "                                           definition='Een groep van tekens om een AIM object te identificeren of te benoemen.',",
               "                                           owner=self)",
               "",
               "        self._toegekendDoor = OTLAttribuut(field=StringField,",
               "                                           naam='toegekendDoor',",
               "                                           label='toegekend door',",
               "                                           objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcIdentificator.toegekendDoor',",
               "                                           definition='Gegevens van de organisatie die de toekenning deed.',",
               "                                           owner=self)",
               "",
               "    @property",
               "    def identificator(self):",
               '        """Een groep van tekens om een AIM object te identificeren of te benoemen."""',
               "        return self._identificator.get_waarde()",
               "",
               "    @identificator.setter",
               "    def identificator(self, value):",
               "        self._identificator.set_waarde(value, owner=self._parent)",
               "",
               "    @property",
               "    def toegekendDoor(self):",
               '        """Gegevens van de organisatie die de toekenning deed."""',
               "        return self._toegekendDoor.get_waarde()",
               "",
               "    @toegekendDoor.setter",
               "    def toegekendDoor(self, value):",
               "        self._toegekendDoor.set_waarde(value, owner=self._parent)",
               "",
               "",
               "# Generated with OTLComplexDatatypeCreator. To modify: extend, do not edit",
               "class DtcIdentificator(ComplexField, AttributeInfo):",
               '    """Complex datatype voor de identificator van een AIM object volgens de bron van de identificator."""',
               "    naam = 'DtcIdentificator'",
               "    label = 'Identificator'",
               "    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcIdentificator'",
               "    definition = 'Complex datatype voor de identificator van een AIM object volgens de bron van de identificator.'",
               "    waardeObject = DtcIdentificatorWaarden",
               "",
               "    def __str__(self):",
               "        return ComplexField.__str__(self)",
               ""]


class OTLComplexDatatypeCreatorTests(unittest.TestCase):
    def test_InvalidOSLODatatypeComplexEmptyUri(self):
        collector = OSLOCollector(mock)
        creator = OTLComplexDatatypeCreator(collector)
        osloDatatypeComplex = OSLODatatypeComplex(name='name', objectUri='', definition='', label='', usagenote='',
                                                  deprecated_version='')

        with self.assertRaises(ValueError) as exception_empty_uri:
            creator.CreateBlockToWriteFromComplexTypes(osloDatatypeComplex)
        self.assertEqual(str(exception_empty_uri.exception), "OSLODatatypeComplex.objectUri is invalid. Value = ''")

    def test_InvalidOSLODatatypeComplexBadUri(self):
        collector = OSLOCollector(mock)
        creator = OTLComplexDatatypeCreator(collector)
        osloDatatypeComplex = OSLODatatypeComplex(name='name', objectUri='Bad objectUri', definition='', label='',
                                                  usagenote='', deprecated_version='')

        with self.assertRaises(ValueError) as exception_bad_uri:
            creator.CreateBlockToWriteFromComplexTypes(osloDatatypeComplex)
        self.assertEqual(str(exception_bad_uri.exception), "OSLODatatypeComplex.objectUri is invalid. Value = 'Bad objectUri'")

    def test_InvalidOSLODatatypeComplexEmptyName(self):
        collector = OSLOCollector(mock)
        creator = OTLComplexDatatypeCreator(collector)
        osloDatatypeComplex = OSLODatatypeComplex(name='',
                                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcIdentificator',
                                                  definition='', label='', usagenote='', deprecated_version='')

        with self.assertRaises(ValueError) as exception_bad_name:
            creator.CreateBlockToWriteFromComplexTypes(osloDatatypeComplex)
        self.assertEqual(str(exception_bad_name.exception), "OSLODatatypeComplex.name is invalid. Value = ''")

    def test_InValidType(self):
        bad_Complex = True
        collector = OSLOCollector(mock)
        creator = OTLComplexDatatypeCreator(collector)
        with self.assertRaises(ValueError) as exception_bad_name:
            creator.CreateBlockToWriteFromComplexTypes(bad_Complex)
        self.assertEqual(str(exception_bad_name.exception), "Input is not a OSLODatatypeComplex")

    def setUp(self) -> OSLOCollector:
        base_dir = os.path.dirname(os.path.realpath(__file__))
        file_location = f'{base_dir}/../OTL_AllCasesTestClass.db'
        sql_reader = SQLDbReader(file_location)
        oslo_creator = OSLOInMemoryCreator(sql_reader)
        collector = OSLOCollector(oslo_creator)
        collector.collect()
        return collector

    def test_create_block_dtc(self):
        collector = self.setUp()
        creator = OTLComplexDatatypeCreator(collector)
        datatype_complex = collector.find_complex_datatype_by_uri(
            'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcIdentificator')
        data_to_write = creator.create_block_to_write_from_complex_primitive_or_union_types(datatype_complex, typeField='Complex')
        self.assertEqual(expectedDtc, data_to_write)
