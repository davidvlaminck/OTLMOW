# coding=utf-8
from src.OTLMOW.OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from abc import abstractmethod, ABC
from src.OTLMOW.OTLModel.Datatypes.StringField import StringField


# Generated with OTLClassCreator. To modify: extend, do not edit
class FirmwareObject(ABC):
    """Abstracte voor de firmware van het object."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#FirmwareObject'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    @abstractmethod
    def __init__(self):
        self._firmwareversie = OTLAttribuut(field=StringField,
                                            naam='firmwareversie',
                                            label='firmwareversie',
                                            objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#FirmwareObject.firmwareversie',
                                            definition='Versie van de firmware.')

    @property
    def firmwareversie(self):
        """Versie van de firmware."""
        return self._firmwareversie.waarde

    @firmwareversie.setter
    def firmwareversie(self, value):
        self._firmwareversie.set_waarde(value, owner=self)
