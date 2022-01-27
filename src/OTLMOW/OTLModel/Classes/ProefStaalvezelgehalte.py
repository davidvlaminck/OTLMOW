# coding=utf-8
from src.OTLMOW.OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from src.OTLMOW.OTLModel.Classes.Proef import Proef
from src.OTLMOW.OTLModel.Datatypes.DtcDocument import DtcDocument


# Generated with OTLClassCreator. To modify: extend, do not edit
class ProefStaalvezelgehalte(Proef):
    """Bepaling van de hoeveelheid staalvezels in de cementbetonverharding."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/proefenmeting#ProefStaalvezelgehalte'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self._staalvezelgehalte = OTLAttribuut(field=DtcDocument,
                                               naam='staalvezelgehalte',
                                               label='staalvezelgehalte',
                                               objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/proefenmeting#ProefStaalvezelgehalte.staalvezelgehalte',
                                               definition='Het resultaat van de test van het gemeten staalvezelgehalte in de BV laag.')

    @property
    def staalvezelgehalte(self):
        """Het resultaat van de test van het gemeten staalvezelgehalte in de BV laag."""
        return self._staalvezelgehalte.waarde

    @staalvezelgehalte.setter
    def staalvezelgehalte(self, value):
        self._staalvezelgehalte.set_waarde(value, owner=self)
