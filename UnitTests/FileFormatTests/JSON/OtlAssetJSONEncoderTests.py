import unittest
from datetime import datetime

from AllCasesTestClass import AllCasesTestClass
from OTLMOW.Facility.OTLFacility import OTLFacility
from OTLMOW.ModelGenerator.OtlAssetJSONEncoder import OtlAssetJSONEncoder


class OtlAssetJSONEncoderTests(unittest.TestCase):
    def test_init_encoder(self):
        otl_facility = OTLFacility(logfile='', settings_path='C:\\resources\\settings_OTLMOW.json')
        encoder = OtlAssetJSONEncoder(settings=otl_facility.settings)
        self.assertIsNotNone(encoder)

    def test_JsonEncode_Boolean(self):
        otl_facility = OTLFacility(logfile='', settings_path='C:\\resources\\settings_OTLMOW.json')
        encoder = OtlAssetJSONEncoder(settings=otl_facility.settings)

        instance = AllCasesTestClass()
        instance.testBooleanField = True
        json_instance = encoder.encode(instance)
        expected = '{"testBooleanField": true, ' \
                   '"typeURI": "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#AllCasesTestClass"}'

        self.assertEqual(expected, json_instance)

    def test_JsonEncode_Keuzelijst(self):
        otl_facility = OTLFacility(logfile='', settings_path='C:\\resources\\settings_OTLMOW.json')
        encoder = OtlAssetJSONEncoder(settings=otl_facility.settings)

        instance = AllCasesTestClass()
        instance.testKeuzelijst = 'waarde-2'
        json_instance = encoder.encode(instance)
        expected = '{"testKeuzelijst": "waarde-2", ' \
                   '"typeURI": "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#AllCasesTestClass"}'

        self.assertEqual(expected, json_instance)

    def test_JsonEncode_UnionType(self):
        otl_facility = OTLFacility(logfile='', settings_path='C:\\resources\\settings_OTLMOW.json')
        encoder = OtlAssetJSONEncoder(settings=otl_facility.settings)

        instance = AllCasesTestClass()
        instance.testUnionType.unionString = 'union waarde'
        json_instance = encoder.encode(instance)
        expected = '{"testUnionType": {"unionString": "union waarde"}, ' \
                   '"typeURI": "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#AllCasesTestClass"}'
        self.assertEqual(expected, json_instance)

        instance.testUnionType.unionKwantWrd.waarde = 1.0
        json_instance = encoder.encode(instance)
        expected = '{"testUnionType": {"unionKwantWrd": {"waarde": 1.0}}, ' \
                   '"typeURI": "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#AllCasesTestClass"}'
        self.assertEqual(expected, json_instance)

    def test_JsonEncode_ComplexType(self):
        otl_facility = OTLFacility(logfile='', settings_path='C:\\resources\\settings_OTLMOW.json')
        encoder = OtlAssetJSONEncoder(settings=otl_facility.settings)

        instance = AllCasesTestClass()
        instance.testComplexType.testStringField = 'string'
        instance.testComplexType.testBooleanField = True
        instance.testComplexType.testComplexType2.testStringField = 'string niveau 2'
        json_instance = encoder.encode(instance)
        expected = '{"testComplexType": {"testBooleanField": true, "testStringField": "string", ' \
                   '"testComplexType2": {"testStringField": "string niveau 2"}}, ' \
                   '"typeURI": "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#AllCasesTestClass"}'

        self.assertEqual(expected, json_instance)

    def test_JsonEncode_StringMetKard(self):
        otl_facility = OTLFacility(logfile='', settings_path='C:\\resources\\settings_OTLMOW.json')
        encoder = OtlAssetJSONEncoder(settings=otl_facility.settings)

        instance = AllCasesTestClass()
        instance.testStringFieldMetKard = ['a', 'b', 'c']
        json_instance = encoder.encode(instance)
        expected = '{"testStringFieldMetKard": ["a", "b", "c"], ' \
                   '"typeURI": "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#AllCasesTestClass"}'

        self.assertEqual(expected, json_instance)

    def test_JsonEncode_KwantWrd(self):
        otl_facility = OTLFacility(logfile='', settings_path='C:\\resources\\settings_OTLMOW.json')
        encoder = OtlAssetJSONEncoder(settings=otl_facility.settings)

        instance = AllCasesTestClass()
        instance.testKwantWrd.waarde = 1.0
        json_instance = encoder.encode(instance)
        expected = '{"testKwantWrd": 1.0, ' \
                   '"typeURI": "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#AllCasesTestClass"}'

        self.assertEqual(expected, json_instance)

    def test_JsonEncode_ComplexTypeMetKard(self):
        otl_facility = OTLFacility(logfile='', settings_path='C:\\resources\\settings_OTLMOW.json')
        encoder = OtlAssetJSONEncoder(settings=otl_facility.settings)

        instance = AllCasesTestClass()
        instance.testComplexTypeMetKard[0].testStringField = 'string'
        instance.testComplexTypeMetKard[0].testStringFieldMetKard = ['lijst', 'waardes']
        instance._testComplexTypeMetKard.add_empty_value()
        instance.testComplexTypeMetKard[1].testStringField = 'string 2'
        instance.testComplexTypeMetKard[1].testStringFieldMetKard = ['lijst2', 'waardes']
        json_instance = encoder.encode(instance)
        expected = '{"testComplexTypeMetKard": [{"testStringField": "string", ' \
                   '"testStringFieldMetKard": ["lijst", "waardes"]}, ' \
                   '{"testStringField": "string 2", ' \
                   '"testStringFieldMetKard": ["lijst2", "waardes"]}], ' \
                   '"typeURI": "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#AllCasesTestClass"}'

        self.assertEqual(expected, json_instance)

    def test_JsonEncode_DateTimeField(self):
        otl_facility = OTLFacility(logfile='', settings_path='C:\\resources\\settings_OTLMOW.json')
        encoder = OtlAssetJSONEncoder(settings=otl_facility.settings)

        instance = AllCasesTestClass()
        instance.testDateTimeField = datetime(2022, 2, 2, 22, 22, 22)
        json_instance = encoder.encode(instance)
        expected = '{"testDateTimeField": "2022-02-02 22:22:22", ' \
                   '"typeURI": "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#AllCasesTestClass"}'

        self.assertEqual(expected, json_instance)
