# coding=utf-8
from OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from OTLModel.Classes.HardwareToegang import HardwareToegang
from OTLModel.Datatypes.IntegerField import IntegerField
from OTLModel.Datatypes.KlHardwareMerk import KlHardwareMerk
from OTLModel.Datatypes.KlHardwareModelnaam import KlHardwareModelnaam
from OTLModel.Datatypes.KlHardwareVormfactor import KlHardwareVormfactor


# Generated with OTLClassCreator. To modify: extend, do not edit
class Hardware(HardwareToegang):
    """Fysieke componenten of onderdelen van een computer."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Hardware'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self._aantalUnits = OTLAttribuut(field=IntegerField,
                                         naam='aantalUnits',
                                         label='aantal units',
                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Hardware.aantalUnits',
                                         definition='Het aantal units dat een server in een rack inneemt.')

        self._merk = OTLAttribuut(field=KlHardwareMerk,
                                  naam='merk',
                                  label='merk',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Hardware.merk',
                                  definition='Het merk van de hardware.')

        self._modelnaam = OTLAttribuut(field=KlHardwareModelnaam,
                                       naam='modelnaam',
                                       label='modelnaam',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Hardware.modelnaam',
                                       definition='De modelnaam van de hardware.')

        self._vormfactor = OTLAttribuut(field=KlHardwareVormfactor,
                                        naam='vormfactor',
                                        label='vormfactor',
                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Hardware.vormfactor',
                                        definition='Het soort toestel waarin de fysieke componenten of onderdelen worden vormgegeven.')

    @property
    def aantalUnits(self):
        """Het aantal units dat een server in een rack inneemt."""
        return self._aantalUnits.waarde

    @aantalUnits.setter
    def aantalUnits(self, value):
        self._aantalUnits.set_waarde(value, owner=self)

    @property
    def merk(self):
        """Het merk van de hardware."""
        return self._merk.waarde

    @merk.setter
    def merk(self, value):
        self._merk.set_waarde(value, owner=self)

    @property
    def modelnaam(self):
        """De modelnaam van de hardware."""
        return self._modelnaam.waarde

    @modelnaam.setter
    def modelnaam(self, value):
        self._modelnaam.set_waarde(value, owner=self)

    @property
    def vormfactor(self):
        """Het soort toestel waarin de fysieke componenten of onderdelen worden vormgegeven."""
        return self._vormfactor.waarde

    @vormfactor.setter
    def vormfactor(self, value):
        self._vormfactor.set_waarde(value, owner=self)
