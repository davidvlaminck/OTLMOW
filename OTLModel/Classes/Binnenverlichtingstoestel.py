# coding=utf-8
from OTLModel.Classes.AIMObject import AIMObject
from OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLModel.Datatypes.KlBinnenverlichtingstoestelSchakelwijze import KlBinnenverlichtingstoestelSchakelwijze
from OTLModel.Datatypes.KlBinnenverlichtingstoestelSoortLamp import KlBinnenverlichtingstoestelSoortLamp


# Generated with OTLClassCreator. To modify: extend, do not edit
class Binnenverlichtingstoestel(AIMObject):
    """Een verlichtingstoestel dat binnen in een gebouw geplaatst wordt. Een verlichtingstoestel is de combinatie van de lamp en de armatuur."""

    typeURI = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Binnenverlichtingstoestel"
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.schakelwijze = KeuzelijstField(naam="schakelwijze",
                                            label="schakelwijze",
                                            lijst=KlBinnenverlichtingstoestelSchakelwijze(),
                                            uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Binnenverlichtingstoestel.schakelwijze",
                                            definition="Geeft aan hoe het toestel aan- en uitgeschakeld wordt.",
                                            constraints="",
                                            usagenote="",
                                            deprecated_version="")
        """Geeft aan hoe het toestel aan- en uitgeschakeld wordt."""

        self.soortLamp = KeuzelijstField(naam="soortLamp",
                                         label="soort lamp",
                                         lijst=KlBinnenverlichtingstoestelSoortLamp(),
                                         uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Binnenverlichtingstoestel.soortLamp",
                                         definition="Geeft aan welke soort lamp er gebruikt wordt in het binnenverlichtingstoestel.",
                                         constraints="",
                                         usagenote="",
                                         deprecated_version="")
        """Geeft aan welke soort lamp er gebruikt wordt in het binnenverlichtingstoestel."""
