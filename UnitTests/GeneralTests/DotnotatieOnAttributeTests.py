from unittest import TestCase

from OTLMOW.Facility.SettingsManager import SettingsManager
from TestClasses.OTLModel.Classes.Onderdeel.AllCasesTestClass import AllCasesTestClass


class DotnotationOnAttributeTests(TestCase):
    def test_dotnotation_on_attribute(self):
        instance = AllCasesTestClass()

        with self.subTest('complex attribute'):
            self.assertEqual('testComplexType', instance._testComplexType.dotnotation)
            self.assertEqual('testComplexType.testBooleanField', instance.testComplexType._testBooleanField.dotnotation)
            self.assertEqual('testComplexType.testComplexType2', instance.testComplexType._testComplexType2.dotnotation)
            self.assertEqual('testComplexType.testComplexType2.testStringField',
                             instance.testComplexType.testComplexType2._testStringField.dotnotation)
            self.assertEqual('testComplexType.testComplexType2.testKwantWrd',
                             instance.testComplexType.testComplexType2._testKwantWrd.dotnotation)
            self.assertEqual('testComplexType.testComplexType2.testKwantWrd.waarde',
                             instance.testComplexType.testComplexType2.testKwantWrd._waarde.dotnotation)

        with self.subTest('complex attribute with cardinality'):
            self.assertEqual('testComplexTypeMetKard[]', instance._testComplexTypeMetKard.dotnotation)
            self.assertEqual('testComplexTypeMetKard[].testBooleanField',
                             instance.testComplexTypeMetKard[0]._testBooleanField.dotnotation)
            self.assertEqual('testComplexTypeMetKard[].testComplexType2MetKard[]',
                             instance.testComplexTypeMetKard[0]._testComplexType2MetKard.dotnotation)
            self.assertEqual('testComplexTypeMetKard[].testComplexType2MetKard[].testStringFieldMetKard[]',
                             instance.testComplexTypeMetKard[0].testComplexType2MetKard[0]._testStringFieldMetKard.dotnotation)

        with self.subTest('non-complex attributes'):
            self.assertEqual('testKeuzelijst', instance._testKeuzelijst.dotnotation)
            self.assertEqual('testStringField', instance._testStringField.dotnotation)
            self.assertEqual('testBooleanField', instance._testBooleanField.dotnotation)
            self.assertEqual('testDecimalField', instance._testDecimalField.dotnotation)

        with self.subTest('non-complex attribute with cardinality'):
            self.assertEqual('testKeuzelijstMetKard[]', instance._testKeuzelijstMetKard.dotnotation)
            self.assertEqual('testStringFieldMetKard[]', instance._testStringFieldMetKard.dotnotation)
            self.assertEqual('testDecimalFieldMetKard[]', instance._testDecimalFieldMetKard.dotnotation)

        with self.subTest('dte attribute'):
            self.assertEqual('testEenvoudigType', instance._testEenvoudigType.dotnotation)

        with self.subTest('kwant waarde attribute'):
            self.assertEqual('testKwantWrd', instance._testKwantWrd.dotnotation)
            self.assertEqual('testKwantWrd.waarde', instance.testKwantWrd._waarde.dotnotation)
            self.assertEqual('testKwantWrd.standaardEenheid', instance.testKwantWrd._standaardEenheid.dotnotation)
            self.assertEqual('testKwantWrdMetKard[]', instance._testKwantWrdMetKard.dotnotation)
            self.assertEqual('testKwantWrdMetKard[].waarde', instance.testKwantWrdMetKard[0]._waarde.dotnotation)
            self.assertEqual('testKwantWrdMetKard[].standaardEenheid',
                             instance.testKwantWrdMetKard[0]._standaardEenheid.dotnotation)

        with self.subTest('union attribute'):
            self.assertEqual('testUnionType', instance._testUnionType.dotnotation)
            self.assertEqual('testUnionType.unionString', instance.testUnionType._unionString.dotnotation)
            self.assertEqual('testUnionType.unionKwantWrd', instance.testUnionType._unionKwantWrd.dotnotation)
            self.assertEqual('testUnionType.unionKwantWrd.waarde', instance.testUnionType.unionKwantWrd._waarde.dotnotation)

        with self.subTest('union attribute with cardinality'):
            self.assertEqual('testUnionTypeMetKard[]', instance._testUnionTypeMetKard.dotnotation)
            self.assertEqual('testUnionTypeMetKard[].unionString', instance.testUnionTypeMetKard[0]._unionString.dotnotation)
            self.assertEqual('testUnionTypeMetKard[].unionKwantWrd', instance.testUnionTypeMetKard[0]._unionKwantWrd.dotnotation)
            self.assertEqual('testUnionTypeMetKard[].unionKwantWrd.waarde',
                             instance.testUnionTypeMetKard[0].unionKwantWrd._waarde.dotnotation)

    def test_use_settingsmanager_to_change_dotnotation(self):
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
        self.assertEqual('testKwantWrdMetKard(),waarde', instance.testKwantWrdMetKard[0]._waarde.dotnotation)

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

    def test_dotnotation_using_waarde_shortcut(self):
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
        self.assertEqual('testKwantWrdMetKard[]', instance.testKwantWrdMetKard[0]._waarde.dotnotation)

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

