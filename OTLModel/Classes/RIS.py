# coding=utf-8
from OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from OTLModel.Classes.IVRIComponent import IVRIComponent
from OTLModel.Datatypes.KlIVRIMerkRIS import KlIVRIMerkRIS
from OTLModel.Datatypes.KlIVRIModelRIS import KlIVRIModelRIS


# Generated with OTLClassCreator. To modify: extend, do not edit
class RIS(IVRIComponent):
    """Afkorting van Roadside ITS Station. Functionele software component die een RIS aanbiedt voor de werking van intelligente verkeersregelaars."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#RIS'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self._merk = OTLAttribuut(field=KlIVRIMerkRIS,
                                  naam='merk',
                                  label='merk',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#RIS.merk',
                                  definition='De merknaam van de RIS; duidt op de leverancier of producent van de iVRI component.')

        self._modelnaam = OTLAttribuut(field=KlIVRIModelRIS,
                                       naam='modelnaam',
                                       label='modelnaam',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#RIS.modelnaam',
                                       definition='De modelnaam/product range van de RIS.')

    @property
    def merk(self):
        """De merknaam van de RIS; duidt op de leverancier of producent van de iVRI component."""
        return self._merk.waarde

    @merk.setter
    def merk(self, value):
        self._merk.set_waarde(value, owner=self)

    @property
    def modelnaam(self):
        """De modelnaam/product range van de RIS."""
        return self._modelnaam.waarde

    @modelnaam.setter
    def modelnaam(self, value):
        self._modelnaam.set_waarde(value, owner=self)
