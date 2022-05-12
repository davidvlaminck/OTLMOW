import unittest

from AllCasesTestClass import AllCasesTestClass, DtcTestComplexTypeWaarden


class ComplexDataTypeFieldTests(unittest.TestCase):
    def test_full_test_on_testclass_kard_1(self):
        instance = AllCasesTestClass()
        with self.subTest('empty instance'):
            self.assertTrue(isinstance(instance.testComplexType, DtcTestComplexTypeWaarden))
            self.assertIsNone(instance.testComplexType.testStringField)
            self.assertIsNone(instance.testComplexType.testBooleanField)

        instance.testComplexType.testStringField = 'test'
        instance.testComplexType.testBooleanField = True
        with self.subTest('assigned values to complex_type with kard 1'):
            self.assertEqual('test', instance.testComplexType.testStringField)
            self.assertTrue(instance.testComplexType.testBooleanField)



