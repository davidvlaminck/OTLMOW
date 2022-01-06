# coding=utf-8
from OTLModel.Classes.AIMObject import AIMObject
from OTLModel.Datatypes.DtcDocument import DtcDocument


# Generated with OTLClassCreator. To modify: extend, do not edit
class Baanlichaam(AIMObject):
    """De lagen tussen het baanbed en het baanoppervlak."""

    typeURI = "https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Baanlichaam"
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.dwarsprofiel = DtcDocument()
        """Een dwarsprofiel is een doorsnijding van een terrein of constructie met een verticaal vlak, aangebracht loodrecht op de as ervan."""
        self.dwarsprofiel.naam = "dwarsprofiel"
        self.dwarsprofiel.label = "dwarsprofiel"
        self.dwarsprofiel.uri = "https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Baanlichaam.dwarsprofiel"
        self.dwarsprofiel.definition = "Een dwarsprofiel is een doorsnijding van een terrein of constructie met een verticaal vlak, aangebracht loodrecht op de as ervan."
        self.dwarsprofiel.constraints = ""
        self.dwarsprofiel.usagenote = "Bestanden van het type xlsx, dwg of pdf."
        self.dwarsprofiel.deprecated_version = ""

        self.horizontaleLigging = DtcDocument()
        """De horizontale ligging van het baanlichaam als document bijlage."""
        self.horizontaleLigging.naam = "horizontaleLigging"
        self.horizontaleLigging.label = "horizontale ligging"
        self.horizontaleLigging.uri = "https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Baanlichaam.horizontaleLigging"
        self.horizontaleLigging.definition = "De horizontale ligging van het baanlichaam als document bijlage."
        self.horizontaleLigging.constraints = ""
        self.horizontaleLigging.usagenote = "Bestanden van het type xlsx, dwg of pdf."
        self.horizontaleLigging.deprecated_version = ""

        self.langsprofiel = DtcDocument()
        """Een langsprofiel is een doorsnijding van een terrein of constructie met een verticaal vlak, aangebracht in de lengterichting van de as ervan."""
        self.langsprofiel.naam = "langsprofiel"
        self.langsprofiel.label = "langsprofiel"
        self.langsprofiel.uri = "https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Baanlichaam.langsprofiel"
        self.langsprofiel.definition = "Een langsprofiel is een doorsnijding van een terrein of constructie met een verticaal vlak, aangebracht in de lengterichting van de as ervan."
        self.langsprofiel.constraints = ""
        self.langsprofiel.usagenote = "Bestanden van het type xlsx, dwg of pdf."
        self.langsprofiel.deprecated_version = ""
