# coding=utf-8
from OTLModel.Classes.AIMNaamObject import AIMNaamObject
from OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLModel.Datatypes.KlHandbedieningType import KlHandbedieningType


# Generated with OTLClassCreator. To modify: extend, do not edit
class Handbediening(AIMNaamObject):
    """Module voor het bedienen met de hand van een techniek die zich in de kast bevindt waaraan de module bevestigd is om de sturing van de betrokken techniek tijdelijk over te nemen of uit te lezen."""

    typeURI = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Handbediening"
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.type = KeuzelijstField(naam="type",
                                    label="type handbediening",
                                    lijst=KlHandbedieningType(),
                                    objectUri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Handbediening.type",
                                    definition="Het gebruikte type voor handbediening langs de buitenkant van een kast voor sturing van systemen binnenin.",
                                    constraints="",
                                    usagenote="",
                                    deprecated_version="")
        """Het gebruikte type voor handbediening langs de buitenkant van een kast voor sturing van systemen binnenin."""
