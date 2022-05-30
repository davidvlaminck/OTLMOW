from unittest import TestCase

from AllCasesTestClass import AllCasesTestClass
from OTLMOW.Facility.SettingsManager import SettingsManager


class DotnotatieOnAttributeTests(TestCase):
    def test_dotnotatie_on_attribute(self):
        instance = AllCasesTestClass()

        with self.subTest('complex attribute'):
            self.assertEqual('testComplexType', instance._testComplexType.dotnotatie)
            self.assertEqual('testComplexType.testBooleanField', instance.testComplexType._testBooleanField.dotnotatie)
            self.assertEqual('testComplexType.testComplexType2', instance.testComplexType._testComplexType2.dotnotatie)
            self.assertEqual('testComplexType.testComplexType2.testStringField',
                             instance.testComplexType.testComplexType2._testStringField.dotnotatie)
            self.assertEqual('testComplexType.testComplexType2.testKwantWrd',
                             instance.testComplexType.testComplexType2._testKwantWrd.dotnotatie)
            self.assertEqual('testComplexType.testComplexType2.testKwantWrd.waarde',
                             instance.testComplexType.testComplexType2.testKwantWrd._waarde.dotnotatie)

        with self.subTest('complex attribute with cardinality'):
            self.assertEqual('testComplexTypeMetKard[]', instance._testComplexTypeMetKard.dotnotatie)
            self.assertEqual('testComplexTypeMetKard[].testBooleanField',
                             instance.testComplexTypeMetKard[0]._testBooleanField.dotnotatie)
            self.assertEqual('testComplexTypeMetKard[].testComplexType2MetKard[]',
                             instance.testComplexTypeMetKard[0]._testComplexType2MetKard.dotnotatie)
            self.assertEqual('testComplexTypeMetKard[].testComplexType2MetKard[].testStringFieldMetKard[]',
                             instance.testComplexTypeMetKard[0].testComplexType2MetKard[0]._testStringFieldMetKard.dotnotatie)

        with self.subTest('non-complex attributes'):
            self.assertEqual('testKeuzelijst', instance._testKeuzelijst.dotnotatie)
            self.assertEqual('testStringField', instance._testStringField.dotnotatie)
            self.assertEqual('testBooleanField', instance._testBooleanField.dotnotatie)
            self.assertEqual('testDecimalNumberField', instance._testDecimalNumberField.dotnotatie)

        with self.subTest('non-complex attribute with cardinality'):
            self.assertEqual('testKeuzelijstMetKard[]', instance._testKeuzelijstMetKard.dotnotatie)
            self.assertEqual('testStringFieldMetKard[]', instance._testStringFieldMetKard.dotnotatie)
            self.assertEqual('testDecimalNumberFieldMetKard[]', instance._testDecimalNumberFieldMetKard.dotnotatie)

        with self.subTest('dte attribute'):
            self.assertEqual('testEenvoudigType', instance._testEenvoudigType.dotnotatie)

        with self.subTest('kwant waarde attribute'):
            self.assertEqual('testKwantWrd', instance._testKwantWrd.dotnotatie)
            self.assertEqual('testKwantWrd.waarde', instance.testKwantWrd._waarde.dotnotatie)
            self.assertEqual('testKwantWrd.standaardEenheid', instance.testKwantWrd._standaardEenheid.dotnotatie)
            self.assertEqual('testKwantWrdMetKard[]', instance._testKwantWrdMetKard.dotnotatie)
            self.assertEqual('testKwantWrdMetKard[].waarde', instance.testKwantWrdMetKard[0]._waarde.dotnotatie)
            self.assertEqual('testKwantWrdMetKard[].standaardEenheid',
                             instance.testKwantWrdMetKard[0]._standaardEenheid.dotnotatie)

        with self.subTest('union attribute'):
            self.assertEqual('testUnionType', instance._testUnionType.dotnotatie)
            self.assertEqual('testUnionType.unionString', instance.testUnionType._unionString.dotnotatie)
            self.assertEqual('testUnionType.unionKwantWrd', instance.testUnionType._unionKwantWrd.dotnotatie)
            self.assertEqual('testUnionType.unionKwantWrd.waarde', instance.testUnionType.unionKwantWrd._waarde.dotnotatie)

        with self.subTest('union attribute with cardinality'):
            self.assertEqual('testUnionTypeMetKard[]', instance._testUnionTypeMetKard.dotnotatie)
            self.assertEqual('testUnionTypeMetKard[].unionString', instance.testUnionTypeMetKard[0]._unionString.dotnotatie)
            self.assertEqual('testUnionTypeMetKard[].unionKwantWrd', instance.testUnionTypeMetKard[0]._unionKwantWrd.dotnotatie)
            self.assertEqual('testUnionTypeMetKard[].unionKwantWrd.waarde',
                             instance.testUnionTypeMetKard[0].unionKwantWrd._waarde.dotnotatie)

    def test_use_settingsmanager_to_change_dotnotatie(self):
        settingsmanager = SettingsManager(settings_path='')
        settingsmanager.settings['file_formats'] = [
            {'name': 'OTLMOW',
             'dotnotation': {
                 'separator': ',',
                 'cardinality separator': '|',
                 'cardinality indicator': '()',
                 'waarde_shortcut_applicable': False}
             }]
        settingsmanager.load_settings_in_app()

        instance = AllCasesTestClass()
        self.assertEqual('testKwantWrdMetKard(),waarde', instance.testKwantWrdMetKard[0]._waarde.dotnotatie)

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

    def test_dotnotatie_using_waarde_shortcut(self):
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
        self.assertEqual('testKwantWrdMetKard[]', instance.testKwantWrdMetKard[0]._waarde.dotnotatie)

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

