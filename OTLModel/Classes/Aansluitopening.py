# coding=utf-8
from OTLModel.Classes.LinkendElement import LinkendElement
from OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLModel.Datatypes.KlRioleringVorm import KlRioleringVorm
from OTLModel.Datatypes.KwantWrdInMeterTAW import KwantWrdInMeterTAW
from OTLModel.Datatypes.KwantWrdInMillimeter import KwantWrdInMillimeter


# Generated with OTLClassCreator. To modify: extend, do not edit
class Aansluitopening(LinkendElement):
    """Een kleine doorgang in de wand tussen twee kamers, of aan het begin van een leiding."""

    typeURI = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Aansluitopening"
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.breedte = KwantWrdInMillimeter()
        """De afstand tussen de uiterste zijden van de aansluitopening in millimeter."""
        self.breedte.naam = "breedte"
        self.breedte.label = "breedte"
        self.breedte.objectUri = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Aansluitopening.breedte"
        self.breedte.definition = "De afstand tussen de uiterste zijden van de aansluitopening in millimeter."
        self.breedte.constraints = ""
        self.breedte.usagenote = ""
        self.breedte.deprecated_version = ""

        self.hoogte = KwantWrdInMillimeter()
        """De afstand tussen het hoogste en laagste punt van de aansluitopening in millimeter."""
        self.hoogte.naam = "hoogte"
        self.hoogte.label = "hoogte"
        self.hoogte.objectUri = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Aansluitopening.hoogte"
        self.hoogte.definition = "De afstand tussen het hoogste en laagste punt van de aansluitopening in millimeter."
        self.hoogte.constraints = ""
        self.hoogte.usagenote = ""
        self.hoogte.deprecated_version = ""

        self.peil = KwantWrdInMeterTAW()
        """BOK peil in meter-TAW van de knijpopening."""
        self.peil.naam = "peil"
        self.peil.label = "peil"
        self.peil.objectUri = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Aansluitopening.peil"
        self.peil.definition = "BOK peil in meter-TAW van de knijpopening."
        self.peil.constraints = ""
        self.peil.usagenote = ""
        self.peil.deprecated_version = ""

        self.vorm = KeuzelijstField(naam="vorm",
                                    label="vorm",
                                    lijst=KlRioleringVorm(),
                                    objectUri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Aansluitopening.vorm",
                                    definition="De vorm van de aansluitopening.",
                                    constraints="",
                                    usagenote="",
                                    deprecated_version="")
        """De vorm van de aansluitopening."""
