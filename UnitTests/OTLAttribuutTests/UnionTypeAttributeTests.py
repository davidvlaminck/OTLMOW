from unittest import TestCase

from OTLMOW.Facility.Exceptions.CouldNotConvertToCorrectType import CouldNotConvertToCorrectType
from OTLMOW.Facility.Exceptions.UnionTypeError import UnionTypeError
from TestClasses.OTLModel.Classes.AllCasesTestClass import AllCasesTestClass


class NonStringableObject(object):
    def __str__(self):
        pass


class UnionTypeAttributeTests(TestCase):
    def test_full_test_on_testclass_kard_1(self):
        instance = AllCasesTestClass()
        with self.subTest('empty instance'):
            self.assertIsNotNone(instance.testUnionType)

        with self.subTest('assign values to UnionType with kard 1'):
            instance.testUnionType.unionString = '1'
            self.assertEqual('1', instance.testUnionType.unionString)
            instance.testUnionType.unionKwantWrd.waarde = 2
            self.assertEqual(2, instance.testUnionType.unionKwantWrd.waarde)
            self.assertEqual(None, instance.testUnionType.unionString)

        with self.subTest('setting None to UnionType with kard 1'):
            instance.testUnionType.unionKwantWrd.waarde = None
            self.assertEqual(None, instance.testUnionType.unionKwantWrd.waarde)
            self.assertEqual(None, instance.testUnionType.unionString)

    def test_full_test_on_testclass_kard_more(self):
        instance = AllCasesTestClass()
        with self.subTest('empty instance'):
            self.assertIsNotNone(instance.testUnionTypeMetKard)

        with self.subTest('assign value to UnionType with kard * by using add_empty_value method'):
            instance.testUnionTypeMetKard[0].unionString = '1'
            self.assertEqual('1', instance.testUnionTypeMetKard[0].unionString)
            instance._testUnionTypeMetKard.add_empty_value()
            instance.testUnionTypeMetKard[1].unionKwantWrd.waarde = 2
            self.assertEqual('1', instance.testUnionTypeMetKard[0].unionString)
            self.assertEqual(2, instance.testUnionTypeMetKard[1].unionKwantWrd.waarde)

        with self.subTest('assign bad value to UnionType with kard *'):
            with self.assertRaises(CouldNotConvertToCorrectType):
                instance.testUnionTypeMetKard[1].unionKwantWrd.waarde = 'a'

        with self.subTest('assign value directly to UnionType with kard *'):
            with self.assertRaises(UnionTypeError):
                instance.testUnionTypeMetKard = ['1']
