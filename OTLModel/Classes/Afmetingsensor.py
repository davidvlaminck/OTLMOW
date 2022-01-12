# coding=utf-8
from OTLModel.Classes.AIMNaamObject import AIMNaamObject
from OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLModel.Datatypes.KlAfmetingsensorMerk import KlAfmetingsensorMerk
from OTLModel.Datatypes.KlAfmetingsensorModelnaam import KlAfmetingsensorModelnaam
from OTLModel.Datatypes.KlAfmetingsensorType import KlAfmetingsensorType


# Generated with OTLClassCreator. To modify: extend, do not edit
class Afmetingsensor(AIMNaamObject):
    """Registratie van voertuigafmetingen."""

    typeURI = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Afmetingsensor"
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.merk = KeuzelijstField(naam="merk",
                                    label="merk",
                                    lijst=KlAfmetingsensorMerk(),
                                    objectUri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Afmetingsensor.merk",
                                    definition="Het merk van de afmetingsensor.",
                                    constraints="",
                                    usagenote="",
                                    deprecated_version="")
        """Het merk van de afmetingsensor."""

        self.modelnaam = KeuzelijstField(naam="modelnaam",
                                         label="modelnaam",
                                         lijst=KlAfmetingsensorModelnaam(),
                                         objectUri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Afmetingsensor.modelnaam",
                                         definition="De modelnaam van de afmetingsensor.",
                                         constraints="",
                                         usagenote="",
                                         deprecated_version="")
        """De modelnaam van de afmetingsensor."""

        self.type = KeuzelijstField(naam="type",
                                    label="type",
                                    lijst=KlAfmetingsensorType(),
                                    objectUri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Afmetingsensor.type",
                                    definition="Het type van de afmetingsensor.",
                                    constraints="",
                                    usagenote="",
                                    deprecated_version="")
        """Het type van de afmetingsensor."""
