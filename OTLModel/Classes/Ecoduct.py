# coding=utf-8
from OTLModel.Classes.AIMObject import AIMObject
from OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLModel.Datatypes.KlEcoEcoductType import KlEcoEcoductType


# Generated with OTLClassCreator. To modify: extend, do not edit
class Ecoduct(AIMObject):
    """Ecoducten of natuurbruggen zorgen ervoor dat dieren veilig de weg kunnen oversteken."""

    typeURI = "https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Ecoduct"
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.type = KeuzelijstField(naam="type",
                                    label="type",
                                    lijst=KlEcoEcoductType(),
                                    objectUri="https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Ecoduct.type",
                                    definition="Het type van ecoduct, zoals bv ecoveloduct, bermbrug,….",
                                    constraints="",
                                    usagenote="",
                                    deprecated_version="")
        """Het type van ecoduct, zoals bv ecoveloduct, bermbrug,…."""
