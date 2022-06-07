from datetime import date
from unittest import TestCase

from OTLMOW.OTLModel.BaseClasses.OTLObject import OTLObjectHelper
from OTLMOW.OTLModel.Classes.Aftakking import Aftakking
from OTLMOW.OTLModel.Classes.Verkeersregelaar import Verkeersregelaar
from TestClasses.OTLModel.Classes.AllCasesTestClass import AllCasesTestClass


class OTLObjectsTests(TestCase):
    def test_build_string_version_dotnotation_empty_class(self):
        infoString = Aftakking().__str__(use_dotnotation=True)
        expected = '^information about Aftakking \d{10,12}:\n$'
        self.assertRegex(infoString, expected)

    def test_build_string_version_dotnotation_empty_class2(self):
        infoString = Verkeersregelaar().__str__(use_dotnotation=True)
        expected = '^information about Verkeersregelaar \d{10,12}:\n$'
        self.assertRegex(infoString, expected)

    def test_make_string_version_dotnotation_empty_class(self):
        v = Verkeersregelaar()
        string_version = OTLObjectHelper().build_string_version(v, indent=4)
        expected = ''
        self.assertEqual(string_version, expected)

    def test_make_string_version_dotnotation_StringField(self):
        v = Verkeersregelaar()
        v.naam = 'VR'
        string_version = OTLObjectHelper().build_string_version(v, indent=4)
        expected = 'naam : VR'
        self.assertEqual(string_version, expected)

    def test_make_string_version_dotnotation_DtcIdentificator(self):
        v = Verkeersregelaar()
        v._assetId.add_empty_value()
        v.assetId.identificator = 'eigen_id'
        v.assetId.toegekendDoor = 'AWV'
        string_version = OTLObjectHelper().build_string_version(v, indent=4)
        expected = 'assetId.identificator : eigen_id\nassetId.toegekendDoor : AWV'
        self.assertEqual(string_version, expected)

    def test_make_string_version_dotnotation_complex_kardinaliteit(self):
        v = Verkeersregelaar()
        v._externeReferentie.add_empty_value()
        v.externeReferentie[0].externReferentienummer = "externe referentie 2"
        v.externeReferentie[0].externePartij = "bij externe partij 2"

        v._externeReferentie.add_empty_value()
        v.externeReferentie[1].externReferentienummer = "externe referentie 1"
        v.externeReferentie[1].externePartij = "bij externe partij 1"
        string_version = OTLObjectHelper().build_string_version(v, indent=4)
        expected = "externeReferentie[].externReferentienummer : ['externe referentie 2', 'externe referentie 1']\n" \
                   "externeReferentie[].externePartij : ['bij externe partij 2', 'bij externe partij 1']"
        self.assertEqual(string_version, expected)

    def test_create_dict_from_asset_testclass(self):
        with self.subTest('Complex datatype: Dtc'):
            instance = AllCasesTestClass()
            instance.testComplexType.testStringField = 'string'
            instance.testComplexType.testBooleanField = True

            d = instance.create_dict_from_asset()
            expected = {'testComplexType': {
                'testBooleanField': True,
                'testStringField': 'string'}}
            self.assertDictEqual(expected, d)

        with self.subTest('simple attributes'):
            instance = AllCasesTestClass()
            instance.testStringField = 'string'
            instance.testBooleanField = True
            instance.testKeuzelijst = 'waarde-2'
            instance.testDecimalField = 1.5
            instance.testDateField = date(year=2022, month=2, day=2)

            d = instance.create_dict_from_asset()
            expected = {'testBooleanField': True,
                        'testDateField': '2022-02-02',
                        'testDecimalField': 1.5,
                        'testKeuzelijst': 'waarde-2',
                        'testStringField': 'string'}
            self.assertDictEqual(expected, d)

        with self.subTest('simple attributes with cardinality'):
            instance = AllCasesTestClass()
            instance._testStringFieldMetKard.add_value('string')
            instance._testStringFieldMetKard.add_value('string 2')
            instance._testKeuzelijstMetKard.add_value('waarde-1')
            instance._testKeuzelijstMetKard.add_value('waarde-2')
            instance._testDecimalFieldMetKard.add_value(1.5)
            instance._testDecimalFieldMetKard.add_value(2.5)

            d = instance.create_dict_from_asset()
            expected = {'testDecimalFieldMetKard': [1.5, 2.5],
                        'testKeuzelijstMetKard': ['waarde-1', 'waarde-2'],
                        'testStringFieldMetKard': ['string', 'string 2']}
            self.assertDictEqual(expected, d)

        with self.subTest('simple types with waarde_shortcuts'):
            instance = AllCasesTestClass()
            instance.testKwantWrd.waarde = 3.5
            instance._testKwantWrdMetKard.add_empty_value()
            instance.testKwantWrdMetKard[0].waarde = 4.5
            instance._testKwantWrdMetKard.add_empty_value()
            instance.testKwantWrdMetKard[1].waarde = 5.5

            d = instance.create_dict_from_asset(waarde_shortcut=True)
            expected = {'testKwantWrd': 3.5,
                        'testKwantWrdMetKard': [4.5, 5.5]}
            self.assertDictEqual(expected, d)

            d = instance.create_dict_from_asset(waarde_shortcut=False)
            expected = {'testKwantWrd': {'waarde': 3.5},
                        'testKwantWrdMetKard': [{'waarde': 4.5}, {'waarde': 5.5}]}
            self.assertDictEqual(expected, d)

        with self.subTest('complex attributes'):
            instance = AllCasesTestClass()
            instance.testComplexType.testStringField = 'string'
            instance.testComplexType.testBooleanField = True
            instance.testComplexType.testKwantWrd.waarde = 1.5
            instance.testComplexType.testComplexType2.testStringField = 'string in complex'
            instance.testComplexType.testComplexType2._testStringFieldMetKard.add_value('string in complex')
            instance.testComplexType.testComplexType2._testStringFieldMetKard.add_value('string 2 in complex')

            d = instance.create_dict_from_asset(waarde_shortcut=True)
            expected = {
                'testComplexType': {'testBooleanField': True,
                                    'testStringField': 'string',
                                    'testKwantWrd': 1.5,
                                    'testComplexType2': {'testStringField': 'string in complex',
                                                         'testStringFieldMetKard': ['string in complex', 'string 2 in complex']}}}
            self.assertDictEqual(expected, d)

        with self.subTest('complex attributes with cardinality'):
            instance = AllCasesTestClass()
            instance._testComplexTypeMetKard.add_empty_value()
            instance.testComplexTypeMetKard[0].testStringField = 'string 1'
            instance.testComplexTypeMetKard[0].testBooleanField = True
            instance._testComplexTypeMetKard.add_empty_value()
            instance.testComplexTypeMetKard[1].testStringField = 'string 2'
            instance.testComplexTypeMetKard[1].testBooleanField = False
            instance.testComplexTypeMetKard[1].testComplexType2.testStringField = 'string in complex'

            d = instance.create_dict_from_asset(waarde_shortcut=True)
            expected = {
                'testComplexTypeMetKard': [{'testBooleanField': True,
                                            'testStringField': 'string 1'},
                                           {'testBooleanField': False,
                                            'testStringField': 'string 2',
                                            'testComplexType2': {'testStringField': 'string in complex'}}
                                           ]}
            self.assertDictEqual(expected, d)
