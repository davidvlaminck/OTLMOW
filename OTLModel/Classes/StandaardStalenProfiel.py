# coding=utf-8
from OTLModel.BaseClasses.AttributeInfo import AttributeInfo
from OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from OTLModel.Classes.StalenProfiel import StalenProfiel
from OTLModel.Datatypes.DtcProfieltype import DtcProfieltype


# Generated with OTLClassCreator. To modify: extend, do not edit
class StandaardStalenProfiel(StalenProfiel, AttributeInfo):
    """Een stalen constructie-element waarvan de lengte vele malen groter is dan de breedte en de hoogte in doorsnede. Standaard stalen profiel omvat de meest genormeerde soorten profielen, zoals H-, I- en U-profielen met voorgedefinieerde profielhoogtematen."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#StandaardStalenProfiel'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        AttributeInfo.__init__(self)
        StalenProfiel.__init__(self)

        self._profieltype = OTLAttribuut(field=DtcProfieltype,
                                         naam='profieltype',
                                         label='profieltype',
                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#StandaardStalenProfiel.profieltype',
                                         definition='Soort van profiel gecombineerd met de hoogte.')

    @property
    def profieltype(self):
        """Soort van profiel gecombineerd met de hoogte."""
        return self._profieltype.waarde

    @profieltype.setter
    def profieltype(self, value):
        self._profieltype.set_waarde(value, owner=self)
