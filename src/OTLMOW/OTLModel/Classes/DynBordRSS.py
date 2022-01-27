# coding=utf-8
from OTLMOW.OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from OTLMOW.OTLModel.Classes.LEDBord import LEDBord
from OTLMOW.OTLModel.Datatypes.KlDynBordRSSMerk import KlDynBordRSSMerk
from OTLMOW.OTLModel.Datatypes.KlDynBordRSSModelnaam import KlDynBordRSSModelnaam


# Generated with OTLClassCreator. To modify: extend, do not edit
class DynBordRSS(LEDBord):
    """Dynamisch verkeersbord voor rijstrooksignalisatie (RSS)."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DynBordRSS'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self._merk = OTLAttribuut(field=KlDynBordRSSMerk,
                                  naam='merk',
                                  label='merk',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DynBordRSS.merk',
                                  definition='Merk van het dynamische bord.')

        self._modelnaam = OTLAttribuut(field=KlDynBordRSSModelnaam,
                                       naam='modelnaam',
                                       label='modelnaam',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DynBordRSS.modelnaam',
                                       definition='Modelnaam van het RSS-bord.')

    @property
    def merk(self):
        """Merk van het dynamische bord."""
        return self._merk.waarde

    @merk.setter
    def merk(self, value):
        self._merk.set_waarde(value, owner=self)

    @property
    def modelnaam(self):
        """Modelnaam van het RSS-bord."""
        return self._modelnaam.waarde

    @modelnaam.setter
    def modelnaam(self, value):
        self._modelnaam.set_waarde(value, owner=self)
