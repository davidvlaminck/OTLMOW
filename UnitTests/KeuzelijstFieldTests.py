import unittest

from ModelGenerator.BaseClasses.KeuzelijstField import KeuzelijstField


class TestKeuzeLijst(KeuzelijstField):
    def __init__(self, optionByLabel: str = None):
        super().__init__(naam="TestKeuzeLijst", label="TestKeuzeLijst",
                         uri="https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#TestKeuzeLijst",
                         definition="TestKeuzeLijst definitie", constraints="", usagenote="",
                         deprecated_version="", codelist="codelist")
        self.add_option('optie1', 'optie 1', 'definitie 1', 'typeURI 1')
        self.add_option('optie2', 'optie 2', 'definitie 2', 'typeURI 2')

        if optionByLabel is not None:
            self.set_value_by_label(optionByLabel)


class KeuzelijstFieldTests(unittest.TestCase):
    def test_InitField(self):
        veld = TestKeuzeLijst()
        self.assertTrue(isinstance(veld, TestKeuzeLijst))
        self.assertTrue(isinstance(veld, KeuzelijstField))
        self.assertTrue(veld.waarde is None)

    def test_AssignCorrectValue(self):
        veld = TestKeuzeLijst()
        veld.set_value_by_label('optie 2')
        self.assertTrue(veld.waarde.label == 'optie 2')
        self.assertTrue(veld.waarde.invulwaarde == 'optie2')

    def test_AssignCorrectValueSetInConstructor(self):
        veld = TestKeuzeLijst('optie 2')
        self.assertTrue(veld.waarde.label == 'optie 2')
        self.assertTrue(veld.waarde.invulwaarde == 'optie2')

    def test_AssignIncorrectValue(self):
        veld = TestKeuzeLijst()
        with self.assertRaises(ValueError):
            veld.set_value_by_label('optie 3')
        self.assertTrue(veld.waarde is None)
