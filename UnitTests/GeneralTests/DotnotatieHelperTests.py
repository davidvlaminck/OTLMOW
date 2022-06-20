import json
from unittest import TestCase

from OTLMOW.Facility.DotnotationHelper import DotnotationHelper
from OTLMOW.Facility.SettingsManager import SettingsManager
from TestClasses.OTLModel.Classes.Onderdeel.AllCasesTestClass import AllCasesTestClass


class JsonLdTestData:
    simple = '{ "a": "value a", "b": "value b" }'
    dict_in_dict = '{ "a": "value a", "b": { "c": "value c", "d": "value d" } }'
    list = '{ "a": [1,2] }'
    listdict_in_dict = '{ "a": "value a", "b": [{ "c": "value c", "d": "value d" }, { "e": "value e", "f": "value f" }]}'


class DotnotationHelperTests(TestCase):
    def test_flatten_dict_simple(self):
        input_dict = json.loads(JsonLdTestData.simple)

        output = DotnotationHelper().flatten_dict(input_dict=input_dict)
        expected = {"a": "value a", "b": "value b"}
        self.assertDictEqual(expected, output)

    def test_flatten_dict_dict_in_dict(self):
        input_dict = json.loads(JsonLdTestData.dict_in_dict)

        output = DotnotationHelper().flatten_dict(input_dict)
        expected = {"a": "value a", "b.c": "value c", "b.d": "value d"}
        self.assertDictEqual(expected, output)

    def test_flatten_dict_list(self):
        input_dict = json.loads(JsonLdTestData.list)

        output = DotnotationHelper().flatten_dict(input_dict=input_dict)
        expected = {"a[0]": 1, "a[1]": 2}
        self.assertDictEqual(expected, output)

    def test_flatten_dict_listdict_in_dict(self):
        input_dict = json.loads(JsonLdTestData.listdict_in_dict)

        output = DotnotationHelper().flatten_dict(input_dict=input_dict)
        expected = {"a": "value a", "b[0].c": "value c", "b[0].d": "value d", "b[1].e": "value e", "b[1].f": "value f"}
        self.assertDictEqual(expected, output)

    def test_get_attributes_by_dotnotation_default_values(self):
        instance = AllCasesTestClass()

        with self.subTest("attribute 1 level deep"):
            result_attribute = DotnotationHelper.get_attributes_by_dotnotation(instance, 'testDecimalField')
            expected_attribute = instance._testDecimalField
            self.assertEqual(expected_attribute, result_attribute)

        with self.subTest("attribute 1 level deep with cardinality > 1"):
            result_attribute = DotnotationHelper.get_attributes_by_dotnotation(instance, 'testStringFieldMetKard[]')
            expected_attribute = instance._testStringFieldMetKard
            self.assertEqual(expected_attribute, result_attribute)

        with self.subTest("attribute 2 levels deep with waarde shortcut disabled"):
            result_attribute = DotnotationHelper.get_attributes_by_dotnotation(instance, 'testKwantWrd.waarde')
            expected_attribute = instance.testKwantWrd._waarde
            self.assertEqual(expected_attribute, result_attribute)

        with self.subTest("attribute 2 levels deep"):
            result_attribute = DotnotationHelper.get_attributes_by_dotnotation(instance, 'testComplexType.testStringField')
            expected_attribute = instance.testComplexType._testStringField
            self.assertEqual(expected_attribute, result_attribute)

        with self.subTest("attribute 2 levels deep with cardinality > 1"):
            result_attribute = DotnotationHelper.get_attributes_by_dotnotation(instance,
                                                                             'testComplexTypeMetKard[].testStringFieldMetKard[]')
            expected_attributes = list(map(lambda c: c._testStringFieldMetKard, instance.testComplexTypeMetKard))
            self.assertEqual(expected_attributes, result_attribute)

        with self.subTest("attribute 3 levels deep"):
            result_attribute = DotnotationHelper.get_attributes_by_dotnotation(instance,
                                                                             'testComplexType.testComplexType2.testStringField')
            expected_attribute = instance.testComplexType.testComplexType2._testStringField
            self.assertEqual(expected_attribute, result_attribute)

        with self.subTest("attribute 3 levels deep with cardinality > 1"):
            result_attribute = DotnotationHelper.get_attributes_by_dotnotation(instance,
                                                                             'testComplexTypeMetKard[].testComplexType2MetKard[].testStringFieldMetKard[]')
            expected_testComplexType2MetKard = list(
                map(lambda c: c._testComplexType2MetKard.waarde, instance.testComplexTypeMetKard))
            expected_attributes = [list(map(lambda c: c[0]._testStringFieldMetKard, expected_testComplexType2MetKard))]
            self.assertEqual(expected_attributes, result_attribute)

        with self.subTest("attribute 4 levels deep with waarde shortcut disabled"):
            result_attribute = DotnotationHelper.get_attributes_by_dotnotation(instance,
                                                                             'testComplexType.testComplexType2.testKwantWrd.waarde')
            expected_attribute = instance.testComplexType.testComplexType2.testKwantWrd._waarde
            self.assertEqual(expected_attribute, result_attribute)

    def test_get_attributes_by_dotnotation_waarde_shortcut(self):
        settingsmanager = SettingsManager(settings_path='')
        settingsmanager.settings['file_formats'] = [
            {'name': 'OTLMOW',
             'dotnotation': {
                 'separator': '.',
                 'cardinality separator': '|',
                 'cardinality indicator': '[]',
                 'waarde_shortcut_applicable': True}
             }]
        settingsmanager.load_settings_in_app()

        instance = AllCasesTestClass()
        with self.subTest("attribute 2 levels deep with waarde shortcut enabled"):
            result_attribute = DotnotationHelper.get_attributes_by_dotnotation(instance, 'testKwantWrd')
            expected_attribute = instance.testKwantWrd._waarde
            self.assertEqual(expected_attribute, result_attribute)

        with self.subTest("attribute 2 levels deep with waarde shortcut enabled and cardinality > 1"):
            result_attribute = DotnotationHelper.get_attributes_by_dotnotation(instance, 'testKwantWrdMetKard[]')
            expected_attribute = [instance.testKwantWrdMetKard[0]._waarde]
            self.assertEqual(expected_attribute, result_attribute)

        with self.subTest("attribute 4 levels deep with waarde shortcut disabled"):
            result_attribute = DotnotationHelper.get_attributes_by_dotnotation(instance,
                                                                             'testComplexType.testComplexType2.testKwantWrd')
            expected_attribute = instance.testComplexType.testComplexType2.testKwantWrd._waarde
            self.assertEqual(expected_attribute, result_attribute)

        # restore original settings
        settingsmanager.settings['file_formats'] = [
            {'name': 'OTLMOW',
             'dotnotation': {
                 'separator': '.',
                 'cardinality separator': '|',
                 'cardinality indicator': '[]',
                 'waarde_shortcut_applicable': False}
             }]
        settingsmanager.load_settings_in_app()

    def test_set_attribute_by_dotnotation_decimal_value_convert_scenarios(self):
        instance = AllCasesTestClass()

        with self.subTest("correctly typed and convert=True"):
            DotnotationHelper.set_attribute_by_dotnotation(instance, 'testDecimalField', 9.0, convert=True)
            self.assertEqual(9.0, instance.testDecimalField)

        with self.subTest("correctly typed and convert=False"):
            DotnotationHelper.set_attribute_by_dotnotation(instance, 'testDecimalField', 8.0, convert=False)
            self.assertEqual(8.0, instance.testDecimalField)

        with self.subTest("incorrectly typed and convert=True"):
            DotnotationHelper.set_attribute_by_dotnotation(instance, 'testDecimalField', "7.0", convert=True)
            self.assertEqual(7.0, instance.testDecimalField)

        with self.subTest("incorrectly typed and convert=False (converted by set_waarde method on attribute itself)"):
            DotnotationHelper.set_attribute_by_dotnotation(instance, 'testDecimalField', "6.0", convert=False)
            self.assertEqual(6.0, instance.testDecimalField)

        with self.subTest("cardinality > 1 and correctly typed and convert=True"):
            DotnotationHelper.set_attribute_by_dotnotation(instance, 'testDecimalFieldMetKard', [9.0], convert=True)
            self.assertEqual(9.0, instance.testDecimalFieldMetKard[0])

        with self.subTest("cardinality > 1 and correctly typed and convert=False"):
            DotnotationHelper.set_attribute_by_dotnotation(instance, 'testDecimalFieldMetKard', [8.0], convert=False)
            self.assertEqual(8.0, instance.testDecimalFieldMetKard[0])

        with self.subTest("cardinality > 1 and incorrectly typed and convert=True"):
            DotnotationHelper.set_attribute_by_dotnotation(instance, 'testDecimalFieldMetKard', ["7.0"], convert=True)
            self.assertEqual(7.0, instance.testDecimalFieldMetKard[0])

        with self.subTest("cardinality > 1 and incorrectly typed and convert=False (converted by set_waarde method on attribute itself)"):
            DotnotationHelper.set_attribute_by_dotnotation(instance, 'testDecimalFieldMetKard', ["6.0"], convert=False)
            self.assertEqual(6.0, instance.testDecimalFieldMetKard[0])

    def test_set_attributes_by_dotnotation_default_values(self):
        instance = AllCasesTestClass()
        settingsmanager = SettingsManager(settings_path='')
        settingsmanager.settings['file_formats'] = [
            {'name': 'OTLMOW',
             'dotnotation': {
                 'separator': '.',
                 'cardinality separator': '|',
                 'cardinality indicator': '[]',
                 'waarde_shortcut_applicable': False}
             }]
        settingsmanager.load_settings_in_app()

        with self.subTest("attribute 1 level deep"):
            DotnotationHelper.set_attribute_by_dotnotation(instance, 'testDecimalField', 6.0)
            self.assertEqual(6.0, instance.testDecimalField)

        with self.subTest("attribute 1 level deep with cardinality > 1"):
            DotnotationHelper.set_attribute_by_dotnotation(instance, 'testStringFieldMetKard[]', ['a', 'b'])
            self.assertEqual(['a', 'b'], instance.testStringFieldMetKard)

        with self.subTest("attribute 2 levels deep with waarde shortcut disabled"):
            DotnotationHelper.set_attribute_by_dotnotation(instance, 'testKwantWrd.waarde', 5.0)
            self.assertEqual(5.0, instance.testKwantWrd.waarde)

        with self.subTest("attribute 2 levels deep"):
            DotnotationHelper.set_attribute_by_dotnotation(instance, 'testComplexType.testStringField', "abc")
            self.assertEqual("abc", instance.testComplexType.testStringField)

        with self.subTest("attribute 2 levels deep with cardinality > 1 and cardinality in first attribute"):
            DotnotationHelper.set_attribute_by_dotnotation(instance, 'testComplexTypeMetKard[].testStringField', ['1.1', '2.1'])
            self.assertEqual('2.1', instance.testComplexTypeMetKard[1].testStringField)

        with self.subTest("attribute 2 levels deep with cardinality > 1 and cardinality in second attribute"):
            DotnotationHelper.set_attribute_by_dotnotation(instance, 'testComplexType.testStringFieldMetKard[]', ['1.1', '1.2'])
            self.assertEqual('1.2', instance.testComplexType.testStringFieldMetKard[1])

        with self.subTest("attribute 2 levels deep with cardinality > 1"):
            DotnotationHelper.set_attribute_by_dotnotation(instance, 'testComplexTypeMetKard[].testStringFieldMetKard[]',
                                                         [['1.1', '1.2'], ['2.1', '2.2']])
            self.assertEqual('2.2', instance.testComplexTypeMetKard[1].testStringFieldMetKard[1])

        with self.subTest("attribute 3 levels deep"):
            DotnotationHelper.set_attribute_by_dotnotation(instance, 'testComplexType.testComplexType2.testStringField', "def")
            self.assertEqual("def", instance.testComplexType.testComplexType2.testStringField)

        with self.subTest("attribute 3 levels deep with cardinality > 1"):
            DotnotationHelper.set_attribute_by_dotnotation(instance, 'testComplexTypeMetKard[].testComplexType2MetKard[].testStringFieldMetKard[]',
                                                         [[['1.1.1', '1.1.2'], ['1.2.1', '1.2.2']],  [['2.1.1', '2.1.2'], ['2.2.1', '2.2.2']]])
            self.assertEqual("2.2.2", instance.testComplexTypeMetKard[1].testComplexType2MetKard[1].testStringFieldMetKard[1])

        with self.subTest("attribute 4 levels deep with waarde shortcut disabled"):
            DotnotationHelper.set_attribute_by_dotnotation(instance, 'testComplexType.testComplexType2.testKwantWrd.waarde', 4.0)
            self.assertEqual(4.0, instance.testComplexType.testComplexType2.testKwantWrd.waarde)

    def test_set_attribute_by_dotnotation_using_settings(self):
        settingsmanager = SettingsManager(settings_path='')
        settingsmanager.settings['file_formats'] = [
            {'name': 'OTLMOW',
             'dotnotation': {
                 'separator': '*',
                 'cardinality separator': '|',
                 'cardinality indicator': '()',
                 'waarde_shortcut_applicable': False}
             }]
        settingsmanager.load_settings_in_app()

        instance = AllCasesTestClass()

        with self.subTest("attribute 1 level deep with cardinality > 1"):
            DotnotationHelper.set_attribute_by_dotnotation(instance, 'testStringFieldMetKard()', ['a', 'b'])
            self.assertEqual(['a', 'b'], instance.testStringFieldMetKard)

        with self.subTest("attribute 2 levels deep"):
            DotnotationHelper.set_attribute_by_dotnotation(instance, 'testComplexType*testStringField', "abc")
            self.assertEqual("abc", instance.testComplexType.testStringField)

        with self.subTest("attribute 2 levels deep with cardinality > 1"):
            DotnotationHelper.set_attribute_by_dotnotation(instance, 'testComplexTypeMetKard()*testStringFieldMetKard()',
                                                         [['1.1', '1.2'], ['2.1', '2.2']])
            self.assertEqual('2.2', instance.testComplexTypeMetKard[1].testStringFieldMetKard[1])

        settingsmanager.settings['file_formats'] = [
            {'name': 'OTLMOW',
             'dotnotation': {
                 'separator': '.',
                 'cardinality separator': '|',
                 'cardinality indicator': '[]',
                 'waarde_shortcut_applicable': False}
             }]
        settingsmanager.load_settings_in_app()

    def test_set_attribute_by_dotnotation_waarde_shortcut(self):
        settingsmanager = SettingsManager(settings_path='')
        settingsmanager.settings['file_formats'] = [
            {'name': 'OTLMOW',
             'dotnotation': {
                 'separator': '.',
                 'cardinality separator': '|',
                 'cardinality indicator': '[]',
                 'waarde_shortcut_applicable': True}
             }]
        settingsmanager.load_settings_in_app()

        instance = AllCasesTestClass()

        with self.subTest("attribute 1 level deep with waarde shortcut enabled"):
            DotnotationHelper.set_attribute_by_dotnotation(instance, 'testKwantWrd', 5.0)
            self.assertEqual(5.0, instance.testKwantWrd.waarde)

        with self.subTest("attribute 1 level deep with cardinality > 1 and waarde shortcut enabled"):
            DotnotationHelper.set_attribute_by_dotnotation(instance, 'testKwantWrdMetKard[]', [0.0, 1.0])
            self.assertEqual(1.0, instance.testKwantWrdMetKard[1].waarde)

        with self.subTest("attribute 2 levels deep with cardinality > 1 (first part) and with waarde shortcut enabled"):
            DotnotationHelper.set_attribute_by_dotnotation(instance, 'testComplexTypeMetKard[].testKwantWrd', [8.0, 9.0])
            self.assertEqual(9.0, instance.testComplexTypeMetKard[1].testKwantWrd.waarde)

        with self.subTest("attribute 2 levels deep with cardinality > 1 (last part) and with waarde shortcut enabled"):
            DotnotationHelper.set_attribute_by_dotnotation(instance, 'testComplexType.testKwantWrdMetKard[]', [2.0, 3.0])
            self.assertEqual(3.0, instance.testComplexType.testKwantWrdMetKard[1].waarde)

        with self.subTest("attribute 3 levels deep with waarde shortcut enabled"):
            DotnotationHelper.set_attribute_by_dotnotation(instance, 'testComplexType.testComplexType2.testKwantWrd', 4.0)
            self.assertEqual(4.0, instance.testComplexType.testComplexType2.testKwantWrd.waarde)

        settingsmanager.settings['file_formats'] = [
            {'name': 'OTLMOW',
             'dotnotation': {
                 'separator': '.',
                 'cardinality separator': '|',
                 'cardinality indicator': '[]',
                 'waarde_shortcut_applicable': False}
             }]
        settingsmanager.load_settings_in_app()
