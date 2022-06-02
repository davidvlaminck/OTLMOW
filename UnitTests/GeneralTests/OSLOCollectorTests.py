import os
import unittest
from unittest.mock import MagicMock

from OTLMOW.ModelGenerator.Inheritance import Inheritance
from OTLMOW.ModelGenerator.OSLOAttribuut import OSLOAttribuut
from OTLMOW.ModelGenerator.OSLOClass import OSLOClass
from OTLMOW.ModelGenerator.OSLOCollector import OSLOCollector
from OTLMOW.ModelGenerator.OSLODatatypeComplex import OSLODatatypeComplex
from OTLMOW.ModelGenerator.OSLODatatypeComplexAttribuut import OSLODatatypeComplexAttribuut
from OTLMOW.ModelGenerator.OSLODatatypePrimitive import OSLODatatypePrimitive
from OTLMOW.ModelGenerator.OSLODatatypePrimitiveAttribuut import OSLODatatypePrimitiveAttribuut
from OTLMOW.ModelGenerator.OSLODatatypeUnion import OSLODatatypeUnion
from OTLMOW.ModelGenerator.OSLODatatypeUnionAttribuut import OSLODatatypeUnionAttribuut
from OTLMOW.ModelGenerator.OSLOEnumeration import OSLOEnumeration
from OTLMOW.ModelGenerator.OSLOInMemoryCreator import OSLOInMemoryCreator
from OTLMOW.ModelGenerator.OSLOTypeLink import OSLOTypeLink
from OTLMOW.ModelGenerator.SQLDbReader import SQLDbReader


