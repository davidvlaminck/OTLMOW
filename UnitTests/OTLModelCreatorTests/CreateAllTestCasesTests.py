import os
import unittest

from OTLMOW.Facility.OTLFacility import OTLFacility
from OTLMOW.ModelGenerator.OSLOCollector import OSLOCollector
from OTLMOW.ModelGenerator.OSLOInMemoryCreator import OSLOInMemoryCreator
from OTLMOW.ModelGenerator.SQLDbReader import SQLDbReader


class CreateAllTestCasesTests(unittest.TestCase):
    # TODO create AllCasesTestClass using sqlite
    def test_init_AllCasesTestClass(self):
        otl_facility = OTLFacility(logfile='',
                                   settings_path="C:\\resources\\settings_OTLMOW.json")  # TODO change to local settings file in unittests

        base_dir = os.path.dirname(os.path.realpath(__file__))
        otl_file_location = f'{base_dir}/../OTL_AllCasesTestClass.db'
        #GA_file_location = '../InputFiles/Geometrie_Artefact_2.3.RC2.db'
        otl_facility.init_otl_model_creator(otl_file_location)
        otl_facility.create_otl_datamodel()

        self.assertTrue(False)