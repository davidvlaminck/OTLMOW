# coding=utf-8
from src.OTLMOW.OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from src.OTLMOW.OTLModel.Classes.AIMObject import AIMObject
from src.OTLMOW.OTLModel.Datatypes.DtcDocument import DtcDocument


# Generated with OTLClassCreator. To modify: extend, do not edit
class Duikschot(AIMObject):
    """Duikschotten onder het wateroppervlak dicht bij de overstortrand verhinderen dat het drijvende materiaal meevloeit met het water."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Duikschot'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self._technischeFiche = OTLAttribuut(field=DtcDocument,
                                             naam='technischeFiche',
                                             label='technische fiche',
                                             objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Duikschot.technischeFiche',
                                             definition='De technische fiche van het duikschot.')

    @property
    def technischeFiche(self):
        """De technische fiche van het duikschot."""
        return self._technischeFiche.waarde

    @technischeFiche.setter
    def technischeFiche(self, value):
        self._technischeFiche.set_waarde(value, owner=self)
