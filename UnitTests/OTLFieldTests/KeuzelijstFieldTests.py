import unittest

from OTLModel.Datatypes.KeuzelijstField import KeuzelijstField, Keuzelijst
from OTLModel.Datatypes.KeuzelijstWaarde import KeuzelijstWaarde


class TestKeuzeLijst(Keuzelijst):
    def __init__(self):
        super().__init__(naam="TestKeuzeLijst", label="TestKeuzeLijst",
                         uri="https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#TestKeuzeLijst",
                         definition="TestKeuzeLijst definitie", usagenote="",
                         deprecated_version="", codelist="codelist")
        self.add_option('optie1', 'optie 1', 'definitie 1', 'typeURI 1')
        self.add_option('optie2', 'optie 2', 'definitie 2', 'typeURI 2')


class TestKeuzeLijstField(KeuzelijstField):
    def __init__(self):
        super().__init__(lijst=TestKeuzeLijst(), naam="TestKeuzeLijstField", label="TestKeuzeLijstField",
                         uri="https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#TestKeuzeLijstField",
                         definition="TestKeuzeLijstField definitie", usagenote="", constraints='', overerving=False,
                         deprecated_version="")


class KeuzelijstFieldTests(unittest.TestCase):
    def test_InitField(self):
        veld = TestKeuzeLijstField()
        self.assertTrue(isinstance(veld.lijst, TestKeuzeLijst))
        self.assertTrue(isinstance(veld, KeuzelijstField))
        self.assertIsNone(veld.waarde)

    def test_AssignCorrectValue(self):
        veld = TestKeuzeLijstField()
        veld.set_value_by_label('optie 2')
        self.assertEqual('optie 2', veld.waarde.label)
        self.assertEqual('optie2', veld.waarde.invulwaarde)
        self.assertTrue(isinstance(veld.waarde, KeuzelijstWaarde))

    def test_AssignIncorrectValue(self):
        veld = TestKeuzeLijstField()
        with self.assertRaises(ValueError):
            veld.set_value_by_label('optie 3')
        self.assertTrue(veld.waarde is None)
