# coding=utf-8
from OTLMOW.OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from OTLMOW.OTLModel.Classes.IVRIComponent import IVRIComponent
from OTLMOW.OTLModel.Datatypes.KlIVRIMerkITSapp import KlIVRIMerkITSapp
from OTLMOW.OTLModel.Datatypes.KlIVRIModelITSapp import KlIVRIModelITSapp


# Generated with OTLClassCreator. To modify: extend, do not edit
class ITSapp(IVRIComponent):
    """Functionele software component die de intelligente regel applicaties aanbiedt aan de intelligente verkeersregelaars."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#ITSapp'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self._merk = OTLAttribuut(field=KlIVRIMerkITSapp,
                                  naam='merk',
                                  label='merk',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#ITSapp.merk',
                                  definition='De merknaam van de ITSapp; duidt op de leverancier of producent van de iVRI component.',
                                  owner=self)

        self._modelnaam = OTLAttribuut(field=KlIVRIModelITSapp,
                                       naam='modelnaam',
                                       label='modelnaam',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#ITSapp.modelnaam',
                                       definition='De modelnaam/product range van de ITSapp.',
                                       owner=self)

    @property
    def merk(self):
        """De merknaam van de ITSapp; duidt op de leverancier of producent van de iVRI component."""
        return self._merk.get_waarde()

    @merk.setter
    def merk(self, value):
        self._merk.set_waarde(value, owner=self)

    @property
    def modelnaam(self):
        """De modelnaam/product range van de ITSapp."""
        return self._modelnaam.get_waarde()

    @modelnaam.setter
    def modelnaam(self, value):
        self._modelnaam.set_waarde(value, owner=self)
