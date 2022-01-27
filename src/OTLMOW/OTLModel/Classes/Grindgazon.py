# coding=utf-8
from src.OTLMOW.OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from src.OTLMOW.OTLModel.Classes.BegroeidVoorkomen import BegroeidVoorkomen
from src.OTLMOW.OTLModel.Datatypes.BooleanField import BooleanField


# Generated with OTLClassCreator. To modify: extend, do not edit
class Grindgazon(BegroeidVoorkomen):
    """Gazontype specifiek op een gestabiliseerde ondergrond. Het is een substraat ontwikkeld om voertuigen sporadisch toe te laten op gazons zonder dat er spoorvorming optreedt."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Grindgazon'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self._isTweelaags = OTLAttribuut(field=BooleanField,
                                         naam='isTweelaags',
                                         label='is tweelaags',
                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Grindgazon.isTweelaags',
                                         definition='Geeft aan of het grindgazon tweelaags of éénlaags is.')

    @property
    def isTweelaags(self):
        """Geeft aan of het grindgazon tweelaags of éénlaags is."""
        return self._isTweelaags.waarde

    @isTweelaags.setter
    def isTweelaags(self, value):
        self._isTweelaags.set_waarde(value, owner=self)
