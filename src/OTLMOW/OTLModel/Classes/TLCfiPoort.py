# coding=utf-8
from src.OTLMOW.OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from src.OTLMOW.OTLModel.Classes.IVRIComponent import IVRIComponent
from src.OTLMOW.OTLModel.Datatypes.KlIVRIMerkTLCfi import KlIVRIMerkTLCfi
from src.OTLMOW.OTLModel.Datatypes.KlIVRIModelTLCfi import KlIVRIModelTLCfi


# Generated with OTLClassCreator. To modify: extend, do not edit
class TLCfiPoort(IVRIComponent):
    """Functionele software component die een TLC-FI interface aanbiedt waardoor data kan uitgewisseld worden voor intelligente verkeersregelaars."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#TLCfiPoort'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self._merk = OTLAttribuut(field=KlIVRIMerkTLCfi,
                                  naam='merk',
                                  label='merk',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#TLCfiPoort.merk',
                                  definition='De merknaam van de TLC-fi poort; duidt op de leverancier of producent van de iVRI component.')

        self._modelnaam = OTLAttribuut(field=KlIVRIModelTLCfi,
                                       naam='modelnaam',
                                       label='modelnaam',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#TLCfiPoort.modelnaam',
                                       definition='De modelnaam/product range van de TLC-fi poort.')

    @property
    def merk(self):
        """De merknaam van de TLC-fi poort; duidt op de leverancier of producent van de iVRI component."""
        return self._merk.waarde

    @merk.setter
    def merk(self, value):
        self._merk.set_waarde(value, owner=self)

    @property
    def modelnaam(self):
        """De modelnaam/product range van de TLC-fi poort."""
        return self._modelnaam.waarde

    @modelnaam.setter
    def modelnaam(self, value):
        self._modelnaam.set_waarde(value, owner=self)
