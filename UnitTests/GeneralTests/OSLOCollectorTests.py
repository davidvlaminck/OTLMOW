import os
import unittest

from OTLMOW.ModelGenerator.OSLOCollector import OSLOCollector
from OTLMOW.ModelGenerator.OSLOInMemoryCreator import OSLOInMemoryCreator
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
