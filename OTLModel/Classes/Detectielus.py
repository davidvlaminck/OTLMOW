# coding=utf-8
from abc import abstractmethod
from OTLModel.Classes.Detectie import Detectie
from OTLModel.Datatypes.DtcAfmetingBxlInM import DtcAfmetingBxlInM
from OTLModel.Datatypes.DtcTijdsduur import DtcTijdsduur


# Generated with OTLClassCreator. To modify: extend, do not edit
class Detectielus(Detectie):
    """Abstracte voor een detectielus. Een detectielus is een kabel onder het wegdek die in staat is om voertuigen te detecteren teneinde de verkeersregelaar aan te sturen. Selectieve lussen zijn in staat om gecodeerde informatie door te geven van prioritaire voertuigen, niet-selectieve lussen geven informatie door van alle voertuigen die het detectie gebied passeren."""

    typeURI = "https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Detectielus"
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    @abstractmethod
    def __init__(self):
        super().__init__()

        self.afmetingenBL = DtcAfmetingBxlInM()
        """Afmetingen breedte x lengte van de lus."""
        self.afmetingenBL.naam = "afmetingenBL"
        self.afmetingenBL.label = "afmetingen b l"
        self.afmetingenBL.objectUri = "https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Detectielus.afmetingenBL"
        self.afmetingenBL.definition = "Afmetingen breedte x lengte van de lus."
        self.afmetingenBL.constraints = ""
        self.afmetingenBL.usagenote = ""
        self.afmetingenBL.deprecated_version = ""

        self.bewakingstijd = DtcTijdsduur()
        """Wachttijd (in uren) waarna een alarm pas mag optreden."""
        self.bewakingstijd.naam = "bewakingstijd"
        self.bewakingstijd.label = "bewakingstijd"
        self.bewakingstijd.objectUri = "https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Detectielus.bewakingstijd"
        self.bewakingstijd.definition = "Wachttijd (in uren) waarna een alarm pas mag optreden."
        self.bewakingstijd.constraints = ""
        self.bewakingstijd.usagenote = ""
        self.bewakingstijd.deprecated_version = ""
