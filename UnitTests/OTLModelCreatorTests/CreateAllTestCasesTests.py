import logging
import os
import unittest

from OTLMOW.Facility.OTLFacility import OTLFacility
from OTLMOW.ModelGenerator.OSLOCollector import OSLOCollector
from OTLMOW.ModelGenerator.OSLOInMemoryCreator import OSLOInMemoryCreator
from OTLMOW.ModelGenerator.SQLDbReader import SQLDbReader


class CreateAllTestCasesTests(unittest.TestCase):
    def setUp(self) -> OSLOCollector:
        base_dir = os.path.dirname(os.path.realpath(__file__))
        file_location = f'{base_dir}/../OTL_AllCasesTestClass.db'
        sql_reader = SQLDbReader(file_location)
        oslo_creator = OSLOInMemoryCreator(sql_reader)
        collector = OSLOCollector(oslo_creator)
        collector.collect()
        return collector

    def test_init_AllCasesTestClass(self):
        base_dir = os.path.dirname(os.path.realpath(__file__))
        settings_file_location = f'{base_dir}/../settings_OTLMOW.json'
        otl_facility = OTLFacility(logfile='',
                                   settings_path=settings_file_location)

        collector = self.setUp()
        otl_facility.collector = collector

        base_dir = os.path.dirname(os.path.realpath(__file__))
        otl_file_location = f'{base_dir}/../OTL_AllCasesTestClass.db'
        #GA_file_location = '../InputFiles/Geometrie_Artefact_2.3.RC2.db'
        otl_facility.init_otl_model_creator(otl_file_location)
        otl_facility.create_otl_datamodel(directory=f'{base_dir}/../TestClasses')

        with self.assertLogs() as captured:
            otl_facility.create_otl_datamodel(directory=f'{base_dir}/../TestClasses')
            allcasesclass_location = f'{base_dir}/../TestClasses/OTLModel/Classes/AllCasesTestClass.py'
            self.assertTrue(os.path.isfile(allcasesclass_location))

        errors = list(filter(lambda r: r.levelno >= logging.ERROR, list(captured.records)))

        self.assertListEqual([], errors)

