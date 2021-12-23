from OTLModel.Classes.AIMNaamObject import AIMNaamObject
from OTLModel.Datatypes.DtcDocument import DtcDocument
from OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLModel.Datatypes.KlWeegsensorMerk import KlWeegsensorMerk
from OTLModel.Datatypes.KlWeegsensorModelnaam import KlWeegsensorModelnaam
from OTLModel.Datatypes.KlWeegsensorType import KlWeegsensorType
from OTLModel.Datatypes.StringField import StringField


# Generated with OTLClassCreator
class Weegsensor(AIMNaamObject):
    """Registratie van de wieldruk van een voertuig (alle klassen). Dit wordt vertaald naar een massa."""

    typeURI = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Weegsensor"
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()
        self.meetrapport = DtcDocument()
        """Document met kalibratiegegevens (aantal rondes, types voertuigen,...)."""
        self.meetrapport.naam = "meetrapport"
        self.meetrapport.label = "meetrapport"
        self.meetrapport.uri = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Weegsensor.meetrapport"
        self.meetrapport.definition = "Document met kalibratiegegevens (aantal rondes, types voertuigen,...)."
        self.meetrapport.constraints = ""
        self.meetrapport.usagenote = "Bestanden van het type pdf."
        self.meetrapport.deprecated_version = ""

        self.merk = KeuzelijstField(naam="merk",
                                    label="merk",
                                    lijst=KlWeegsensorMerk(),
                                    uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Weegsensor.merk",
                                    definition="Het merk van de weegsensor.",
                                    constraints="",
                                    usagenote="",
                                    deprecated_version="")
        """Het merk van de weegsensor."""

        self.modelnaam = KeuzelijstField(naam="modelnaam",
                                         label="modelnaam",
                                         lijst=KlWeegsensorModelnaam(),
                                         uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Weegsensor.modelnaam",
                                         definition="De modelnaam van de weegsensor.",
                                         constraints="",
                                         usagenote="",
                                         deprecated_version="")
        """De modelnaam van de weegsensor."""

        self.rijstrook = StringField(naam="rijstrook",
                                     label="rijstrook",
                                     uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Weegsensor.rijstrook",
                                     definition="Beschrijft de rijstroken die door de weegsensor bewaakt worden.",
                                     constraints="",
                                     usagenote="",
                                     deprecated_version="")
        """Beschrijft de rijstroken die door de weegsensor bewaakt worden."""

        self.serienummer = StringField(naam="serienummer",
                                       label="serienummer",
                                       uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Weegsensor.serienummer",
                                       definition="Het unieke nummer waarmee het toestel door de fabrikant geïdentificeerd is.",
                                       constraints="",
                                       usagenote="",
                                       deprecated_version="")
        """Het unieke nummer waarmee het toestel door de fabrikant geïdentificeerd is."""

        self.type = KeuzelijstField(naam="type",
                                    label="type",
                                    lijst=KlWeegsensorType(),
                                    uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Weegsensor.type",
                                    definition="Het type van de weegsensor.",
                                    constraints="",
                                    usagenote="",
                                    deprecated_version="")
        """Het type van de weegsensor."""
