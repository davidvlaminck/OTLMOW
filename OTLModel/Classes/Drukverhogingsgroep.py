# coding=utf-8
from OTLModel.Classes.Brandvoorziening import Brandvoorziening
from OTLModel.Datatypes.KwantWrdInBar import KwantWrdInBar
from OTLModel.Datatypes.KwantWrdInKiloWatt import KwantWrdInKiloWatt


# Generated with OTLClassCreator. To modify: extend, do not edit
class Drukverhogingsgroep(Brandvoorziening):
    """Onderdeel dat de druk van het aangevoerde water regelt."""

    typeURI = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Drukverhogingsgroep"
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.inkomendeDruk = KwantWrdInBar()
        """Verwachte inkomende druk van het water bij de groep."""
        self.inkomendeDruk.naam = "inkomendeDruk"
        self.inkomendeDruk.label = "inkomende druk"
        self.inkomendeDruk.uri = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Drukverhogingsgroep.inkomendeDruk"
        self.inkomendeDruk.definition = "Verwachte inkomende druk van het water bij de groep."
        self.inkomendeDruk.constraints = ""
        self.inkomendeDruk.usagenote = ""
        self.inkomendeDruk.deprecated_version = ""

        self.uitgaandeDruk = KwantWrdInBar()
        """Verwachte uitgaande druk van het water na regeling door de groep."""
        self.uitgaandeDruk.naam = "uitgaandeDruk"
        self.uitgaandeDruk.label = "uitgaande druk"
        self.uitgaandeDruk.uri = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Drukverhogingsgroep.uitgaandeDruk"
        self.uitgaandeDruk.definition = "Verwachte uitgaande druk van het water na regeling door de groep."
        self.uitgaandeDruk.constraints = ""
        self.uitgaandeDruk.usagenote = ""
        self.uitgaandeDruk.deprecated_version = ""

        self.vermogen = KwantWrdInKiloWatt()
        """Elektrische vermogen vereist voor de goede werking van de groep."""
        self.vermogen.naam = "vermogen"
        self.vermogen.label = "vermogen"
        self.vermogen.uri = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Drukverhogingsgroep.vermogen"
        self.vermogen.definition = "Elektrische vermogen vereist voor de goede werking van de groep."
        self.vermogen.constraints = ""
        self.vermogen.usagenote = ""
        self.vermogen.deprecated_version = ""
