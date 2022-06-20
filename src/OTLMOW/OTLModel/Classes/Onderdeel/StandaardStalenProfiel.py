# coding=utf-8
from OTLMOW.OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from OTLMOW.OTLModel.Classes.Abstracten.StalenProfiel import StalenProfiel
from OTLMOW.OTLModel.Datatypes.DtcProfieltype import DtcProfieltype


# Generated with OTLClassCreator. To modify: extend, do not edit
class StandaardStalenProfiel(StalenProfiel):
    """Een stalen constructie-element waarvan de lengte vele malen groter is dan de breedte en de hoogte in doorsnede. Standaard stalen profiel omvat de meest genormeerde soorten profielen, zoals H-, I- en U-profielen met voorgedefinieerde profielhoogtematen."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#StandaardStalenProfiel'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self._profieltype = OTLAttribuut(field=DtcProfieltype,
                                         naam='profieltype',
                                         label='profieltype',
                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#StandaardStalenProfiel.profieltype',
                                         definition='Soort van profiel gecombineerd met de hoogte.',
                                         owner=self)

    @property
    def profieltype(self):
        """Soort van profiel gecombineerd met de hoogte."""
        return self._profieltype.get_waarde()

    @profieltype.setter
    def profieltype(self, value):
        self._profieltype.set_waarde(value, owner=self)
