from OTLModel.Classes.AIMObject import AIMObject
from OTLModel.Classes.Signalisatie import Signalisatie
from OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLModel.Datatypes.KlDivergentiepuntbebakeningselementType import KlDivergentiepuntbebakeningselementType
from OTLModel.Datatypes.KlFolieType import KlFolieType


# Generated with OTLClassCreator. To modify: extend, do not edit
class Divergentiepuntbebakeningselement(AIMObject, Signalisatie):
    """Een constructie met als doel de zichtbaarheid van het divergentiepunt te vergroten."""

    typeURI = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Divergentiepuntbebakeningselement"
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        AIMObject.__init__(self)
        Signalisatie.__init__(self)

        self.folietype = KeuzelijstField(naam="folietype",
                                         label="folietype",
                                         lijst=KlFolieType(),
                                         uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Divergentiepuntbebakeningselement.folietype",
                                         definition="Het type folie dat bevestigd is aan het Divergentiepuntbebakeningselement.",
                                         constraints="",
                                         usagenote="",
                                         deprecated_version="")
        """Het type folie dat bevestigd is aan het Divergentiepuntbebakeningselement."""

        self.type = KeuzelijstField(naam="type",
                                    label="type",
                                    lijst=KlDivergentiepuntbebakeningselementType(),
                                    uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Divergentiepuntbebakeningselement.type",
                                    definition="De vormen van het divergentiepuntbebakeningselement.",
                                    constraints="",
                                    usagenote="",
                                    deprecated_version="")
        """De vormen van het divergentiepuntbebakeningselement."""
