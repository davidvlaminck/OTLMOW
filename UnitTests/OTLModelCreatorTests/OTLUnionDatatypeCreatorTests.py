import os
import unittest
from unittest.mock import MagicMock

from OTLMOW.ModelGenerator.OSLOCollector import OSLOCollector
from OTLMOW.ModelGenerator.OSLODatatypeUnion import OSLODatatypeUnion
from OTLMOW.ModelGenerator.OSLOInMemoryCreator import OSLOInMemoryCreator
from OTLMOW.ModelGenerator.OTLUnionDatatypeCreator import OTLUnionDatatypeCreator
from OTLMOW.ModelGenerator.SQLDbReader import SQLDbReader

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

expectedDtu = ['# coding=utf-8',
               'from OTLMOW.OTLModel.BaseClasses.AttributeInfo import AttributeInfo',
               'from OTLMOW.OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut',
               'from OTLMOW.OTLModel.Datatypes.KwantWrdTest import KwantWrdTest',
               'from OTLMOW.OTLModel.Datatypes.StringField import StringField',
               'from OTLMOW.OTLModel.Datatypes.UnionTypeField import UnionTypeField',
               'from OTLMOW.OTLModel.Datatypes.UnionWaarden import UnionWaarden',
               '',
               '',
               '# Generated with OTLUnionDatatypeCreator. To modify: extend, do not edit',
               'class DtuTestUnionTypeWaarden(AttributeInfo, UnionWaarden):',
               '    def __init__(self, parent=None):',
               '        AttributeInfo.__init__(self, parent)',
               '        UnionWaarden.__init__(self)',
               '        self._unionKwantWrd = OTLAttribuut(field=KwantWrdTest,',
               "                                           naam='unionKwantWrd',",
               "                                           label='Union kwantitatieve "
               "waarde',",
               '                                           '
               "objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtuTestUnionType.unionKwantWrd',",
               "                                           kardinaliteit_min='0',",
               "                                           definition='Kwantitatieve waarde "
               "van het test Union datatype',",
               '                                           owner=self)',
               '',
               '        self._unionString = OTLAttribuut(field=StringField,',
               "                                         naam='unionString',",
               "                                         label='Union tekstveld',",
               '                                         '
               "objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtuTestUnionType.unionString',",
               "                                         kardinaliteit_min='0',",
               "                                         definition='Vrij tekstveld van het "
               "test Union datatype',",
               '                                         owner=self)',
               '',
               '    @property',
               '    def unionKwantWrd(self):',
               '        """Kwantitatieve waarde van het test Union datatype"""',
               '        return self._unionKwantWrd.get_waarde()',
               '',
               '    @unionKwantWrd.setter',
               '    def unionKwantWrd(self, value):',
               '        self._unionKwantWrd.set_waarde(value, owner=self._parent)',
               '        if value is not None:',
               "            self.clear_other_props('_unionKwantWrd')",
               '',
               '    @property',
               '    def unionString(self):',
               '        """Vrij tekstveld van het test Union datatype"""',
               '        return self._unionString.get_waarde()',
               '',
               '    @unionString.setter',
               '    def unionString(self, value):',
               '        self._unionString.set_waarde(value, owner=self._parent)',
               '        if value is not None:',
               "            self.clear_other_props('_unionString')",
               '',
               '',
               '# Generated with OTLUnionDatatypeCreator. To modify: extend, do not edit',
               'class DtuTestUnionType(UnionTypeField, AttributeInfo):',
               '    """Union datatype voor test doeleinden."""',
               "    naam = 'DtuTestUnionType'",
               "    label = 'Test UnionType'",
               '    objectUri = '
               "'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtuTestUnionType'",
               "    definition = 'Union datatype voor test doeleinden.'",
               '    waardeObject = DtuTestUnionTypeWaarden',
               '',
               '    def __str__(self):',
               '        return UnionTypeField.__str__(self)',
               '']


class OTLUnionDatatypeCreatorTests(unittest.TestCase):
    def test_invalid_oslo_datatype_union(self):
        creator = OTLUnionDatatypeCreator(MagicMock(spec=OSLOCollector))

        with self.subTest('empty name'):
            oslo_datatype_union = OSLODatatypeUnion(name='',
                                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel'
                                                              '#DtuLichtmastMasthoogte',
                                                    definition='', label='', usagenote='',
                                                    deprecated_version='')

            with self.assertRaises(ValueError) as exception_bad_name:
                creator.create_block_to_write_from_union_types(oslo_datatype_union)
            self.assertEqual(str(exception_bad_name.exception), "OSLODatatypeUnion.name is invalid. Value = ''")

        with self.subTest('empty uri'):
            oslo_datatype_union = OSLODatatypeUnion(name='name', objectUri='', definition='', label='',
                                                    usagenote='',
                                                    deprecated_version='')

            with self.assertRaises(ValueError) as exception_bad_uri:
                creator.create_block_to_write_from_union_types(oslo_datatype_union)
            self.assertEqual(str(exception_bad_uri.exception), "OSLODatatypeUnion.objectUri is invalid. Value = ''")

        with self.subTest('bad uri'):
            oslo_datatype_union = OSLODatatypeUnion(name='name', objectUri='bad objectUri', definition='', label='',
                                                    usagenote='',
                                                    deprecated_version='')

            with self.assertRaises(ValueError) as exception_bad_uri:
                creator.create_block_to_write_from_union_types(oslo_datatype_union)
            self.assertEqual(str(exception_bad_uri.exception), "OSLODatatypeUnion.objectUri is invalid. Value = 'bad objectUri'")

        with self.subTest('invalid type'):
            with self.assertRaises(ValueError) as exception_bad_name:
                creator.create_block_to_write_from_union_types(None)
            self.assertEqual(str(exception_bad_name.exception), "Input is not a OSLODatatypeUnion")

    def setUp(self) -> OSLOCollector:
        base_dir = os.path.dirname(os.path.realpath(__file__))
        file_location = f'{base_dir}/../OTL_AllCasesTestClass.db'
        sql_reader = SQLDbReader(file_location)
        oslo_creator = OSLOInMemoryCreator(sql_reader)
        collector = OSLOCollector(oslo_creator)
        collector.collect()
        return collector

    def test_create_block(self):
        collector = self.setUp()
        creator = OTLUnionDatatypeCreator(collector)
        datatype_DtuTestUnionType = collector.find_union_datatype_by_uri(
            'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtuTestUnionType')
        data_to_write = creator.create_block_to_write_from_union_types(datatype_DtuTestUnionType)
        self.assertEqual(expectedDtu, data_to_write)
