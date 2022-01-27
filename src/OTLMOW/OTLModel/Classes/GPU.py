# coding=utf-8
from src.OTLMOW.OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from src.OTLMOW.OTLModel.Classes.AIMNaamObject import AIMNaamObject
from src.OTLMOW.OTLModel.Datatypes.KlGPUMerk import KlGPUMerk
from src.OTLMOW.OTLModel.Datatypes.KlGPUModelnaam import KlGPUModelnaam


# Generated with OTLClassCreator. To modify: extend, do not edit
class GPU(AIMNaamObject):
    """Grafische verwerkingseenheid."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#GPU'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self._merk = OTLAttribuut(field=KlGPUMerk,
                                  naam='merk',
                                  label='merk',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#GPU.merk',
                                  definition='Het merk van de GPU.')

        self._modelnaam = OTLAttribuut(field=KlGPUModelnaam,
                                       naam='modelnaam',
                                       label='modelnaam',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#GPU.modelnaam',
                                       definition='De modelnaam van de GPU.')

    @property
    def merk(self):
        """Het merk van de GPU."""
        return self._merk.waarde

    @merk.setter
    def merk(self, value):
        self._merk.set_waarde(value, owner=self)

    @property
    def modelnaam(self):
        """De modelnaam van de GPU."""
        return self._modelnaam.waarde

    @modelnaam.setter
    def modelnaam(self, value):
        self._modelnaam.set_waarde(value, owner=self)
