import os
import unittest

from AllCasesTestClass import AllCasesTestClass
from OTLMOW.Facility.CsvExporter import CsvExporter
from OTLMOW.Facility.CsvImporter import CsvImporter
from OTLMOW.Facility.OTLFacility import OTLFacility
from OTLMOW.OTLModel.Classes.Verkeersregelaar import Verkeersregelaar

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))


class CsvExporterTests(unittest.TestCase):
    def test_init_importer_only_load_with_settings(self):
        otl_facility = OTLFacility(None, settings_path='C:\\resources\\settings_OTLMOW.json')

        with self.subTest('load with correct settings'):
            exporter = CsvExporter(settings=otl_facility.settings)
            self.assertIsNotNone(exporter)

        with self.subTest('load without settings'):
            with self.assertRaises(ValueError):
                CsvExporter(settings=None)

        with self.subTest('load with incorrect settings (no file_formats)'):
            with self.assertRaises(ValueError):
                CsvExporter(settings={"auth_options": [{}]})

        with self.subTest('load with incorrect settings (file_formats but no csv)'):
            with self.assertRaises(ValueError):
                CsvExporter(settings={"file_formats": [{}]})

    @unittest.skip
    def test_load_test_file(self):
        otl_facility = OTLFacility(None, settings_path='C:\\resources\\settings_OTLMOW.json')
        importer = CsvImporter(settings=otl_facility.settings)
        file_location = os.path.abspath(os.path.join(os.sep, ROOT_DIR, 'test_file_VR.csv'))
        importer.import_csv_file(file_location)
        self.assertEqual(354, len(importer.data))
        self.assertEqual(34, len(importer.headers))

    def test_create_data_from_objects_empty_objects(self):
        otl_facility = OTLFacility(None, settings_path='C:\\resources\\settings_OTLMOW.json')
        exporter = CsvExporter(settings=otl_facility.settings)

        with self.subTest('empty list of objects'):
            with self.assertRaises(ValueError):
                list_of_objects = []
                exporter.create_data_from_objects(list_of_objects)

        with self.subTest('object in list without valid assetId'):
            with self.assertRaises(ValueError):
                list_of_objects = [AllCasesTestClass()]
                csv_data = exporter.create_data_from_objects(list_of_objects)

        with self.subTest('object in list without valid assetId -> empty string'):
            with self.assertRaises(ValueError):
                list_of_objects = [AllCasesTestClass()]
                list_of_objects[0].assetId.identificator = ''
                csv_data = exporter.create_data_from_objects(list_of_objects)

        with self.subTest('object in list with valid assetId -> string'):
            list_of_objects = [AllCasesTestClass()]
            list_of_objects[0].assetId.identificator = '0'
            csv_data = exporter.create_data_from_objects(list_of_objects)
            self.assertEqual('typeURI', csv_data[0][0])
            self.assertEqual('assetId.identificator', csv_data[0][1])
            self.assertEqual('assetId.toegekendDoor', csv_data[0][2])
            self.assertEqual('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#AllCasesTestClass', csv_data[1][0])
            self.assertEqual('0', csv_data[1][1])
            self.assertEqual(None, csv_data[1][2])

    def test_create_data_from_objects_nonempty_objects_same_type(self):
        otl_facility = OTLFacility(None, settings_path='C:\\resources\\settings_OTLMOW.json')
        exporter = CsvExporter(settings=otl_facility.settings)

        list_of_objects = [AllCasesTestClass(), AllCasesTestClass()]
        list_of_objects[0].assetId.identificator = '0'
        list_of_objects[0].testDecimalNumberField = 1.0
        list_of_objects[0].testBooleanField = True
        list_of_objects[0].testKeuzelijst = 'waarde-1'
        list_of_objects[0].testComplexType.testStringField = 'string in complex veld'
        list_of_objects[0].testComplexType.testKwantWrd.waarde = 2.0

        list_of_objects[1].assetId.identificator = '1'
        list_of_objects[1].testBooleanField = False
        list_of_objects[1].testKeuzelijstMetKard = ['waarde-2']
        list_of_objects[1].testDecimalNumberField = 2.5
        list_of_objects[1].testComplexType.testComplexType2.testStringField = 'string in complex veld binnenin complex veld'

        csv_data = exporter.create_data_from_objects(list_of_objects)

        with self.subTest('verify headers'):
            self.assertEqual('typeURI', csv_data[0][0])
            self.assertEqual('assetId.identificator', csv_data[0][1])
            self.assertEqual('assetId.toegekendDoor', csv_data[0][2])
            self.assertEqual('testBooleanField', csv_data[0][3])
            self.assertEqual('testComplexType.testKwantWrd.waarde', csv_data[0][4])  # TODO fix
            self.assertEqual('testComplexType.testStringField', csv_data[0][5])
            self.assertEqual('testDecimalNumberField', csv_data[0][6])
            self.assertEqual('testKeuzelijst', csv_data[0][7])
            self.assertEqual('testComplexType.testComplexType2.testStringField', csv_data[0][8])
            self.assertEqual('testKeuzelijstMetKard[0]', csv_data[0][9])  # TODO fix

        with self.subTest('verify asset 1'):
            self.assertEqual('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#AllCasesTestClass', csv_data[1][0])
            self.assertEqual('0', csv_data[1][1])
            self.assertEqual(None, csv_data[1][2])
            self.assertEqual(True, csv_data[1][3])
            self.assertEqual(2.0, csv_data[1][4])
            self.assertEqual('string in complex veld', csv_data[1][5])
            self.assertEqual(1.0, csv_data[1][6])
            self.assertEqual('waarde-1', csv_data[1][7])
            self.assertEqual(None, csv_data[1][8])
            self.assertEqual(None, csv_data[1][9])

        with self.subTest('verify asset 2'):
            self.assertEqual('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#AllCasesTestClass', csv_data[2][0])
            self.assertEqual('1', csv_data[2][1])
            self.assertEqual(None, csv_data[2][2])
            self.assertEqual(False, csv_data[2][3])
            self.assertEqual(None, csv_data[2][4])
            self.assertEqual(None, csv_data[2][5])
            self.assertEqual(2.5, csv_data[2][6])
            self.assertEqual(None, csv_data[2][7])
            self.assertEqual('string in complex veld binnenin complex veld', csv_data[2][8])
            self.assertEqual(['waarde-2'], csv_data[2][9])

