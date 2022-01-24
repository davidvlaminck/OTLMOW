# coding=utf-8
from OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from OTLModel.Classes.Proef import Proef
from OTLModel.Datatypes.KwantWrdInCelsius import KwantWrdInCelsius


# Generated with OTLClassCreator. To modify: extend, do not edit
class ProefTemperatuur(Proef):
    """Controle van de temperatuur van een asfaltmengsel."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/proefenmeting#ProefTemperatuur'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self._temperatuur = OTLAttribuut(field=KwantWrdInCelsius,
                                         naam='temperatuur',
                                         label='temperatuur',
                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/proefenmeting#ProefTemperatuur.temperatuur',
                                         definition='De temperatuur van de BV laag in graden Celsius.')

    @property
    def temperatuur(self):
        """De temperatuur van de BV laag in graden Celsius."""
        return self._temperatuur.waarde

    @temperatuur.setter
    def temperatuur(self, value):
        self._temperatuur.set_waarde(value, owner=self)
