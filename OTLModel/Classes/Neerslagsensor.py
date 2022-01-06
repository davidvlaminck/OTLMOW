from OTLModel.Classes.AIMNaamObject import AIMNaamObject
from OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLModel.Datatypes.KlNeerslagsensorMerk import KlNeerslagsensorMerk
from OTLModel.Datatypes.KlNeerslagsensorModelnaam import KlNeerslagsensorModelnaam
from OTLModel.Datatypes.KlNeerslagsensorType import KlNeerslagsensorType


# Generated with OTLClassCreator. To modify: extend, do not edit
class Neerslagsensor(AIMNaamObject):
    """Detectie van neerslag(hoeveelheid/intensiteit)."""

    typeURI = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Neerslagsensor"
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.merk = KeuzelijstField(naam="merk",
                                    label="merk",
                                    lijst=KlNeerslagsensorMerk(),
                                    uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Neerslagsensor.merk",
                                    definition="Het merk van de neerslagsensor.",
                                    constraints="",
                                    usagenote="",
                                    deprecated_version="")
        """Het merk van de neerslagsensor."""

        self.modelnaam = KeuzelijstField(naam="modelnaam",
                                         label="modelnaam",
                                         lijst=KlNeerslagsensorModelnaam(),
                                         uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Neerslagsensor.modelnaam",
                                         definition="De modelnaam van de neerslagsensor.",
                                         constraints="",
                                         usagenote="",
                                         deprecated_version="")
        """De modelnaam van de neerslagsensor."""

        self.type = KeuzelijstField(naam="type",
                                    label="type",
                                    lijst=KlNeerslagsensorType(),
                                    uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Neerslagsensor.type",
                                    definition="Het type van de neerslagsensor.",
                                    constraints="",
                                    usagenote="",
                                    deprecated_version="")
        """Het type van de neerslagsensor."""
