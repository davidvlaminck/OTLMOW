# coding=utf-8
from OTLModel.BaseClasses.AttributeInfo import AttributeInfo
from OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from OTLModel.Classes.LEDBord import LEDBord
from OTLModel.Datatypes.KlDynBordPKMerk import KlDynBordPKMerk
from OTLModel.Datatypes.KlDynBordPKModelnaam import KlDynBordPKModelnaam


# Generated with OTLClassCreator. To modify: extend, do not edit
class DynBordPK(LEDBord, AttributeInfo):
    """Dynamisch verkeersbord dat een Pijl of Kruis verkeersteken kan afbeelden."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DynBordPK'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        AttributeInfo.__init__(self)
        LEDBord.__init__(self)

        self._merk = OTLAttribuut(field=KlDynBordPKMerk,
                                  naam='merk',
                                  label='merk',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DynBordPK.merk',
                                  definition='Merk van het dynamische bord.')

        self._modelnaam = OTLAttribuut(field=KlDynBordPKModelnaam,
                                       naam='modelnaam',
                                       label='modelnaam',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DynBordPK.modelnaam',
                                       definition='Modelnaam van het PK-bord.')

    @property
    def merk(self):
        """Merk van het dynamische bord."""
        return self._merk.waarde

    @merk.setter
    def merk(self, value):
        self._merk.set_waarde(value, owner=self)

    @property
    def modelnaam(self):
        """Modelnaam van het PK-bord."""
        return self._modelnaam.waarde

    @modelnaam.setter
    def modelnaam(self, value):
        self._modelnaam.set_waarde(value, owner=self)
