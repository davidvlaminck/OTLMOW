from unittest import TestCase

from AllCasesTestClass import AllCasesTestClass
from OTLMOW.Facility.Exceptions.CouldNotConvertToCorrectType import CouldNotConvertToCorrectType


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

    def test_full_test_on_testclass_kard_more(self):
        instance = AllCasesTestClass()
        with self.subTest('empty instance'):
            self.assertIsNone(instance.testStringFieldMetKard)

        with self.subTest('assign value to stringfield with kard * by using add_value method'):
            instance._testStringFieldMetKard.add_value('1')
            self.assertEqual('1', instance.testStringFieldMetKard[0])
            instance._testStringFieldMetKard.add_value('2')
            self.assertEqual('1', instance.testStringFieldMetKard[0])
            self.assertEqual('2', instance.testStringFieldMetKard[1])

        with self.subTest('assign bad value to stringfield with kard * by using add_value method'):
            with self.assertRaises(CouldNotConvertToCorrectType):
                instance._testStringFieldMetKard.add_value(NonStringableObject())

        with self.subTest('assign value directly to stringfield with kard *'):
            instance.testStringFieldMetKard = ['1']
            self.assertEqual('1', instance.testStringFieldMetKard[0])
            instance.testStringFieldMetKard = ['2']
            self.assertEqual('2', instance.testStringFieldMetKard[0])
            instance.testStringFieldMetKard = ['1', '2']
            self.assertEqual('1', instance.testStringFieldMetKard[0])
            self.assertEqual('2', instance.testStringFieldMetKard[1])
