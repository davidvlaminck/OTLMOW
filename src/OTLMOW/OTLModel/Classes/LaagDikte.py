# coding=utf-8
from OTLMOW.OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from abc import abstractmethod, ABC
from OTLMOW.OTLModel.Datatypes.KwantWrdInCentimeter import KwantWrdInCentimeter


# Generated with OTLClassCreator. To modify: extend, do not edit
class LaagDikte(ABC):
    """Abstracte waarmee aan een laag het attribuut dikte wordt toegekend."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#LaagDikte'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    @abstractmethod
    def __init__(self):
        self._dikte = OTLAttribuut(field=KwantWrdInCentimeter,
                                   naam='dikte',
                                   label='dikte',
                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#LaagDikte.dikte',
                                   definition='De gemiddelde dikte van een laag in centimeter.')

    @property
    def dikte(self):
        """De gemiddelde dikte van een laag in centimeter."""
        return self._dikte.waarde

    @dikte.setter
    def dikte(self, value):
        self._dikte.set_waarde(value, owner=self)
