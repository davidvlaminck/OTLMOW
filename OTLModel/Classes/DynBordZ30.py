# coding=utf-8
from OTLModel.BaseClasses.AttributeInfo import AttributeInfo
from OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from OTLModel.Classes.LEDBord import LEDBord
from OTLModel.Datatypes.KlDynBordZ30Merk import KlDynBordZ30Merk
from OTLModel.Datatypes.KlDynBordZ30Modelnaam import KlDynBordZ30Modelnaam


# Generated with OTLClassCreator. To modify: extend, do not edit
class DynBordZ30(LEDBord, AttributeInfo):
    """Dynamisch verkeersbord dat verkeerstekens voor een zone 30 kan weergeven."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DynBordZ30'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        AttributeInfo.__init__(self)
        LEDBord.__init__(self)

        self._merk = OTLAttribuut(field=KlDynBordZ30Merk,
                                  naam='merk',
                                  label='merk',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DynBordZ30.merk',
                                  definition='Merk van het dynamisch zone-30 bord.')

        self._modelnaam = OTLAttribuut(field=KlDynBordZ30Modelnaam,
                                       naam='modelnaam',
                                       label='modelnaam',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DynBordZ30.modelnaam',
                                       definition='De modelnaam van het Z30-bord.')

    @property
    def merk(self):
        """Merk van het dynamisch zone-30 bord."""
        return self._merk.waarde

    @merk.setter
    def merk(self, value):
        self._merk.set_waarde(value, owner=self)

    @property
    def modelnaam(self):
        """De modelnaam van het Z30-bord."""
        return self._modelnaam.waarde

    @modelnaam.setter
    def modelnaam(self, value):
        self._modelnaam.set_waarde(value, owner=self)
