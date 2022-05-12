# coding=utf-8
from OTLMOW.OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from abc import abstractmethod
from OTLMOW.OTLModel.Classes.ArtificieleLaag import ArtificieleLaag
from OTLMOW.OTLModel.Datatypes.KlAlgBouwklassegroep import KlAlgBouwklassegroep


# Generated with OTLClassCreator. To modify: extend, do not edit
class LaagBouwklasse(ArtificieleLaag):
    """Abstracte waarmee aan een laag het attribuut bouwklasse wordt toegekend."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#LaagBouwklasse'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    @abstractmethod
    def __init__(self):
        super().__init__()

        self._bouwklasse = OTLAttribuut(field=KlAlgBouwklassegroep,
                                        naam='bouwklasse',
                                        label='bouwklasse',
                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#LaagBouwklasse.bouwklasse',
                                        definition='Een maat voor de verkeersbelasting over de volledige levensduur van de laag. De laag is ontworpen volgens de aangeduide bouwklasse.',
                                        owner=self)

    @property
    def bouwklasse(self):
        """Een maat voor de verkeersbelasting over de volledige levensduur van de laag. De laag is ontworpen volgens de aangeduide bouwklasse."""
        return self._bouwklasse.get_waarde()

    @bouwklasse.setter
    def bouwklasse(self, value):
        self._bouwklasse.set_waarde(value, owner=self)
