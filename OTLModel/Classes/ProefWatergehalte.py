# coding=utf-8
from OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from OTLModel.Classes.Proef import Proef
from OTLModel.Datatypes.DtcDocument import DtcDocument


# Generated with OTLClassCreator. To modify: extend, do not edit
class ProefWatergehalte(Proef):
    """Bepaling van de hoeveelheid water die opgenomen kan worden in een betonverharding."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/proefenmeting#ProefWatergehalte'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self._watergehalte = OTLAttribuut(field=DtcDocument,
                                          naam='watergehalte',
                                          label='watergehalte',
                                          objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/proefenmeting#ProefWatergehalte.watergehalte',
                                          definition='Het resultaat van de test van het gemeten watergehalte in de BV laag.')

    @property
    def watergehalte(self):
        """Het resultaat van de test van het gemeten watergehalte in de BV laag."""
        return self._watergehalte.waarde

    @watergehalte.setter
    def watergehalte(self, value):
        self._watergehalte.set_waarde(value, owner=self)
