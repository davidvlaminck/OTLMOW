# coding=utf-8
from OTLModel.Classes.AIMNaamObject import AIMNaamObject
from OTLModel.Datatypes.BooleanField import BooleanField
from OTLModel.Datatypes.DtcDocument import DtcDocument


# Generated with OTLClassCreator. To modify: extend, do not edit
class FietstelDisplay(AIMNaamObject):
    """Verankerd toestel dat een selectie van telgegevens van het fietstelsysteem toont voor passerende fietsers."""

    typeURI = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#FietstelDisplay"
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.isDubbelzijdig = BooleanField(naam="isDubbelzijdig",
                                           label="is dubbelzijdig",
                                           uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#FietstelDisplay.isDubbelzijdig",
                                           definition="Geeft aan of het display telgegevens toont langs zijn beide zijden of niet.",
                                           constraints="",
                                           usagenote="",
                                           deprecated_version="")
        """Geeft aan of het display telgegevens toont langs zijn beide zijden of niet."""

        self.technischeFiche = DtcDocument()
        """Document met de technische specificaties van het display."""
        self.technischeFiche.naam = "technischeFiche"
        self.technischeFiche.label = "technische fiche"
        self.technischeFiche.uri = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#FietstelDisplay.technischeFiche"
        self.technischeFiche.definition = "Document met de technische specificaties van het display."
        self.technischeFiche.constraints = ""
        self.technischeFiche.usagenote = ""
        self.technischeFiche.deprecated_version = ""
