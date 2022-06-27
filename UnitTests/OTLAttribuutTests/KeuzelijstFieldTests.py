import logging
from unittest import TestCase

from OTLMOW.Facility.Exceptions.RemovedOptionError import RemovedOptionError
from TestClasses.OTLModel.Classes.Onderdeel.AllCasesTestClass import AllCasesTestClass


class NonStringableObject(object):
    def __str__(self):
        pass

# logging.warning = lambda l: None
# logging.error = lambda l: None

class KeuzelijstFieldTests(TestCase):
    def test_adms_status(self):
        instance = AllCasesTestClass()
        with self.subTest('ingebruik value'):
            instance.testKeuzelijst = 'waarde-4'
            self.assertEqual('waarde-4', instance.testKeuzelijst)

        with self.subTest('uitgebruik value'):
            with self.assertWarns(DeprecationWarning):
                instance.testKeuzelijst = 'waarde-5'
                self.assertEqual('waarde-5', instance.testKeuzelijst)

        with self.subTest('verwijderd value'):
            with self.assertRaises(RemovedOptionError):
                instance.testKeuzelijst = 'waarde-6'
                self.assertEqual('waarde-6', instance.testKeuzelijst)

    def test_full_test_on_testclass_kard_1(self):
        instance = AllCasesTestClass()
        with self.subTest('empty instance'):
            self.assertIsNone(instance.testKeuzelijst)

        with self.subTest('assign values to Keuzelijst with kard 1'):
            instance.testKeuzelijst = 'waarde-1'
            self.assertEqual('waarde-1', instance.testKeuzelijst)
            instance.testKeuzelijst = 'waarde-2'
            self.assertEqual('waarde-2', instance.testKeuzelijst)

    def test_full_test_on_testclass_kard_more(self):
        instance = AllCasesTestClass()
        with self.subTest('empty instance'):
            self.assertIsNone(instance.testKeuzelijstMetKard)
            self.assertFalse(instance._testKeuzelijstMetKard.field.waarde_shortcut_applicable)

        with self.subTest('assign value directly to KeuzelijstMetKard with kard *'):
            instance.testKeuzelijstMetKard = ['waarde-1']
            self.assertEqual('waarde-1', instance.testKeuzelijstMetKard[0])

        with self.subTest('assign value to KeuzelijstMetKard with kard * by using add_value method'):
            instance._testKeuzelijstMetKard.add_value('waarde-2')
            self.assertEqual('waarde-1', instance.testKeuzelijstMetKard[0])
            self.assertEqual('waarde-2', instance.testKeuzelijstMetKard[1])

        with self.subTest('assign bad value to KeuzelijstMetKard with kard *'):
            with self.assertRaises(ValueError):
                instance.testKeuzelijstMetKard = ['waarde-1', 'a']
