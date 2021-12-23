from OTLModel.Classes.AIMObject import AIMObject
from OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLModel.Datatypes.KlPutbekledingType import KlPutbekledingType
from OTLModel.Datatypes.KwantWrdInMillimeter import KwantWrdInMillimeter


# Generated with OTLClassCreator
class Putbekleding(AIMObject):
    """De soort afwerkingslaag waarmee een put bekleed is."""

    typeURI = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Putbekleding"
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()
        self.laagdikte = KwantWrdInMillimeter()
        """De dikte van de bekledingslaag in millimeter."""
        self.laagdikte.naam = "laagdikte"
        self.laagdikte.label = "laagdikte"
        self.laagdikte.uri = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Putbekleding.laagdikte"
        self.laagdikte.definition = "De dikte van de bekledingslaag in millimeter."
        self.laagdikte.constraints = ""
        self.laagdikte.usagenote = ""
        self.laagdikte.deprecated_version = ""

        self.type = KeuzelijstField(naam="type",
                                    label="type",
                                    lijst=KlPutbekledingType(),
                                    uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Putbekleding.type",
                                    definition="Bepaalt het type van de putbekleding.",
                                    constraints="",
                                    usagenote="",
                                    deprecated_version="")
        """Bepaalt het type van de putbekleding."""
