import os
import unittest
from unittest import mock

import rdflib

from OTLMOW.ModelGenerator.OSLOCollector import OSLOCollector
from OTLMOW.ModelGenerator.OSLOEnumeration import OSLOEnumeration
from OTLMOW.ModelGenerator.OSLOInMemoryCreator import OSLOInMemoryCreator
from OTLMOW.ModelGenerator.OTLEnumerationCreator import OTLEnumerationCreator
from OTLMOW.ModelGenerator.SQLDbReader import SQLDbReader
from OTLMOW.OTLModel.Datatypes.KeuzelijstWaarde import KeuzelijstWaarde

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

expectedKeuzelijst = ['# coding=utf-8',
                      'import random',
                      'from OTLMOW.OTLModel.Datatypes.KeuzelijstField import KeuzelijstField',
                      'from OTLMOW.OTLModel.Datatypes.KeuzelijstWaarde import KeuzelijstWaarde',
                      '',
                      '',
                      '# Generated with OTLEnumerationCreator. To modify: extend, do not edit',
                      'class KlTestKeuzelijst(KeuzelijstField):',
                      '    """Keuzelijst met test waarden."""',
                      "    naam = 'KlTestKeuzelijst'",
                      "    label = 'Test keuzelijst'",
                      '    objectUri = '
                      "'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#KlTestKeuzelijst'",
                      "    definition = 'Keuzelijst met test waarden.'",
                      '    codelist = '
                      "'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlTestKeuzelijst'",
                      '    options = {',
                      "        'waarde-1': KeuzelijstWaarde(invulwaarde='waarde-1',",
                      "                                     label='waarde 1',",
                      '                                     '
                      "objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlTestKeuzelijst/waarde-1'),",
                      "        'waarde-2': KeuzelijstWaarde(invulwaarde='waarde-2',",
                      "                                     label='waarde 2',",
                      '                                     '
                      "objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlTestKeuzelijst/waarde-2'),",
                      "        'waarde-3': KeuzelijstWaarde(invulwaarde='waarde-3',",
                      "                                     label='waarde 3',",
                      '                                     '
                      "objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlTestKeuzelijst/waarde-3')",
                      '    }',
                      '',
                      '    @classmethod',
                      '    def get_dummy_data(cls):',
                      '        return random.choice(list(cls.options.keys()))',
                      '',
                      '    @staticmethod',
                      '    def create_dummy_data():',
                      '        return KlTestKeuzelijst.get_dummy_data()',
                      '']


class OTLEnumerationCreatorTests(unittest.TestCase):
    def test_InvalidOSLOEnumerationEmptyUri(self):
        collector = OSLOCollector(mock)
        creator = OTLEnumerationCreator(collector)
        osloEnumeration = OSLOEnumeration(name='name', objectUri='', definition='', label='', usagenote='',
                                          deprecated_version='', codelist='')

        with self.assertRaises(ValueError) as exception_empty_uri:
            creator.create_block_to_write_from_enumerations(osloEnumeration)
        self.assertEqual(str(exception_empty_uri.exception), "OSLOEnumeration.objectUri is invalid. Value = ''")

    def test_InvalidOSLOEnumerationBadUri(self):
        collector = OSLOCollector(mock)
        creator = OTLEnumerationCreator(collector)
        osloEnumeration = OSLOEnumeration(name='name', objectUri='Bad objectUri', definition='', label='', usagenote='',
                                          deprecated_version='', codelist='')

        with self.assertRaises(ValueError) as exception_bad_uri:
            creator.create_block_to_write_from_enumerations(osloEnumeration)
        self.assertEqual(str(exception_bad_uri.exception), "OSLOEnumeration.objectUri is invalid. Value = 'Bad objectUri'")

    def test_InvalidOSLOEnumerationEmptyName(self):
        collector = OSLOCollector(mock)
        creator = OTLEnumerationCreator(collector)
        osloEnumeration = OSLOEnumeration(name='',
                                          objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#KwantWrd',
                                          definition='', label='', usagenote='',
                                          deprecated_version='', codelist='')

        with self.assertRaises(ValueError) as exception_bad_name:
            creator.create_block_to_write_from_enumerations(osloEnumeration)
        self.assertEqual(str(exception_bad_name.exception), "OSLOEnumeration.name is invalid. Value = ''")

    def test_InValidType(self):
        bad_primitive = True
        collector = OSLOCollector(mock)
        creator = OTLEnumerationCreator(collector)
        with self.assertRaises(ValueError) as exception_bad_name:
            creator.create_block_to_write_from_enumerations(bad_primitive)
        self.assertEqual(str(exception_bad_name.exception), "Input is not a OSLOEnumeration")

    def setUp(self) -> OSLOCollector:
        base_dir = os.path.dirname(os.path.realpath(__file__))
        file_location = f'{base_dir}/../OTL_AllCasesTestClass.db'
        sql_reader = SQLDbReader(file_location)
        oslo_creator = OSLOInMemoryCreator(sql_reader)
        collector = OSLOCollector(oslo_creator)
        collector.collect()
        return collector

    def test_KlTestKeuzelijst(self):
        collector = self.setUp()
        creator = OTLEnumerationCreator(collector)
        KlAIMToestand = collector.find_enumeration_by_uri(
            'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#KlTestKeuzelijst')
        dataToWrite = creator.create_block_to_write_from_enumerations(KlAIMToestand)

        self.assertListEqual(expectedKeuzelijst, dataToWrite)

    def test_get_keuzelijstwaardes_by_name(self):
        collector = self.setUp()
        creator = OTLEnumerationCreator(collector)
        keuzelijst = collector.find_enumeration_by_uri(
            'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#KlTestKeuzelijst')
        keuzelijst_waarden = creator.get_keuzelijstwaardes_by_name(keuzelijst.name)
        self.assertTrue(len(keuzelijst_waarden) > 0)
        self.assertIsInstance(keuzelijst_waarden[0], KeuzelijstWaarde)

        waarde_2 = next(k for k in keuzelijst_waarden if k.invulwaarde == 'waarde-2')
        self.assertEqual('waarde-2', waarde_2.invulwaarde)
        self.assertEqual('waarde 2', waarde_2.label)
        self.assertEqual('', waarde_2.definitie)
        self.assertEqual('https://wegenenverkeer.data.vlaanderen.be/id/concept/KlTestKeuzelijst/waarde-2',
                         waarde_2.objectUri)

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
