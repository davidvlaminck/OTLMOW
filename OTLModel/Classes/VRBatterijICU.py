# coding=utf-8
from OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from OTLModel.Classes.VRModuleZFirmware import VRModuleZFirmware
from OTLModel.Datatypes.KlVRBatterijCUMerk import KlVRBatterijCUMerk
from OTLModel.Datatypes.KlVRBatterijCUModelnaam import KlVRBatterijCUModelnaam


# Generated with OTLClassCreator. To modify: extend, do not edit
class VRBatterijICU(VRModuleZFirmware):
    """Batterij die zorgt dat de primaire melding "spanning afwezig", in het geval van een spanningsuitval, nog kan doorgestuurd worden naar het afstandsbewakingssysteem."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#VRBatterijICU'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self._merk = OTLAttribuut(field=KlVRBatterijCUMerk,
                                  naam='merk',
                                  label='merk',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#VRBatterijICU.merk',
                                  definition='De merknaam van de VR-batterij ICU.')

        self._modelnaam = OTLAttribuut(field=KlVRBatterijCUModelnaam,
                                       naam='modelnaam',
                                       label='modelnaam',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#VRBatterijICU.modelnaam',
                                       definition='De modelnaam van de VR-batterij ICU.')

    @property
    def merk(self):
        """De merknaam van de VR-batterij ICU."""
        return self._merk.waarde

    @merk.setter
    def merk(self, value):
        self._merk.set_waarde(value, owner=self)

    @property
    def modelnaam(self):
        """De modelnaam van de VR-batterij ICU."""
        return self._modelnaam.waarde

    @modelnaam.setter
    def modelnaam(self, value):
        self._modelnaam.set_waarde(value, owner=self)
