# coding=utf-8
from OTLModel.Classes.AIMNaamObject import AIMNaamObject
from OTLModel.Datatypes.DteIPv4Adres import DteIPv4Adres
from OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLModel.Datatypes.KlNetwerkMerk import KlNetwerkMerk
from OTLModel.Datatypes.KlNetwerkelemGebruik import KlNetwerkelemGebruik
from OTLModel.Datatypes.KlNetwerkelemModelnaam import KlNetwerkelemModelnaam
from OTLModel.Datatypes.StringField import StringField


# Generated with OTLClassCreator. To modify: extend, do not edit
class Netwerkelement(AIMNaamObject):
    """Toestel,onderdeel van het netwerk,waarop netwerkverbindingen kunnen aangelegd worden."""

    typeURI = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Netwerkelement"
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.beschrijvingFabrikant = StringField(naam="beschrijvingFabrikant",
                                                 label="beschrijving fabrikant",
                                                 objectUri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Netwerkelement.beschrijvingFabrikant",
                                                 definition="Bijkomende specificaties over het apparaat of onderdeel type van de fabrikant.",
                                                 constraints="",
                                                 usagenote="",
                                                 deprecated_version="")
        """Bijkomende specificaties over het apparaat of onderdeel type van de fabrikant."""

        self.gebruik = KeuzelijstField(naam="gebruik",
                                       label="gebruik",
                                       lijst=KlNetwerkelemGebruik(),
                                       objectUri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Netwerkelement.gebruik",
                                       definition="Toestel, onderdeel van het netwerk, waarop netwerkverbindingen kunnen aangelegd worden.",
                                       constraints="",
                                       usagenote="",
                                       deprecated_version="")
        """Toestel, onderdeel van het netwerk, waarop netwerkverbindingen kunnen aangelegd worden."""

        self.ipAddressBeheer = DteIPv4Adres()
        """IP adres van het toestel."""
        self.ipAddressBeheer.naam = "ipAddressBeheer"
        self.ipAddressBeheer.label = "IP address beheer"
        self.ipAddressBeheer.objectUri = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Netwerkelement.ipAddressBeheer"
        self.ipAddressBeheer.definition = "IP adres van het toestel."
        self.ipAddressBeheer.constraints = ""
        self.ipAddressBeheer.usagenote = ""
        self.ipAddressBeheer.deprecated_version = ""

        self.ipAddressMask = DteIPv4Adres()
        """IP adres mask van het toestel."""
        self.ipAddressMask.naam = "ipAddressMask"
        self.ipAddressMask.label = "IP address mask"
        self.ipAddressMask.objectUri = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Netwerkelement.ipAddressMask"
        self.ipAddressMask.definition = "IP adres mask van het toestel."
        self.ipAddressMask.constraints = ""
        self.ipAddressMask.usagenote = ""
        self.ipAddressMask.deprecated_version = ""

        self.ipGateway = DteIPv4Adres()
        """IP adres van gateway."""
        self.ipGateway.naam = "ipGateway"
        self.ipGateway.label = "IP gateway"
        self.ipGateway.objectUri = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Netwerkelement.ipGateway"
        self.ipGateway.definition = "IP adres van gateway."
        self.ipGateway.constraints = ""
        self.ipGateway.usagenote = ""
        self.ipGateway.deprecated_version = ""

        self.merk = KeuzelijstField(naam="merk",
                                    label="merk",
                                    lijst=KlNetwerkMerk(),
                                    objectUri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Netwerkelement.merk",
                                    definition="Merk waarmee de fabrikant het netwerkelement identificeert.",
                                    constraints="",
                                    usagenote="",
                                    deprecated_version="")
        """Merk waarmee de fabrikant het netwerkelement identificeert."""

        self.modelnaam = KeuzelijstField(naam="modelnaam",
                                         label="modelnaam",
                                         lijst=KlNetwerkelemModelnaam(),
                                         objectUri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Netwerkelement.modelnaam",
                                         definition="Modelnaam waarmee de fabrikant dit type toestel identificeert.",
                                         constraints="",
                                         usagenote="",
                                         deprecated_version="")
        """Modelnaam waarmee de fabrikant dit type toestel identificeert."""

        self.nSAPAddress = StringField(naam="nSAPAddress",
                                       label="NSAP-address",
                                       objectUri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Netwerkelement.nSAPAddress",
                                       definition="Netwerkadres van deze component.",
                                       constraints="",
                                       usagenote="",
                                       deprecated_version="")
        """Netwerkadres van deze component."""

        self.serienummer = StringField(naam="serienummer",
                                       label="serienummer",
                                       objectUri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Netwerkelement.serienummer",
                                       definition="Unieke identificatiecode van het toestel, toegekend door de fabrikant.",
                                       constraints="",
                                       usagenote="",
                                       deprecated_version="")
        """Unieke identificatiecode van het toestel, toegekend door de fabrikant."""

        self.softwareVersie = StringField(naam="softwareVersie",
                                          label="software versie",
                                          objectUri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Netwerkelement.softwareVersie",
                                          definition="Identificatie van de softwareversie die op dit apparaat of onderdeel geladen is. Dit kan ook de firmwareversie zijn.",
                                          constraints="",
                                          usagenote="",
                                          deprecated_version="")
        """Identificatie van de softwareversie die op dit apparaat of onderdeel geladen is. Dit kan ook de firmwareversie zijn."""
