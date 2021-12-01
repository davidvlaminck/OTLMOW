import unittest

from ModelGenerator.BaseClasses.KeuzelijstField import KeuzelijstField


class KeuzelijstFieldTests(unittest.TestCase):
    def test_InitField(self):
        veld = KeuzelijstField('naam', 'label', 'uri')
        veld.addOption('optie1', 'optie 1', 'definitie', 'uri')

    def test_CheckFields(self):
        veld = KeuzelijstField('naam', 'label', 'uri')
        veld.addOption('optie1', 'optie 1', 'definitie', 'uri')
        listOptions = veld.getOptions()
        self.assertTrue(listOptions[0].waarde == 'optie1')
        self.assertTrue(listOptions[0].label == 'optie 1')
        self.assertTrue(listOptions[0].uri == 'uri')
        self.assertTrue(listOptions[0].definitie == 'definitie')

    def test_FindOptionByValue(self):
        veld = KeuzelijstField('naam', 'label', 'uri')
        veld.addOption('optie1', 'optie 1', 'definitie', 'uri')
        option = veld.getOptionByValue('optie1')
        self.assertTrue(option.label == 'optie 1')

    def test_FindSecondOptionByValue(self):
        veld = KeuzelijstField('naam', 'label', 'uri')
        veld.addOption('optie1', 'optie 1', 'definitie', 'uri')
        veld.addOption('optie2', 'optie 2', 'definitie2', 'uri2')
        option = veld.getOptionByValue('optie2')
        self.assertTrue(option.label == 'optie 2')

    def test_FindSecondOptionByLabel(self):
        veld = KeuzelijstField('naam', 'label', 'uri')
        veld.addOption('optie1', 'optie 1', 'definitie', 'uri')
        veld.addOption('optie2', 'optie 2', 'definitie2', 'uri2')
        option = veld.getOptionByLabel('optie 2')
        self.assertTrue(option.waarde == 'optie2')