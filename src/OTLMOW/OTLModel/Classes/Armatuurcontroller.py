# coding=utf-8
from OTLMOW.OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from OTLMOW.OTLModel.Classes.Communicatieapparatuur import Communicatieapparatuur
from OTLMOW.OTLModel.Classes.FirmwareObject import FirmwareObject
from OTLMOW.OTLModel.Datatypes.StringField import StringField


# Generated with OTLClassCreator. To modify: extend, do not edit
class Armatuurcontroller(Communicatieapparatuur, FirmwareObject):
    """Controller die op het verlichtingstoestel wordt gemonteerd en die één verlichtingstoestel aanstuurt."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Armatuurcontroller'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        Communicatieapparatuur.__init__(self)
        FirmwareObject.__init__(self)

        self._merk = OTLAttribuut(field=StringField,
                                  naam='merk',
                                  label='merk',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Armatuurcontroller.merk',
                                  definition='Merk van de armatuurcontroller.')

        self._modelnaam = OTLAttribuut(field=StringField,
                                       naam='modelnaam',
                                       label='modelnaam',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Armatuurcontroller.modelnaam',
                                       definition='Modelnaam van de armatuurcontroller.')

        self._serienummer = OTLAttribuut(field=StringField,
                                         naam='serienummer',
                                         label='serienummer',
                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Armatuurcontroller.serienummer',
                                         definition='Het unieke nummer waarmee het toestel door de fabrikant geïdentificeerd is.')

    @property
    def merk(self):
        """Merk van de armatuurcontroller."""
        return self._merk.waarde

    @merk.setter
    def merk(self, value):
        self._merk.set_waarde(value, owner=self)

    @property
    def modelnaam(self):
        """Modelnaam van de armatuurcontroller."""
        return self._modelnaam.waarde

    @modelnaam.setter
    def modelnaam(self, value):
        self._modelnaam.set_waarde(value, owner=self)

    @property
    def serienummer(self):
        """Het unieke nummer waarmee het toestel door de fabrikant geïdentificeerd is."""
        return self._serienummer.waarde

    @serienummer.setter
    def serienummer(self, value):
        self._serienummer.set_waarde(value, owner=self)
