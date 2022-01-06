# coding=utf-8
from OTLModel.Classes.AIMNaamObject import AIMNaamObject
from OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLModel.Datatypes.KlWIMDataloggerMerk import KlWIMDataloggerMerk
from OTLModel.Datatypes.KlWIMDataloggerModelnaam import KlWIMDataloggerModelnaam


# Generated with OTLClassCreator. To modify: extend, do not edit
class WIMDatalogger(AIMNaamObject):
    """Lokale verwerkingseenheid voor aggregatie weeggegevens."""

    typeURI = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#WIMDatalogger"
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.merk = KeuzelijstField(naam="merk",
                                    label="merk",
                                    lijst=KlWIMDataloggerMerk(),
                                    uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#WIMDatalogger.merk",
                                    definition="Het merk van de WIM datalogger.",
                                    constraints="",
                                    usagenote="",
                                    deprecated_version="")
        """Het merk van de WIM datalogger."""

        self.modelnaam = KeuzelijstField(naam="modelnaam",
                                         label="modelnaam",
                                         lijst=KlWIMDataloggerModelnaam(),
                                         uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#WIMDatalogger.modelnaam",
                                         definition="De modelnaam van de WIM datalogger.",
                                         constraints="",
                                         usagenote="",
                                         deprecated_version="")
        """De modelnaam van de WIM datalogger."""