class OSLOCollectorTests(unittest.TestCase):
    def test_collect(self):
        base_dir = os.path.dirname(os.path.realpath(__file__))
        file_location = f'{base_dir}/../OTL_AllCasesTestClass.db'
        sql_reader = SQLDbReader(file_location)
        oslo_creator = OSLOInMemoryCreator(sql_reader)
        collector = OSLOCollector(oslo_creator)
        collector.collect()

        self.assertTrue(len(collector.inheritances) >= 1)
        self.assertTrue(len(collector.attributes) >= 1)
        self.assertTrue(len(collector.classes) >= 1)
        self.assertTrue(len(collector.complex_datatypes) >= 1)
        self.assertTrue(len(collector.complex_datatype_attributen) >= 1)
        self.assertTrue(len(collector.primitive_datatypes) >= 1)
        self.assertTrue(len(collector.primitive_datatype_attributen) >= 1)
        self.assertTrue(len(collector.union_datatypes) >= 1)
        self.assertTrue(len(collector.union_datatype_attributen) >= 1)
        self.assertTrue(len(collector.enumerations) >= 1)
        self.assertTrue(len(collector.relations) >= 1)
        self.assertTrue(len(collector.typeLinks) >= 1)

    def test_find_attributes_by_class(self):
        collector = OSLOCollector(MagicMock(spec=OSLOInMemoryCreator))
        collector.classes = [OSLOClass(objectUri='a')]
        collector.attributes = [OSLOAttribuut(name='b1', class_uri='b', objectUri='b1'),
                                OSLOAttribuut(name='a2', class_uri='a', objectUri='a2'),
                                OSLOAttribuut(name='a1', class_uri='a', objectUri='a1')]

        attributes = collector.find_attributes_by_class(collector.classes[0])
        self.assertEqual('a1', attributes[0].name)
        self.assertEqual('a2', attributes[1].name)

        attributes = collector.find_attributes_by_class(None)
        self.assertListEqual([], attributes)

    def test_find_inheritances_by_class(self):
        collector = OSLOCollector(MagicMock(spec=OSLOInMemoryCreator))
        collector.classes = [OSLOClass(objectUri='a')]
        collector.inheritances = [Inheritance(base_name='b1', class_uri='b', base_uri='b1'),
                                  Inheritance(base_name='a2', class_uri='a', base_uri='a2'),
                                  Inheritance(base_name='a1', class_uri='a', base_uri='a1')]

        inheritances = collector.find_inheritances_by_class(collector.classes[0])
        self.assertEqual('a1', inheritances[0].base_name)
        self.assertEqual('a2', inheritances[1].base_name)

        inheritances = collector.find_inheritances_by_class(None)
        self.assertListEqual([], inheritances)

    def test_find_class_by_uri(self):
        collector = OSLOCollector(MagicMock(spec=OSLOInMemoryCreator))
        collector.classes = [OSLOClass(name='a', objectUri='a'), OSLOClass(name='b', objectUri='b')]

        class_found = collector.find_class_by_uri('a')
        self.assertEqual('a', class_found.name)

        class_found = collector.find_class_by_uri('c')
        self.assertIsNone(class_found)

    def test_find_primitive_datatype_by_uri(self):
        collector = OSLOCollector(MagicMock(spec=OSLOInMemoryCreator))
        collector.primitive_datatypes = [OSLODatatypePrimitive(name='a', objectUri='a'),
                                         OSLODatatypePrimitive(name='b', objectUri='b')]

        datatype_found = collector.find_primitive_datatype_by_uri('a')
        self.assertEqual('a', datatype_found.name)

        datatype_found = collector.find_primitive_datatype_by_uri('c')
        self.assertIsNone(datatype_found)

    def test_find_primitive_datatypes_by_uri(self):
        collector = OSLOCollector(MagicMock(spec=OSLOInMemoryCreator))
        collector.primitive_datatype_attributen = [OSLODatatypePrimitiveAttribuut(name='a2', objectUri='a2', class_uri='a'),
                                                   OSLODatatypePrimitiveAttribuut(name='a1', objectUri='a1', class_uri='a'),
                                                   OSLODatatypePrimitiveAttribuut(name='b', objectUri='b', class_uri='b')]

        attributes = collector.find_primitive_datatype_attributes_by_class_uri('a')
        self.assertEqual('a1', attributes[0].name)
        self.assertEqual('a2', attributes[1].name)

        attributes = collector.find_primitive_datatype_attributes_by_class_uri(None)
        self.assertListEqual([], attributes)

    def test_find_complex_datatype_by_uri(self):
        collector = OSLOCollector(MagicMock(spec=OSLOInMemoryCreator))
        collector.complex_datatypes = [OSLODatatypeComplex(name='a', objectUri='a'),
                                       OSLODatatypeComplex(name='b', objectUri='b')]

        datatype_found = collector.find_complex_datatype_by_uri('a')
        self.assertEqual('a', datatype_found.name)

        datatype_found = collector.find_complex_datatype_by_uri('c')
        self.assertIsNone(datatype_found)

    def test_find_complex_datatypes_by_uri(self):
        collector = OSLOCollector(MagicMock(spec=OSLOInMemoryCreator))
        collector.complex_datatype_attributen = [OSLODatatypeComplexAttribuut(name='a2', objectUri='a2', class_uri='a'),
                                                 OSLODatatypeComplexAttribuut(name='a1', objectUri='a1', class_uri='a'),
                                                 OSLODatatypeComplexAttribuut(name='b', objectUri='b', class_uri='b')]

        attributes = collector.find_complex_datatype_attributes_by_class_uri('a')
        self.assertEqual('a1', attributes[0].name)
        self.assertEqual('a2', attributes[1].name)

        attributes = collector.find_complex_datatype_attributes_by_class_uri(None)
        self.assertListEqual([], attributes)

    def test_find_union_datatype_by_uri(self):
        collector = OSLOCollector(MagicMock(spec=OSLOInMemoryCreator))
        collector.union_datatypes = [OSLODatatypeUnion(name='a', objectUri='a'),
                                     OSLODatatypeUnion(name='b', objectUri='b')]

        datatype_found = collector.find_union_datatype_by_uri('a')
        self.assertEqual('a', datatype_found.name)

        datatype_found = collector.find_union_datatype_by_uri('c')
        self.assertIsNone(datatype_found)

    def test_find_union_datatypes_by_uri(self):
        collector = OSLOCollector(MagicMock(spec=OSLOInMemoryCreator))
        collector.union_datatype_attributen = [OSLODatatypeUnionAttribuut(name='a2', objectUri='a2', class_uri='a'),
                                               OSLODatatypeUnionAttribuut(name='a1', objectUri='a1', class_uri='a'),
                                               OSLODatatypeUnionAttribuut(name='b', objectUri='b', class_uri='b')]

        attributes = collector.find_union_datatype_attributes_by_class_uri('a')
        self.assertEqual('a1', attributes[0].name)
        self.assertEqual('a2', attributes[1].name)

        attributes = collector.find_union_datatype_attributes_by_class_uri(None)
        self.assertListEqual([], attributes)

    def test_find_enumeration_by_uri(self):
        collector = OSLOCollector(MagicMock(spec=OSLOInMemoryCreator))
        collector.enumerations = [OSLOEnumeration(name='a', objectUri='a'),
                                  OSLOEnumeration(name='b', objectUri='b')]

        enumeration_found = collector.find_enumeration_by_uri('a')
        self.assertEqual('a', enumeration_found.name)

        enumeration_found = collector.find_enumeration_by_uri('c')
        self.assertIsNone(enumeration_found)

    def test_find_type_link_by_uri(self):
        collector = OSLOCollector(MagicMock(spec=OSLOInMemoryCreator))
        collector.typeLinks = [OSLOTypeLink(item_uri='a', item_tabel='a'),
                               OSLOTypeLink(item_uri='b', item_tabel='b')]

        typelink_found = collector.find_type_link_by_uri('a')
        self.assertEqual('a', typelink_found.item_tabel)

        typelink_found = collector.find_type_link_by_uri('c')
        self.assertIsNone(typelink_found)
