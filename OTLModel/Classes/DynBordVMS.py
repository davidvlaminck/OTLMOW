# coding=utf-8
from OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from OTLModel.Classes.LEDBord import LEDBord
from OTLModel.Datatypes.KlDynBordVMSMerk import KlDynBordVMSMerk
from OTLModel.Datatypes.KlDynBordVMSModelnaam import KlDynBordVMSModelnaam


# Generated with OTLClassCreator. To modify: extend, do not edit
class DynBordVMS(LEDBord):
    """Dynamisch verkeersbord dat dynamische verkeerstekens  (linkerzijde) en teksten (rechterzijde) kan afbeelden. VMS staat voor Variable Message Signs."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DynBordVMS'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self._merk = OTLAttribuut(field=KlDynBordVMSMerk,
                                  naam='merk',
                                  label='merk',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DynBordVMS.merk',
                                  definition='Merk van het dynamische bord.')

        self._modelnaam = OTLAttribuut(field=KlDynBordVMSModelnaam,
                                       naam='modelnaam',
                                       label='modelnaam',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DynBordVMS.modelnaam',
                                       definition='Modelnaam van het VMS-bord.')

    @property
    def merk(self):
        """Merk van het dynamische bord."""
        return self._merk.waarde

    @merk.setter
    def merk(self, value):
        self._merk.set_waarde(value, owner=self)

    @property
    def modelnaam(self):
        """Modelnaam van het VMS-bord."""
        return self._modelnaam.waarde

    @modelnaam.setter
    def modelnaam(self, value):
        self._modelnaam.set_waarde(value, owner=self)
