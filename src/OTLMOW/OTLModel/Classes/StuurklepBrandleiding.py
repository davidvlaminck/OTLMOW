# coding=utf-8
from OTLMOW.OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from OTLMOW.OTLModel.Classes.Brandvoorziening import Brandvoorziening
from OTLMOW.OTLModel.Datatypes.BooleanField import BooleanField


# Generated with OTLClassCreator. To modify: extend, do not edit
class StuurklepBrandleiding(Brandvoorziening):
    """Een afsluiter die vanop afstand bediend wordt om te verhinderen dat er water in de leiding blijft staan."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#StuurklepBrandleiding'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self._heeftLeegloopklep = OTLAttribuut(field=BooleanField,
                                               naam='heeftLeegloopklep',
                                               label='heeft leegloopklep',
                                               objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#StuurklepBrandleiding.heeftLeegloopklep',
                                               definition='Voorziet een mogelijkheid om via de klep de brandleiding te laten leeglopen.',
                                               owner=self)

    @property
    def heeftLeegloopklep(self):
        """Voorziet een mogelijkheid om via de klep de brandleiding te laten leeglopen."""
        return self._heeftLeegloopklep.waarde

    @heeftLeegloopklep.setter
    def heeftLeegloopklep(self, value):
        self._heeftLeegloopklep.set_waarde(value, owner=self)
