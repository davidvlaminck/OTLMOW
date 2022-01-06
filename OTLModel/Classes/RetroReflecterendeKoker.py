# coding=utf-8
from OTLModel.Classes.AIMObject import AIMObject
from OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLModel.Datatypes.KlRetroreflecterendeKokerFolieType import KlRetroreflecterendeKokerFolieType


# Generated with OTLClassCreator. To modify: extend, do not edit
class RetroReflecterendeKoker(AIMObject):
    """Een kunststoffen koker bevestigd rond een steun om de zichtbaarheid van verkeerseilanden te verhogen."""

    typeURI = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#RetroReflecterendeKoker"
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.folieType = KeuzelijstField(naam="folieType",
                                         label="folie type",
                                         lijst=KlRetroreflecterendeKokerFolieType(),
                                         uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#RetroReflecterendeKoker.folieType",
                                         definition="Een keuzelijst het folietype van reflecterende koker te bepalen.",
                                         constraints="",
                                         usagenote="",
                                         deprecated_version="")
        """Een keuzelijst het folietype van reflecterende koker te bepalen."""
