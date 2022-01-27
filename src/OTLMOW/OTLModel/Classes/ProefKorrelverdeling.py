# coding=utf-8
from src.OTLMOW.OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from src.OTLMOW.OTLModel.Classes.Proef import Proef
from src.OTLMOW.OTLModel.Datatypes.DtcDocument import DtcDocument


# Generated with OTLClassCreator. To modify: extend, do not edit
class ProefKorrelverdeling(Proef):
    """Bepaling van de doorval door een reeks zeven van een granulaatmengsel volgens NBN EN 933-1."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/proefenmeting#ProefKorrelverdeling'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self._korrelverdeling = OTLAttribuut(field=DtcDocument,
                                             naam='korrelverdeling',
                                             label='korrelverdeling',
                                             objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/proefenmeting#ProefKorrelverdeling.korrelverdeling',
                                             definition='Het resultaat van de test van de gemeten korrelverdeling in de BV laag.')

    @property
    def korrelverdeling(self):
        """Het resultaat van de test van de gemeten korrelverdeling in de BV laag."""
        return self._korrelverdeling.waarde

    @korrelverdeling.setter
    def korrelverdeling(self, value):
        self._korrelverdeling.set_waarde(value, owner=self)
