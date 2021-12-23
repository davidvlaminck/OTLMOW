from OTLModel.Classes.AIMNaamObject import AIMNaamObject
from OTLModel.Datatypes.DtcDocument import DtcDocument


# Generated with OTLClassCreator
class Bel(AIMNaamObject):
    """Toestel dat door middel van een geluidssignaal de aandacht vestigt op een situatie."""

    typeURI = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bel"
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()
        self.technischeFiche = DtcDocument()
        """De technische fiche van een bel."""
        self.technischeFiche.naam = "technischeFiche"
        self.technischeFiche.label = "technische fiche"
        self.technischeFiche.uri = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bel.technischeFiche"
        self.technischeFiche.definition = "De technische fiche van een bel."
        self.technischeFiche.constraints = ""
        self.technischeFiche.usagenote = ""
        self.technischeFiche.deprecated_version = ""
