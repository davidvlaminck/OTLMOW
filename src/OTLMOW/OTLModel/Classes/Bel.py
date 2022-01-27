# coding=utf-8
from src.OTLMOW.OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from src.OTLMOW.OTLModel.Classes.AIMNaamObject import AIMNaamObject
from src.OTLMOW.OTLModel.Datatypes.DtcDocument import DtcDocument


# Generated with OTLClassCreator. To modify: extend, do not edit
class Bel(AIMNaamObject):
    """Toestel dat door middel van een geluidssignaal de aandacht vestigt op een situatie."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bel'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self._technischeFiche = OTLAttribuut(field=DtcDocument,
                                             naam='technischeFiche',
                                             label='technische fiche',
                                             objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bel.technischeFiche',
                                             definition='De technische fiche van een bel.')

    @property
    def technischeFiche(self):
        """De technische fiche van een bel."""
        return self._technischeFiche.waarde

    @technischeFiche.setter
    def technischeFiche(self, value):
        self._technischeFiche.set_waarde(value, owner=self)
