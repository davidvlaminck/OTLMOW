from OTLModel.Classes.AIMObject import AIMObject
from OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLModel.Datatypes.KlVerwarmingselementMerk import KlVerwarmingselementMerk
from OTLModel.Datatypes.KlVerwarmingselementModelnaam import KlVerwarmingselementModelnaam
from OTLModel.Datatypes.KwantWrdInWatt import KwantWrdInWatt


# Generated with OTLClassCreator. To modify: extend, do not edit
class Verwarmingselement(AIMObject):
    """Toestel dat het verwarmingslint van warmte voorziet afhankelijk van de omgevingstemperatuur."""

    typeURI = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Verwarmingselement"
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.merk = KeuzelijstField(naam="merk",
                                    label="merk",
                                    lijst=KlVerwarmingselementMerk(),
                                    uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Verwarmingselement.merk",
                                    definition="Merk van het element volgens de fabrikant.",
                                    constraints="",
                                    usagenote="",
                                    deprecated_version="")
        """Merk van het element volgens de fabrikant."""

        self.modelnaam = KeuzelijstField(naam="modelnaam",
                                         label="modelnaam",
                                         lijst=KlVerwarmingselementModelnaam(),
                                         uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Verwarmingselement.modelnaam",
                                         definition="Modelnaam van het element volgens de fabrikant.",
                                         constraints="",
                                         usagenote="",
                                         deprecated_version="")
        """Modelnaam van het element volgens de fabrikant."""

        self.vermogen = KwantWrdInWatt()
        """Elektrisch vermogen nodig voor de correcte werking van het element."""
        self.vermogen.naam = "vermogen"
        self.vermogen.label = "vermogen"
        self.vermogen.uri = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Verwarmingselement.vermogen"
        self.vermogen.definition = "Elektrisch vermogen nodig voor de correcte werking van het element."
        self.vermogen.constraints = ""
        self.vermogen.usagenote = ""
        self.vermogen.deprecated_version = ""
