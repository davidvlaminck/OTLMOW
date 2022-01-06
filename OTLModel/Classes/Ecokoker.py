from OTLModel.Classes.AIMObject import AIMObject
from OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLModel.Datatypes.KlEcoEcokokerType import KlEcoEcokokerType


# Generated with OTLClassCreator. To modify: extend, do not edit
class Ecokoker(AIMObject):
    """Een kleine ecotunnel of ecokoker is een doorgang voor dieren onder een weg of spoorweg."""

    typeURI = "https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Ecokoker"
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.type = KeuzelijstField(naam="type",
                                    label="type",
                                    lijst=KlEcoEcokokerType(),
                                    uri="https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Ecokoker.type",
                                    definition="Het type van ecokoker zoals bv. amfibieënkoker, ….",
                                    constraints="",
                                    usagenote="",
                                    deprecated_version="")
        """Het type van ecokoker zoals bv. amfibieënkoker, …."""
