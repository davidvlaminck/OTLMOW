from OTLModel.Classes.AIMNaamObject import AIMNaamObject
from OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLModel.Datatypes.KlNetwerkMerk import KlNetwerkMerk
from OTLModel.Datatypes.KlNetwerkTechnologie import KlNetwerkTechnologie
from OTLModel.Datatypes.KlNetwerkkaartModelnaam import KlNetwerkkaartModelnaam
from OTLModel.Datatypes.StringField import StringField


# Generated with OTLClassCreator. To modify: extend, do not edit
class Netwerkkaart(AIMNaamObject):
    """Component van een NetwerkElement om specifieke verbindingen te leggen."""

    typeURI = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Netwerkkaart"
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.beschrijvingFabrikant = StringField(naam="beschrijvingFabrikant",
                                                 label="beschrijving fabrikant",
                                                 uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Netwerkkaart.beschrijvingFabrikant",
                                                 definition="Bijkomende specificaties over het apparaat of onderdeel type van de fabrikant.",
                                                 constraints="",
                                                 usagenote="",
                                                 deprecated_version="")
        """Bijkomende specificaties over het apparaat of onderdeel type van de fabrikant."""

        self.merk = KeuzelijstField(naam="merk",
                                    label="merk",
                                    lijst=KlNetwerkMerk(),
                                    uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Netwerkkaart.merk",
                                    definition="Merk waarmee de fabrikant de netwerkkaart identificeert.",
                                    constraints="",
                                    usagenote="",
                                    deprecated_version="")
        """Merk waarmee de fabrikant de netwerkkaart identificeert."""

        self.modelnaam = KeuzelijstField(naam="modelnaam",
                                         label="modelnaam",
                                         lijst=KlNetwerkkaartModelnaam(),
                                         uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Netwerkkaart.modelnaam",
                                         definition="Modelnaam waarmee de fabrikant dit type toestel identificeert.",
                                         constraints="",
                                         usagenote="",
                                         deprecated_version="")
        """Modelnaam waarmee de fabrikant dit type toestel identificeert."""

        self.serienummer = StringField(naam="serienummer",
                                       label="serienummer",
                                       uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Netwerkkaart.serienummer",
                                       definition="Unieke identificatiecode van het toestel, toegekend door de fabrikant.",
                                       constraints="",
                                       usagenote="",
                                       deprecated_version="")
        """Unieke identificatiecode van het toestel, toegekend door de fabrikant."""

        self.softwareVersie = StringField(naam="softwareVersie",
                                          label="software versie",
                                          uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Netwerkkaart.softwareVersie",
                                          definition="Identificatie van de softwareversie die op dit apparaat of onderdeel geladen is. Dit kan ook een firmwareversie zijn.",
                                          constraints="",
                                          usagenote="",
                                          deprecated_version="")
        """Identificatie van de softwareversie die op dit apparaat of onderdeel geladen is. Dit kan ook een firmwareversie zijn."""

        self.technologie = KeuzelijstField(naam="technologie",
                                           label="technologie",
                                           lijst=KlNetwerkTechnologie(),
                                           uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Netwerkkaart.technologie",
                                           definition="Intern gebruikte netwerk protocol.",
                                           constraints="",
                                           usagenote="",
                                           deprecated_version="")
        """Intern gebruikte netwerk protocol."""
