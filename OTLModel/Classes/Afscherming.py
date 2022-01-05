from OTLModel.Classes.AIMObject import AIMObject
from OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLModel.Datatypes.KlEcoAfschermingtype import KlEcoAfschermingtype



# Generated with OTLClassCreator. To modify: extend, do not edit
class Afscherming(AIMObject):
    """Schermen of wallen op de rand van het ecoduct die ervoor zorgen dat dieren op de brug niet afgeschrikt worden door de lichten van voorbijrijdende voertuigen."""

    typeURI = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Afscherming"
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()
        self.type = KeuzelijstField(naam="type",
                                    label="type",
                                    lijst=KlEcoAfschermingtype(),
                                    uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Afscherming.type",
                                    definition="Het type van afscherming.",
                                    constraints="",
                                    usagenote="",
                                    deprecated_version="")
        """Het type van afscherming."""
