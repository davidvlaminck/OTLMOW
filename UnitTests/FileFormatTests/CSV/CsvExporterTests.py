import os
import unittest
import datetime
from pathlib import Path

from OTLMOW.Facility.FileFormats.CsvExporter import CsvExporter
from OTLMOW.Facility.FileFormats.CsvImporter import CsvImporter
from OTLMOW.Facility.OTLFacility import OTLFacility
from SettingManagerForUnitTests import get_settings_path_for_unittests
from TestClasses.OTLModel.Classes.Onderdeel.AllCasesTestClass import AllCasesTestClass

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))


class CsvExporterTests(unittest.TestCase):
    @staticmethod
    def set_up_facility():
        settings_file_location = get_settings_path_for_unittests()
        otl_facility = OTLFacility(settings_path=settings_file_location)
        return otl_facility

    def test_init_importer_only_load_with_settings(self):
        otl_facility = self.set_up_facility()

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

    def test_load_and_writefile(self):
        otl_facility = self.set_up_facility()
        importer = CsvImporter(settings=otl_facility.settings)
        file_location = os.path.abspath(os.path.join(os.sep, ROOT_DIR, 'test_file_VR.csv'))
        objects = importer.import_file(file_location)
        exporter = CsvExporter(settings=otl_facility.settings)
        new_file_location = os.path.abspath(os.path.join(os.sep, ROOT_DIR, 'test_export_file_VR.csv'))
        if os.path.isfile(new_file_location):
            os.remove(new_file_location)
        exporter.export_to_file(list_of_objects=objects, filepath=new_file_location)
        self.assertTrue(os.path.isfile(new_file_location))

    def test_find_sorted_header_index(self):
        otl_facility = self.set_up_facility()
        exporter = CsvExporter(settings=otl_facility.settings)
        with self.subTest('no headers yet'):
            exporter.csv_headers = ['typeURI', 'assetId.identificator', 'assetId.toegekendDoor']
            result = exporter.find_sorted_header_index('a')
            expected = 3
            self.assertEqual(expected, result)

        with self.subTest('1 header after'):
            exporter.csv_headers = ['typeURI', 'assetId.identificator', 'assetId.toegekendDoor', 'a']
            result = exporter.find_sorted_header_index('b')
            expected = 4
            self.assertEqual(expected, result)

        with self.subTest('1 header before'):
            exporter.csv_headers = ['typeURI', 'assetId.identificator', 'assetId.toegekendDoor', 'b']
            result = exporter.find_sorted_header_index('a')
            expected = 3
            self.assertEqual(expected, result)

    def test_sort_headers(self):
        otl_facility = self.set_up_facility()
        exporter = CsvExporter(settings=otl_facility.settings)
        with self.subTest('no headers'):
            result = exporter.sort_headers(['typeURI', 'assetId.identificator', 'assetId.toegekendDoor'])
            expected = ['typeURI', 'assetId.identificator', 'assetId.toegekendDoor']
            self.assertListEqual(expected, result)

        with self.subTest('2 headers'):
            result = exporter.sort_headers(['typeURI', 'assetId.identificator', 'assetId.toegekendDoor', 'b', 'a'])
            expected = ['typeURI', 'assetId.identificator', 'assetId.toegekendDoor', 'a', 'b']
            self.assertListEqual(expected, result)

        with self.subTest('complex headers'):
            result = exporter.sort_headers(['typeURI', 'assetId.identificator', 'assetId.toegekendDoor', 'a.2', 'a.1'])
            expected = ['typeURI', 'assetId.identificator', 'assetId.toegekendDoor', 'a.1', 'a.2']
            self.assertListEqual(expected, result)

    def test_create_data_from_objects_empty_objects(self):
        otl_facility = self.set_up_facility()
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
        otl_facility = self.set_up_facility()
        exporter = CsvExporter(settings=otl_facility.settings)

        list_of_objects = [AllCasesTestClass(), AllCasesTestClass()]
        list_of_objects[0].assetId.identificator = '0'
        list_of_objects[0].testDecimalField = 1.0
        list_of_objects[0].testBooleanField = True
        list_of_objects[0].testKeuzelijst = 'waarde-1'
        list_of_objects[0].testComplexType.testStringField = 'string in complex veld'
        list_of_objects[0].testComplexType.testKwantWrd.waarde = 2.0

        list_of_objects[1].assetId.identificator = '1'
        list_of_objects[1].testBooleanField = False
        list_of_objects[1].testKeuzelijstMetKard = ['waarde-2']
        list_of_objects[1].testDateField = datetime.date(2022, 2, 2)
        list_of_objects[1].testDecimalField = 2.5
        list_of_objects[1].testComplexType.testComplexType2.testStringField = 'string in complex veld binnenin complex veld'

        csv_data = exporter.create_data_from_objects(list_of_objects)

        with self.subTest('verify headers'):
            self.assertEqual('typeURI', csv_data[0][0])
            self.assertEqual('assetId.identificator', csv_data[0][1])
            self.assertEqual('assetId.toegekendDoor', csv_data[0][2])
            self.assertEqual('testBooleanField', csv_data[0][3])
            self.assertEqual('testComplexType.testComplexType2.testStringField', csv_data[0][4])
            self.assertEqual('testComplexType.testKwantWrd', csv_data[0][5])
            self.assertEqual('testComplexType.testStringField', csv_data[0][6])
            self.assertEqual('testDateField', csv_data[0][7])
            self.assertEqual('testDecimalField', csv_data[0][8])
            self.assertEqual('testKeuzelijst', csv_data[0][9])
            self.assertEqual('testKeuzelijstMetKard[]', csv_data[0][10])

        with self.subTest('verify asset 1'):
            self.assertEqual('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#AllCasesTestClass', csv_data[1][0])
            self.assertEqual('0', csv_data[1][1])
            self.assertEqual(None, csv_data[1][2])
            self.assertEqual(True, csv_data[1][3])
            self.assertEqual(None, csv_data[1][4])
            self.assertEqual(2.0, csv_data[1][5])
            self.assertEqual('string in complex veld', csv_data[1][6])
            self.assertEqual(1.0, csv_data[1][8])
            self.assertEqual('waarde-1', csv_data[1][9])
            self.assertEqual(None, csv_data[1][10])

        with self.subTest('verify asset 2'):
            self.assertEqual('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#AllCasesTestClass', csv_data[2][0])
            self.assertEqual('1', csv_data[2][1])
            self.assertEqual(None, csv_data[2][2])
            self.assertEqual(False, csv_data[2][3])
            self.assertEqual('string in complex veld binnenin complex veld', csv_data[2][4])
            self.assertEqual(None, csv_data[2][5])
            self.assertEqual(None, csv_data[2][6])
            self.assertEqual('2022-02-02', csv_data[2][7])
            self.assertEqual(2.5, csv_data[2][8])
            self.assertEqual(None, csv_data[2][9])
            self.assertEqual(['waarde-2'], csv_data[2][10])

    def test_create_data_from_objects_cardinality(self):
        otl_facility = self.set_up_facility()
        exporter = CsvExporter(settings=otl_facility.settings)

        list_of_objects = [AllCasesTestClass()]
        list_of_objects[0].assetId.identificator = '0'
        list_of_objects[0]._testComplexTypeMetKard.add_empty_value()
        list_of_objects[0].testComplexTypeMetKard[0].testStringField = '1.1'
        list_of_objects[0].testComplexTypeMetKard[0].testBooleanField = False
        list_of_objects[0]._testComplexTypeMetKard.add_empty_value()
        list_of_objects[0].testComplexTypeMetKard[1].testStringField = '1.2'
        list_of_objects[0].testComplexTypeMetKard[1].testBooleanField = True

        csv_data = exporter.create_data_from_objects(list_of_objects)

        self.assertEqual('typeURI', csv_data[0][0])
        self.assertEqual('assetId.identificator', csv_data[0][1])
        self.assertEqual('assetId.toegekendDoor', csv_data[0][2])
        self.assertEqual('testComplexTypeMetKard[].testBooleanField', csv_data[0][3])
        self.assertEqual('testComplexTypeMetKard[].testStringField', csv_data[0][4])
        self.assertEqual('0', csv_data[1][1])
        self.assertEqual(None, csv_data[1][2])
        self.assertListEqual([False, True], csv_data[1][3])
        self.assertListEqual(['1.1', '1.2'], csv_data[1][4])

    def test_create_data_from_objects_different_settings(self):
        otl_facility = self.set_up_facility()
        exporter = CsvExporter(settings=otl_facility.settings)
        exporter.settings = {
            "name": "csv",
            "dotnotation": {
                "separator": "+",
                "cardinality separator": "$",
                "cardinality indicator": "()",
                "waarde_shortcut_applicable": True
            },
            "delimiter": ','
        }

        list_of_objects = [AllCasesTestClass(), AllCasesTestClass()]
        list_of_objects[0].assetId.identificator = '0'
        list_of_objects[0].testDecimalField = 1.0
        list_of_objects[0].testBooleanField = True
        list_of_objects[0].testKeuzelijst = 'waarde-1'
        list_of_objects[0].testComplexType.testStringField = 'string in complex veld'
        list_of_objects[0].testComplexType.testKwantWrd.waarde = 2.0

        list_of_objects[1].assetId.identificator = '1'
        list_of_objects[1].testBooleanField = False
        list_of_objects[1].testKeuzelijstMetKard = ['waarde-2', 'waarde-3']
        list_of_objects[1].testDecimalField = 2.5
        list_of_objects[1].testComplexType.testComplexType2.testStringField = 'string in complex veld binnenin complex veld'

        csv_data = exporter.create_data_from_objects(list_of_objects)

        with self.subTest('verify headers with different dotnotation settings'):
            self.assertEqual('assetId+identificator', csv_data[0][1])
            self.assertEqual('assetId+toegekendDoor', csv_data[0][2])
            self.assertEqual('testComplexType+testComplexType2+testStringField', csv_data[0][4])
            self.assertEqual('testComplexType+testKwantWrd', csv_data[0][5])
            self.assertEqual('testComplexType+testStringField', csv_data[0][6])
            self.assertEqual('testKeuzelijstMetKard()', csv_data[0][9])

        csv_data_lines = exporter.create_data_lines_from_data(csv_data, delimiter=exporter.settings['delimiter'])
        expected_line_asset_2 = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#AllCasesTestClass,1,,False,string in complex veld binnenin complex veld,,,2.5,,waarde-2$waarde-3'

        with self.subTest('verify data with different settings'):
            self.assertEqual(expected_line_asset_2, csv_data_lines[2])

    def test_create_with_different_cardinality_among_subattributes(self):
        otl_facility = self.set_up_facility()
        exporter = CsvExporter(settings=otl_facility.settings)

        list_of_objects = [AllCasesTestClass()]
        list_of_objects[0].assetId.identificator = '0'
        list_of_objects[0]._testComplexTypeMetKard.add_empty_value()
        list_of_objects[0].testComplexTypeMetKard[0].testBooleanField = False
        list_of_objects[0].testComplexTypeMetKard[0].testStringField = '1.1'
        list_of_objects[0]._testComplexTypeMetKard.add_empty_value()
        list_of_objects[0].testComplexTypeMetKard[1].testBooleanField = True
        list_of_objects[0].testComplexTypeMetKard[1].testKwantWrd.waarde = 2.0
        list_of_objects[0].testComplexTypeMetKard[1].testStringField = '1.2'
        list_of_objects[0]._testComplexTypeMetKard.add_empty_value()
        list_of_objects[0].testComplexTypeMetKard[2].testStringField = '1.3'

        csv_data = exporter.create_data_from_objects(list_of_objects)

        self.assertEqual('testComplexTypeMetKard[].testBooleanField', csv_data[0][3])
        self.assertEqual('testComplexTypeMetKard[].testKwantWrd', csv_data[0][4])
        self.assertEqual('testComplexTypeMetKard[].testStringField', csv_data[0][5])

        self.assertListEqual([False, True, None], csv_data[1][3])
        self.assertListEqual([None, 2.0, None], csv_data[1][4])
        self.assertListEqual(['1.1', '1.2', '1.3'], csv_data[1][5])

        csv_data_lines = exporter.create_data_lines_from_data(csv_data, ';')

        expected = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#AllCasesTestClass;0;;False|True|;|2.0|;1.1|1.2|1.3'
        self.assertEqual(expected, csv_data_lines[1])



