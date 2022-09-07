# coding=utf-8
from OTLMOW.OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from OTLMOW.OTLModel.Classes.Abstracten.HardwareToegang import HardwareToegang
from OTLMOW.OTLModel.Datatypes.IntegerField import IntegerField
from OTLMOW.OTLModel.Datatypes.KlHardwareMerk import KlHardwareMerk
from OTLMOW.OTLModel.Datatypes.KlHardwareModelnaam import KlHardwareModelnaam
from OTLMOW.OTLModel.Datatypes.KlHardwareVormfactor import KlHardwareVormfactor
from OTLMOW.GeometrieArtefact.PuntGeometrie import PuntGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class Hardware(HardwareToegang, PuntGeometrie):
    """Fysieke componenten of onderdelen van een computer."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Hardware'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        HardwareToegang.__init__(self)
        PuntGeometrie.__init__(self)

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Kast')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Cluster')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Dongle')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Hardware')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Rack')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Sturing', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#UPS')

        self._aantalUnits = OTLAttribuut(field=IntegerField,
                                         naam='aantalUnits',
                                         label='aantal units',
                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Hardware.aantalUnits',
                                         definition='Het aantal units dat een server in een rack inneemt.',
                                         owner=self)

        self._merk = OTLAttribuut(field=KlHardwareMerk,
                                  naam='merk',
                                  label='merk',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Hardware.merk',
                                  definition='Het merk van de hardware.',
                                  owner=self)

        self._modelnaam = OTLAttribuut(field=KlHardwareModelnaam,
                                       naam='modelnaam',
                                       label='modelnaam',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Hardware.modelnaam',
                                       definition='De modelnaam van de hardware.',
                                       owner=self)

        self._vormfactor = OTLAttribuut(field=KlHardwareVormfactor,
                                        naam='vormfactor',
                                        label='vormfactor',
                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Hardware.vormfactor',
                                        definition='Het soort toestel waarin de fysieke componenten of onderdelen worden vormgegeven.',
                                        owner=self)

    @property
    def aantalUnits(self):
        """Het aantal units dat een server in een rack inneemt."""
        return self._aantalUnits.get_waarde()

    @aantalUnits.setter
    def aantalUnits(self, value):
        self._aantalUnits.set_waarde(value, owner=self)

    @property
    def merk(self):
        """Het merk van de hardware."""
        return self._merk.get_waarde()

    @merk.setter
    def merk(self, value):
        self._merk.set_waarde(value, owner=self)

    @property
    def modelnaam(self):
        """De modelnaam van de hardware."""
        return self._modelnaam.get_waarde()

    @modelnaam.setter
    def modelnaam(self, value):
        self._modelnaam.set_waarde(value, owner=self)

    @property
    def vormfactor(self):
        """Het soort toestel waarin de fysieke componenten of onderdelen worden vormgegeven."""
        return self._vormfactor.get_waarde()

    @vormfactor.setter
    def vormfactor(self, value):
        self._vormfactor.set_waarde(value, owner=self)
