# coding=utf-8
from OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from OTLModel.Classes.LEDBord import LEDBord
from OTLModel.Datatypes.KlDynBordRVMSMerk import KlDynBordRVMSMerk
from OTLModel.Datatypes.KlDynBordRVMSModelnaam import KlDynBordRVMSModelnaam


# Generated with OTLClassCreator. To modify: extend, do not edit
class DynBordRVMS(LEDBord):
    """Dynamisch verkeersbord dat dynamische verkeerstekens  en teksten kan afbeelden. RVMS staat voor Road-side Variable Message Signs."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DynBordRVMS'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self._merk = OTLAttribuut(field=KlDynBordRVMSMerk,
                                  naam='merk',
                                  label='merk',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DynBordRVMS.merk',
                                  definition='Merk van het dynamische bord.')

        self._modelnaam = OTLAttribuut(field=KlDynBordRVMSModelnaam,
                                       naam='modelnaam',
                                       label='modelnaam',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DynBordRVMS.modelnaam',
                                       definition='Modelnaam van het RVMS-bord.')

    @property
    def merk(self):
        """Merk van het dynamische bord."""
        return self._merk.waarde

    @merk.setter
    def merk(self, value):
        self._merk.set_waarde(value, owner=self)

    @property
    def modelnaam(self):
        """Modelnaam van het RVMS-bord."""
        return self._modelnaam.waarde

    @modelnaam.setter
    def modelnaam(self, value):
        self._modelnaam.set_waarde(value, owner=self)
