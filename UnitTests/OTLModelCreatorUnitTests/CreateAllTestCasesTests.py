import logging
import os
import unittest

from OTLMOW.Facility.AssetFactory import AssetFactory
from OTLMOW.Facility.OTLFacility import OTLFacility
from OTLMOW.ModelGenerator.OSLOCollector import OSLOCollector
from OTLMOW.ModelGenerator.OSLOInMemoryCreator import OSLOInMemoryCreator
from OTLMOW.ModelGenerator.SQLDbReader import SQLDbReader
from UnitTests.TestClasses.OTLModel.Classes.Onderdeel.AllCasesTestClass import AllCasesTestClass


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

        with self.assertLogs() as captured:
            otl_facility.create_otl_datamodel(directory=f'{base_dir}/../TestClasses', otl_sqlite_file_location=otl_file_location)
            allcasesclass_location = f'{base_dir}/../TestClasses/OTLModel/Classes/Onderdeel/AllCasesTestClass.py'
            self.assertTrue(os.path.isfile(allcasesclass_location))

        errors = list(filter(lambda r: r.levelno >= logging.ERROR, list(captured.records)))

        self.assertListEqual([], errors)

    def test_use_AllCasesTestClass(self):
        instance = AssetFactory.dynamic_create_instance_from_uri('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#AllCasesTestClass', directory='UnitTests.TestClasses.OTLModel.Classes')
        self.assertIsInstance(instance, AllCasesTestClass)


