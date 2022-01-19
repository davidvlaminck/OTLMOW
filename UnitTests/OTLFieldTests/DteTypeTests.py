import decimal
import unittest
from abc import ABC

from OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from OTLModel.Datatypes.DteKleurRAL import DteKleurRAL
from OTLModel.Datatypes.StringField import StringField
from OTLModel.Classes.AIMObject import AIMObject


class DteTestClass(AIMObject, ABC):
    def __init__(self):
        self._kleur = OTLAttribuut(field=DteKleurRAL,
                                   naam='kleur',
                                   label='kleur',
                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Lichtmast.kleur',
                                   definition='RAL kleur van de lichtmast.')

    @property
    def kleur(self):
        """RAL kleur van de lichtmast."""
        return self._kleur.waarde

    @kleur.setter
    def kleur(self, value):
        self._kleur.set_waarde(value, owner=self)


class RelatiesTests(unittest.TestCase):
    def test_DteTestClass(self):
        instance = DteTestClass()

        self.assertEqual(instance._kleur.field, DteKleurRAL)

        instance.kleur.waarde = "1111"
        self.assertEqual("1111", instance.kleur.waarde)

        with self.assertRaises(TypeError):
            instance.kleur.waarde = 2.0

        self.assertTrue(isinstance(instance.kleur.waarde, str))
