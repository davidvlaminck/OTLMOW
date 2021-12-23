from OTLModel.Classes.Straatmeubilair import Straatmeubilair
from OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLModel.Datatypes.KlOmegaElementMateriaal import KlOmegaElementMateriaal
from OTLModel.Datatypes.KlPlaatsingswijze import KlPlaatsingswijze


# Generated with OTLClassCreator
class OmegaElement(Straatmeubilair):
    """Een voetgangersafsluiting met als doel om de voetgangers te geleiden."""

    typeURI = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#OmegaElement"
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()
        self.materiaal = KeuzelijstField(naam="materiaal",
                                         label="materiaal",
                                         lijst=KlOmegaElementMateriaal(),
                                         uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#OmegaElement.materiaal",
                                         definition="De materie waaruit het omega-element bestaat.",
                                         constraints="",
                                         usagenote="",
                                         deprecated_version="")
        """De materie waaruit het omega-element bestaat."""

        self.plaatsingswijze = KeuzelijstField(naam="plaatsingswijze",
                                               label="plaatsingswijze",
                                               lijst=KlPlaatsingswijze(),
                                               uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#OmegaElement.plaatsingswijze",
                                               definition="Aanduiding of het omega-element eenvoudig wegneembaar is.",
                                               constraints="",
                                               usagenote="",
                                               deprecated_version="")
        """Aanduiding of het omega-element eenvoudig wegneembaar is."""
