import logging
import os
import unittest
from pathlib import Path

from OTLMOW.Facility.AssetFactory import AssetFactory
from OTLMOW.Facility.OTLFacility import OTLFacility
from UnitTests.TestClasses.OTLModel.Classes.Onderdeel.AllCasesTestClass import AllCasesTestClass


class CreateAllTestCasesTests(unittest.TestCase):
    def test_init_AllCasesTestClass(self):
        current_file_path = Path(__file__)
        base_dir = current_file_path.parents[0]
        settings_file_location = Path(f'{base_dir}/../settings_OTLMOW.json')
        subset_file_location = Path(f'{base_dir}/../OTL_AllCasesTestClass.db')

        otl_facility = OTLFacility(settings_path=settings_file_location)

        with self.assertLogs() as captured:
            otl_facility.create_otl_datamodel(directory=Path(f'{base_dir}/../TestClasses'),
                                              otl_sqlite_file_location=subset_file_location)
            allcasesclass_location = Path(f'{base_dir}/../TestClasses/OTLModel/Classes/Onderdeel/AllCasesTestClass.py')
            self.assertTrue(os.path.isfile(allcasesclass_location))

        errors = list(filter(lambda r: r.levelno >= logging.ERROR, list(captured.records)))
        self.assertListEqual([], errors)

    def test_use_AllCasesTestClass(self):
        instance = AssetFactory.dynamic_create_instance_from_uri('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#AllCasesTestClass',
                                                                 directory='UnitTests.TestClasses.OTLModel.Classes')
        self.assertIsInstance(instance, AllCasesTestClass)


