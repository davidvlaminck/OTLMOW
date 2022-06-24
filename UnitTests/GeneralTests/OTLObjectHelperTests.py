import unittest

from TestClasses.OTLModel.Classes.Onderdeel.AllCasesTestClass import AllCasesTestClass


class OTLObjectHelperTest(unittest.TestCase):
    def test_list_attributes_and_values_by_dotnotation_simple_attributes(self):
        instance = AllCasesTestClass()
        instance.testKeuzelijst = 'waarde-2'
        instance.testBooleanField = True
        attribute_list = list(instance.list_attributes_and_values_by_dotnotation())
        expected_list = [('testBooleanField', True),
                         ('testKeuzelijst', 'waarde-2')]
        self.assertListEqual(expected_list, attribute_list)

    def test_list_attributes_and_values_by_dotnotation_complex_attributes(self):
        instance = AllCasesTestClass()
        instance.testComplexType.testStringField = 'string 1'
        instance.testComplexType.testComplexType2.testStringField = 'string 2'
        instance.testUnionType.unionKwantWrd.waarde = 2.0
        attribute_list = list(instance.list_attributes_and_values_by_dotnotation())
        expected_list = [('testComplexType.testComplexType2.testStringField', 'string 2'),
                         ('testComplexType.testStringField', 'string 1'),
                         ('testUnionType.unionKwantWrd.waarde', 2.0)]
        self.assertListEqual(expected_list, attribute_list)

    def test_list_attributes_and_values_by_dotnotation_attributes_with_cardinality(self):
        instance = AllCasesTestClass()
        instance.testStringFieldMetKard = ['a', 'b']
        instance.testComplexType.testStringFieldMetKard = ['c', 'd']
        instance._testComplexTypeMetKard.add_empty_value()
        instance.testComplexTypeMetKard[0].testStringField = 'e'
        instance._testComplexTypeMetKard.add_empty_value()
        instance.testComplexTypeMetKard[1].testStringField = 'f'
        attribute_list = list(instance.list_attributes_and_values_by_dotnotation())
        expected_list = [('testComplexType.testStringFieldMetKard[]', ['c', 'd']),
                         ('testComplexTypeMetKard[].testStringField', ['e', 'f']),
                         ('testStringFieldMetKard[]', ['a', 'b'])]
        self.assertListEqual(expected_list, attribute_list)

    def test_list_attributes_and_values_by_dotnotation_waarde_shortcut(self):
        instance = AllCasesTestClass()
        instance.testComplexType._testKwantWrdMetKard.add_empty_value()
        instance.testComplexType._testKwantWrdMetKard.add_empty_value()
        instance.testComplexType.testKwantWrdMetKard[0].waarde = 3.0
        instance.testComplexType.testKwantWrdMetKard[1].waarde = 4.0
        instance.testComplexType.testComplexType2.testKwantWrd.waarde = 5.0
        instance.testUnionType.unionKwantWrd.waarde = 2.0
        attribute_list = list(instance.list_attributes_and_values_by_dotnotation(waarde_shortcut=True))
        expected_list = [('testComplexType.testComplexType2.testKwantWrd', 5.0),
                         ('testComplexType.testKwantWrdMetKard[]', [3.0, 4.0]),
                         ('testUnionType.unionKwantWrd', 2.0)]
        self.assertListEqual(expected_list, attribute_list)