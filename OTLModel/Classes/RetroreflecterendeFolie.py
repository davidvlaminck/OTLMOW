from OTLModel.Classes.AIMObject import AIMObject
from OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLModel.Datatypes.KlFolieType import KlFolieType


# Generated with OTLClassCreator
class RetroreflecterendeFolie(AIMObject):
    """Retroreflecterend bekledingsmateriaal, bijvoorbeeld van een divergentiepuntbebakeningselement, retroreflecterende koker, of het beeldvlak van een retroreflecterend verkeersbord."""

    typeURI = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#RetroreflecterendeFolie"
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()
        self.folietype = KeuzelijstField(naam="folietype",
                                         label="folietype",
                                         lijst=KlFolieType(),
                                         uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#RetroreflecterendeFolie.folietype",
                                         definition="Het type folie dat bevestigd is aan het retroreflecterend verkeersbord.",
                                         constraints="",
                                         usagenote="",
                                         deprecated_version="")
        """Het type folie dat bevestigd is aan het retroreflecterend verkeersbord."""
