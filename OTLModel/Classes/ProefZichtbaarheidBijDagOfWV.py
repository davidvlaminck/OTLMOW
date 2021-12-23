from OTLModel.Classes.Proef import Proef
from OTLModel.Datatypes.DecimalFloatField import DecimalFloatField


# Generated with OTLClassCreator
class ProefZichtbaarheidBijDagOfWV(Proef):
    """Bepaling van de luminantiecoëfficiënt bij diffuse verlichting van een gemarkeerd oppervlak (Qd) bij daglicht of onder openbare verlichting."""

    typeURI = "https://wegenenverkeer.data.vlaanderen.be/ns/proefenmeting#ProefZichtbaarheidBijDagOfWV"
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()
        self.luminantiecoëfficiënt = DecimalFloatField(naam="luminantiecoëfficiënt",
                                                       label="luminantiecoëfficient",
                                                       uri="https://wegenenverkeer.data.vlaanderen.be/ns/proefenmeting#ProefZichtbaarheidBijDagOfWV.luminantiecoëfficiënt",
                                                       definition="De verhouding van de luminantie van het oppervlak in een gegeven richting en de verlichtingssterkte op het oppervlak.",
                                                       constraints="",
                                                       usagenote="uitgedrukt in mcd. m-2.lux-1",
                                                       deprecated_version="")
        """De verhouding van de luminantie van het oppervlak in een gegeven richting en de verlichtingssterkte op het oppervlak."""
