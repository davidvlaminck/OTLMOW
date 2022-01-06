from OTLModel.Classes.AIMNaamObject import AIMNaamObject
from OTLModel.Datatypes.DtcDocument import DtcDocument
from OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLModel.Datatypes.KlCodeklavierMerk import KlCodeklavierMerk
from OTLModel.Datatypes.KlCodeklavierModelnaam import KlCodeklavierModelnaam
from OTLModel.Datatypes.KlCodeklavierWerking import KlCodeklavierWerking


# Generated with OTLClassCreator. To modify: extend, do not edit
class Codeklavier(AIMNaamObject):
    """Toestel voor het aansturen van een asset op basis van ingetoetste codes."""

    typeURI = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Codeklavier"
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.merk = KeuzelijstField(naam="merk",
                                    label="merk",
                                    lijst=KlCodeklavierMerk(),
                                    uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Codeklavier.merk",
                                    definition="Het merk van het codeklavier.",
                                    constraints="",
                                    usagenote="",
                                    deprecated_version="")
        """Het merk van het codeklavier."""

        self.modelnaam = KeuzelijstField(naam="modelnaam",
                                         label="modelnaam",
                                         lijst=KlCodeklavierModelnaam(),
                                         uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Codeklavier.modelnaam",
                                         definition="De modelnaam van het codeklavier.",
                                         constraints="",
                                         usagenote="",
                                         deprecated_version="")
        """De modelnaam van het codeklavier."""

        self.technischeFiche = DtcDocument()
        """De technische fiche van het codeklavier."""
        self.technischeFiche.naam = "technischeFiche"
        self.technischeFiche.label = "technische fiche"
        self.technischeFiche.uri = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Codeklavier.technischeFiche"
        self.technischeFiche.definition = "De technische fiche van het codeklavier."
        self.technischeFiche.constraints = ""
        self.technischeFiche.usagenote = ""
        self.technischeFiche.deprecated_version = ""

        self.werking = KeuzelijstField(naam="werking",
                                       label="werking",
                                       lijst=KlCodeklavierWerking(),
                                       uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Codeklavier.werking",
                                       definition="Indeling van het toestel volgens de manier waarop de gebruiker de aansturing doet.",
                                       constraints="",
                                       usagenote="",
                                       deprecated_version="")
        """Indeling van het toestel volgens de manier waarop de gebruiker de aansturing doet."""
