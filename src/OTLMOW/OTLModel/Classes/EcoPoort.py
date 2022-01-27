# coding=utf-8
from src.OTLMOW.OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from src.OTLMOW.OTLModel.Classes.ComplexeGeleiding import ComplexeGeleiding
from src.OTLMOW.OTLModel.Datatypes.KlEcoPoorttype import KlEcoPoorttype
from src.OTLMOW.OTLModel.Datatypes.KwantWrdInMeter import KwantWrdInMeter


# Generated with OTLClassCreator. To modify: extend, do not edit
class EcoPoort(ComplexeGeleiding):
    """Een afsluitbare doorgang om mensen toe te laten tot het gebied."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#EcoPoort'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self._breedte = OTLAttribuut(field=KwantWrdInMeter,
                                     naam='breedte',
                                     label='breedte',
                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#EcoPoort.breedte',
                                     definition='De breedte van de poort in meter.')

        self._poortType = OTLAttribuut(field=KlEcoPoorttype,
                                       naam='poortType',
                                       label='poort type',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#EcoPoort.poortType',
                                       definition='Bepaling van het type van poort.')

    @property
    def breedte(self):
        """De breedte van de poort in meter."""
        return self._breedte.waarde

    @breedte.setter
    def breedte(self, value):
        self._breedte.set_waarde(value, owner=self)

    @property
    def poortType(self):
        """Bepaling van het type van poort."""
        return self._poortType.waarde

    @poortType.setter
    def poortType(self, value):
        self._poortType.set_waarde(value, owner=self)
