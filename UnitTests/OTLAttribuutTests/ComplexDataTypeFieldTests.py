import unittest

from OTLMOW.Facility.Exceptions.MethodNotApplicableError import MethodNotApplicableError
from UnitTests.TestClasses.OTLModel.Classes.AllCasesTestClass import AllCasesTestClass
from UnitTests.TestClasses.OTLModel.Datatypes.DtcTestComplexType import DtcTestComplexTypeWaarden


class ComplexDataTypeFieldTests(unittest.TestCase):
    def test_full_test_on_testclass_kard_1(self):
        instance = AllCasesTestClass()
        with self.subTest('empty instance'):
            self.assertIsNotNone(instance.testComplexType)

        with self.subTest('assign values to testComplexType with kard 1'):
            self.assertIsNotNone(instance.testComplexType)
            self.assertIsInstance(instance.testComplexType, DtcTestComplexTypeWaarden)

            instance.testComplexType.testStringField = '1'
            self.assertEqual('1', instance.testComplexType.testStringField)
            instance.testComplexType.testBooleanField = True
            self.assertEqual(True, instance.testComplexType.testBooleanField)

        with self.subTest('incorrect use of add_empty_value'):
            with self.assertRaises(RuntimeError):
                instance._testComplexType.add_empty_value()

        with self.subTest('incorrectly assign values to testComplexType with kard 1 directly'):
            with self.assertRaises(ValueError):
                instance.testComplexType = '1'

    def test_full_test_on_testclass_kard_more(self):
        instance = AllCasesTestClass()
        with self.subTest('empty instance'):
            self.assertIsNotNone(instance.testComplexTypeMetKard)

        with self.subTest('assign value to ComplexType with kard * by using add_empty_value method'):
            self.assertIsNotNone(instance.testComplexTypeMetKard)
            self.assertIsInstance(instance.testComplexTypeMetKard, list)
            self.assertIsInstance(instance.testComplexTypeMetKard[0], DtcTestComplexTypeWaarden)
            self.assertEqual(1, len(instance.testComplexTypeMetKard))

            instance.testComplexTypeMetKard[0].testStringField = '1'
            self.assertEqual('1', instance.testComplexTypeMetKard[0].testStringField)
            instance.testComplexTypeMetKard[0].testBooleanField = True
            self.assertEqual(True, instance.testComplexTypeMetKard[0].testBooleanField)

            instance._testComplexTypeMetKard.add_empty_value()
            self.assertIsNotNone(instance.testComplexTypeMetKard)
            self.assertIsInstance(instance.testComplexTypeMetKard[1], DtcTestComplexTypeWaarden)
            self.assertEqual(2, len(instance.testComplexTypeMetKard))

            instance.testComplexTypeMetKard[1].testStringField = '2'
            self.assertEqual('2', instance.testComplexTypeMetKard[1].testStringField)
            instance.testComplexTypeMetKard[1].testBooleanField = False
            self.assertEqual(False, instance.testComplexTypeMetKard[1].testBooleanField)

        with self.subTest('assign value directly to ComplexType with kard *'):
            waardeObject1 = DtcTestComplexTypeWaarden()
            waardeObject1.testStringField = '1'
            waardeObject1.testBooleanField = True

            waardeObject2 = DtcTestComplexTypeWaarden()
            waardeObject2.testStringField = '2'
            waardeObject2.testBooleanField = False

            instance.testComplexTypeMetKard = [waardeObject1]
            self.assertEqual('1', instance.testComplexTypeMetKard[0].testStringField)
            self.assertEqual(True, instance.testComplexTypeMetKard[0].testBooleanField)

            instance.testComplexTypeMetKard = [waardeObject2]
            self.assertEqual('2', instance.testComplexTypeMetKard[0].testStringField)
            self.assertEqual(False, instance.testComplexTypeMetKard[0].testBooleanField)

            instance.testComplexTypeMetKard = [waardeObject1, waardeObject2]
            self.assertEqual('1', instance.testComplexTypeMetKard[0].testStringField)
            self.assertEqual(True, instance.testComplexTypeMetKard[0].testBooleanField)
            self.assertEqual('2', instance.testComplexTypeMetKard[1].testStringField)
            self.assertEqual(False, instance.testComplexTypeMetKard[1].testBooleanField)

    def test_complex_kard_in_complex_kard(self):
        instance = AllCasesTestClass()
        with self.subTest('empty instance'):
            self.assertIsNotNone(instance.testComplexTypeMetKard)

        with self.subTest('assign value to ComplexType with kard *'):
            self.assertIsNotNone(instance.testComplexTypeMetKard)
            self.assertIsInstance(instance.testComplexTypeMetKard, list)
            self.assertIsInstance(instance.testComplexTypeMetKard[0], DtcTestComplexTypeWaarden)
            self.assertEqual(1, len(instance.testComplexTypeMetKard))
            instance.testComplexTypeMetKard[0].testStringField = '1'
            self.assertEqual('1', instance.testComplexTypeMetKard[0].testStringField)
            instance.testComplexTypeMetKard[0].testBooleanField = True
            self.assertEqual(True, instance.testComplexTypeMetKard[0].testBooleanField)

            instance._testComplexTypeMetKard.add_empty_value()
            self.assertIsNotNone(instance.testComplexTypeMetKard)
            self.assertIsInstance(instance.testComplexTypeMetKard[1], DtcTestComplexTypeWaarden)
            self.assertEqual(2, len(instance.testComplexTypeMetKard))

            instance.testComplexTypeMetKard[1].testStringField = '2'
            self.assertEqual('2', instance.testComplexTypeMetKard[1].testStringField)
            instance.testComplexTypeMetKard[1].testBooleanField = False
            self.assertEqual(False, instance.testComplexTypeMetKard[1].testBooleanField)

        with self.subTest('assign value to ComplexType within ComplexType with kard *'):
            instance.testComplexTypeMetKard[0].testComplexType2MetKard[0]._testStringFieldMetKard.add_value('1.1')
            instance.testComplexTypeMetKard[0].testComplexType2MetKard[0]._testStringFieldMetKard.add_value('1.2')
            self.assertEqual('1.1', instance.testComplexTypeMetKard[0].testComplexType2MetKard[0].testStringFieldMetKard[0])
            self.assertEqual('1.2', instance.testComplexTypeMetKard[0].testComplexType2MetKard[0].testStringFieldMetKard[1])