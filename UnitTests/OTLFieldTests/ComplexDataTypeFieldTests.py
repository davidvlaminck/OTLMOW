import unittest

from OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from OTLModel.Datatypes.DtcRechtspersoon import DtcRechtspersoon
from OTLModel.Datatypes.DtcIdentificator import DtcIdentificator


class DtcTestClass:
    def __init__(self):
        self._assetId = OTLAttribuut(field=DtcIdentificator,
                                     naam='assetId',
                                     label='asset-id',
                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#AIMObject.assetId',
                                     definition='Unieke identificatie van de asset zoals toegekend door de assetbeheerder of n.a.v. eerste aanlevering door de leverancier.')

        self._persoon = OTLAttribuut(field=DtcRechtspersoon,
                                              naam='persoon',
                                              label='persoon',
                                              objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#AIMObject.persoon',
                                              kardinaliteit_max='*',
                                              definition='Persoon definitie')

    @property
    def assetId(self):
        """Unieke identificatie van de asset zoals toegekend door de assetbeheerder of n.a.v. eerste aanlevering door de leverancier."""
        return self._assetId.waarde

    @assetId.setter
    def assetId(self, value):
        self._assetId.set_waarde(value, owner=self)

    @property
    def persoon(self):
        """Persoon definitie"""
        return self._persoon.waarde

    @persoon.setter
    def persoon(self, value):
        self._persoon.set_waarde(value, owner=self)


class ComplexDataTypeFieldTests(unittest.TestCase):
    def test_DtcIdentificator(self):
        instance = DtcTestClass()
        instance.assetId.identificator = "abc"
        instance.assetId.toegekendDoor = "def"
        self.assertEqual("abc", instance.assetId.identificator)
        self.assertEqual("def", instance.assetId.toegekendDoor)

    def test_dtcPersoon(self):
        instance = DtcTestClass()
        instance.persoon.afdeling = "afdeling"
        self.assertEqual("afdeling", instance.persoon.afdeling)

        instance.persoon.adres.straatnaam = "straat"
        self.assertEqual("straat", instance.persoon.adres.straatnaam)



