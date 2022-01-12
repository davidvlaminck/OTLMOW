# coding=utf-8
from OTLModel.Classes.Proef import Proef
from OTLModel.Datatypes.KwantWrdInCelsius import KwantWrdInCelsius


# Generated with OTLClassCreator. To modify: extend, do not edit
class ProefTemperatuur(Proef):
    """Controle van de temperatuur van een asfaltmengsel."""

    typeURI = "https://wegenenverkeer.data.vlaanderen.be/ns/proefenmeting#ProefTemperatuur"
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.temperatuur = KwantWrdInCelsius()
        """De temperatuur van de BV laag in graden Celsius."""
        self.temperatuur.naam = "temperatuur"
        self.temperatuur.label = "temperatuur"
        self.temperatuur.objectUri = "https://wegenenverkeer.data.vlaanderen.be/ns/proefenmeting#ProefTemperatuur.temperatuur"
        self.temperatuur.definition = "De temperatuur van de BV laag in graden Celsius."
        self.temperatuur.constraints = ""
        self.temperatuur.usagenote = ""
        self.temperatuur.deprecated_version = ""
