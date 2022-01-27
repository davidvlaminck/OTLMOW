# coding=utf-8
from OTLMOW.OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from abc import abstractmethod
from OTLMOW.OTLModel.Classes.VerkeersregelaarModule import VerkeersregelaarModule
from OTLMOW.OTLModel.Classes.FirmwareObject import FirmwareObject
from OTLMOW.OTLModel.Datatypes.KlVRModuleMetFirmwareMerk import KlVRModuleMetFirmwareMerk
from OTLMOW.OTLModel.Datatypes.KlVRModuleMetFirmwareModelnaam import KlVRModuleMetFirmwareModelnaam


# Generated with OTLClassCreator. To modify: extend, do not edit
class VRModuleMetFirmware(VerkeersregelaarModule, FirmwareObject):
    """Abstracte voor modules met firmware van een verkeersregelaar."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#VRModuleMetFirmware'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    @abstractmethod
    def __init__(self):
        FirmwareObject.__init__(self)
        VerkeersregelaarModule.__init__(self)

        self._merk = OTLAttribuut(field=KlVRModuleMetFirmwareMerk,
                                  naam='merk',
                                  label='merk',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#VRModuleMetFirmware.merk',
                                  definition='Het merk van de VR module met Firmware.')

        self._modelnaam = OTLAttribuut(field=KlVRModuleMetFirmwareModelnaam,
                                       naam='modelnaam',
                                       label='modelnaam',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#VRModuleMetFirmware.modelnaam',
                                       definition='De modelnaam/product range van de VR module met Firmware.')

    @property
    def merk(self):
        """Het merk van de VR module met Firmware."""
        return self._merk.waarde

    @merk.setter
    def merk(self, value):
        self._merk.set_waarde(value, owner=self)

    @property
    def modelnaam(self):
        """De modelnaam/product range van de VR module met Firmware."""
        return self._modelnaam.waarde

    @modelnaam.setter
    def modelnaam(self, value):
        self._modelnaam.set_waarde(value, owner=self)
