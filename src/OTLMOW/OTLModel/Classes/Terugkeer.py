# coding=utf-8
from OTLMOW.OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from OTLMOW.OTLModel.Classes.ComplexeGeleiding import ComplexeGeleiding
from OTLMOW.OTLModel.Datatypes.KlEcoOverstaptype import KlEcoOverstaptype


# Generated with OTLClassCreator. To modify: extend, do not edit
class Terugkeer(ComplexeGeleiding):
    """Een mogelijkheid om dieren die toch aan de wegkant verzeild zijn geraakt terug naar de veilige kant te laten begeven."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Terugkeer'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self._typeUitvoering = OTLAttribuut(field=KlEcoOverstaptype,
                                            naam='typeUitvoering',
                                            label='type uitvoering',
                                            objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Terugkeer.typeUitvoering',
                                            definition='Het type van terugkeer.')

    @property
    def typeUitvoering(self):
        """Het type van terugkeer."""
        return self._typeUitvoering.waarde

    @typeUitvoering.setter
    def typeUitvoering(self, value):
        self._typeUitvoering.set_waarde(value, owner=self)
