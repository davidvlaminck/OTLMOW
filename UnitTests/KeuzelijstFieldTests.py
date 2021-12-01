import unittest

from ModelGenerator.BaseClasses.KeuzelijstField import KeuzelijstField
from ModelGenerator.BaseClasses.Keuzelijst import Keuzelijst


class TestKeuzeLijst(Keuzelijst):
    def __init__(self):
        super(TestKeuzeLijst, self).__init__('TestKeuzeLijst', 'Test KeuzeLijst',
                                            "https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/TestKeuzeLijst")
        self.addOption('optie1', 'optie 1', 'definitie 1', 'uri 1')
        self.addOption('optie2', 'optie 2', 'definitie 2', 'uri 2')


class KeuzelijstFieldTests(unittest.TestCase):
    def test_InitField(self):
        veld = KeuzelijstField(TestKeuzeLijst())
        self.assertTrue(isinstance(veld.keuzelijst, TestKeuzeLijst))
        self.assertTrue(veld.value is None)

    def test_AssignCorrectValue(self):
        veld = KeuzelijstField(TestKeuzeLijst())
        veld.setValueByLabel('optie 2')
        self.assertTrue(veld.value.label == 'optie 2')
        self.assertTrue(veld.value.waarde == 'optie2')

    def test_AssignIncorrectValue(self):
        veld = KeuzelijstField(TestKeuzeLijst())
        with self.assertRaises(ValueError):
            veld.setValueByLabel('optie 3')
        self.assertTrue(veld.value is None)



