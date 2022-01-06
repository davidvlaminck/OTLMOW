from OTLModel.Classes.AIMObject import AIMObject
from OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLModel.Datatypes.KlStopcontactAantalPolen import KlStopcontactAantalPolen
from OTLModel.Datatypes.KwantWrdInAmpere import KwantWrdInAmpere
from OTLModel.Datatypes.KwantWrdInVolt import KwantWrdInVolt


# Generated with OTLClassCreator. To modify: extend, do not edit
class Stopcontact(AIMObject):
    """Een aansluitpunt op het elektrisch net voor afname van elektrische energie met behulp van een stekker."""

    typeURI = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Stopcontact"
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.aantalPolen = KeuzelijstField(naam="aantalPolen",
                                           label="aantal polen",
                                           lijst=KlStopcontactAantalPolen(),
                                           uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Stopcontact.aantalPolen",
                                           definition="Typering van het stopcontact volgens het aantal polen op basis van een keuzelijst.",
                                           constraints="",
                                           usagenote="",
                                           deprecated_version="")
        """Typering van het stopcontact volgens het aantal polen op basis van een keuzelijst."""

        self.spanning = KwantWrdInVolt()
        """De voorziene spanning voor het stopcontact."""
        self.spanning.naam = "spanning"
        self.spanning.label = "spanning"
        self.spanning.uri = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Stopcontact.spanning"
        self.spanning.definition = "De voorziene spanning voor het stopcontact."
        self.spanning.constraints = ""
        self.spanning.usagenote = ""
        self.spanning.deprecated_version = ""

        self.stroomsterkte = KwantWrdInAmpere()
        """Maximale stroomsterkte van het stopcontact uitgedrukt in ampère."""
        self.stroomsterkte.naam = "stroomsterkte"
        self.stroomsterkte.label = "stroomsterkte"
        self.stroomsterkte.uri = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Stopcontact.stroomsterkte"
        self.stroomsterkte.definition = "Maximale stroomsterkte van het stopcontact uitgedrukt in ampère."
        self.stroomsterkte.constraints = ""
        self.stroomsterkte.usagenote = ""
        self.stroomsterkte.deprecated_version = ""
