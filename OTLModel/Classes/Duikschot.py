# coding=utf-8
from OTLModel.Classes.AIMObject import AIMObject
from OTLModel.Datatypes.DtcDocument import DtcDocument


# Generated with OTLClassCreator. To modify: extend, do not edit
class Duikschot(AIMObject):
    """Duikschotten onder het wateroppervlak dicht bij de overstortrand verhinderen dat het drijvende materiaal meevloeit met het water."""

    typeURI = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Duikschot"
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.technischeFiche = DtcDocument()
        """De technische fiche van het duikschot."""
        self.technischeFiche.naam = "technischeFiche"
        self.technischeFiche.label = "technische fiche"
        self.technischeFiche.uri = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Duikschot.technischeFiche"
        self.technischeFiche.definition = "De technische fiche van het duikschot."
        self.technischeFiche.constraints = ""
        self.technischeFiche.usagenote = ""
        self.technischeFiche.deprecated_version = ""
