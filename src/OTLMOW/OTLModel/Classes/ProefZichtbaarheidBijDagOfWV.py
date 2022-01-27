# coding=utf-8
from src.OTLMOW.OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from src.OTLMOW.OTLModel.Classes.Proef import Proef
from src.OTLMOW.OTLModel.Datatypes.FloatOrDecimalField import FloatOrDecimalField


# Generated with OTLClassCreator. To modify: extend, do not edit
class ProefZichtbaarheidBijDagOfWV(Proef):
    """Bepaling van de luminantiecoëfficiënt bij diffuse verlichting van een gemarkeerd oppervlak (Qd) bij daglicht of onder openbare verlichting."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/proefenmeting#ProefZichtbaarheidBijDagOfWV'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self._luminantiecoëfficiënt = OTLAttribuut(field=FloatOrDecimalField,
                                                   naam='luminantiecoëfficiënt',
                                                   label='luminantiecoëfficient',
                                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/proefenmeting#ProefZichtbaarheidBijDagOfWV.luminantiecoëfficiënt',
                                                   usagenote='uitgedrukt in mcd. m-2.lux-1',
                                                   definition='De verhouding van de luminantie van het oppervlak in een gegeven richting en de verlichtingssterkte op het oppervlak.')

    @property
    def luminantiecoëfficiënt(self):
        """De verhouding van de luminantie van het oppervlak in een gegeven richting en de verlichtingssterkte op het oppervlak."""
        return self._luminantiecoëfficiënt.waarde

    @luminantiecoëfficiënt.setter
    def luminantiecoëfficiënt(self, value):
        self._luminantiecoëfficiënt.set_waarde(value, owner=self)
