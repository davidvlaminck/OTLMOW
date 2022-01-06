# coding=utf-8
from OTLModel.Classes.AIMNaamObject import AIMNaamObject
from OTLModel.Datatypes.BooleanField import BooleanField
from OTLModel.Datatypes.DtcAfmetingDiameterInCm import DtcAfmetingDiameterInCm
from OTLModel.Datatypes.DtuAfmetingGrondvlak import DtuAfmetingGrondvlak
from OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLModel.Datatypes.KlAlgMateriaal import KlAlgMateriaal
from OTLModel.Datatypes.KwantWrdInCentimeter import KwantWrdInCentimeter


# Generated with OTLClassCreator. To modify: extend, do not edit
class Sokkel(AIMNaamObject):
    """Onderdeel dat zich voornamelijk voornamelijk boven het maaiveld bevindt en als doel heeft het object dat er op rust te verhogen, het object te omhullen ter bescherming of de ondergrond te nivelleren. Afhankelijk van de grootte van dat object en van de omvang van de sokkel, kan die ook zorgen voor nodige stabiliteit zoals een fundering."""

    typeURI = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Sokkel"
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.afmetingGrondvlak = DtuAfmetingGrondvlak()
        """De afmeting van het grondvlak van de sokkel volgens zijn vorm."""
        self.afmetingGrondvlak.naam = "afmetingGrondvlak"
        self.afmetingGrondvlak.label = "afmeting grondvlak"
        self.afmetingGrondvlak.uri = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Sokkel.afmetingGrondvlak"
        self.afmetingGrondvlak.definition = "De afmeting van het grondvlak van de sokkel volgens zijn vorm."
        self.afmetingGrondvlak.constraints = ""
        self.afmetingGrondvlak.usagenote = ""
        self.afmetingGrondvlak.deprecated_version = ""

        self.heeftMaaibescherming = BooleanField(naam="heeftMaaibescherming",
                                                 label="heeft maaibescherming",
                                                 uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Sokkel.heeftMaaibescherming",
                                                 definition="Geeft aan of de sokkel (en daarmee het object dat er bovenop geplaatst is) beschermd is tegen schade als gevolg van het maaien van omliggende begroeiing.",
                                                 constraints="",
                                                 usagenote="",
                                                 deprecated_version="")
        """Geeft aan of de sokkel (en daarmee het object dat er bovenop geplaatst is) beschermd is tegen schade als gevolg van het maaien van omliggende begroeiing."""

        self.hoogteBovenMaaiveld = KwantWrdInCentimeter()
        """Hoogte in centimeters van het hoogste punt van de sokkel gemeten vanaf het maaiveld."""
        self.hoogteBovenMaaiveld.naam = "hoogteBovenMaaiveld"
        self.hoogteBovenMaaiveld.label = "hoogte boven het maaiveld"
        self.hoogteBovenMaaiveld.uri = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Sokkel.hoogteBovenMaaiveld"
        self.hoogteBovenMaaiveld.definition = "Hoogte in centimeters van het hoogste punt van de sokkel gemeten vanaf het maaiveld."
        self.hoogteBovenMaaiveld.constraints = ""
        self.hoogteBovenMaaiveld.usagenote = ""
        self.hoogteBovenMaaiveld.deprecated_version = ""

        self.materiaal = KeuzelijstField(naam="materiaal",
                                         label="materiaal",
                                         lijst=KlAlgMateriaal(),
                                         uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Sokkel.materiaal",
                                         definition="De grondstof waaruit de sokkel (voornamelijk) vervaardigd is.",
                                         constraints="",
                                         usagenote="",
                                         deprecated_version="")
        """De grondstof waaruit de sokkel (voornamelijk) vervaardigd is."""

        self.sokkelhoogte = KwantWrdInCentimeter()
        """De totale hoogte van de sokkel wanneer die rechtop staat."""
        self.sokkelhoogte.naam = "sokkelhoogte"
        self.sokkelhoogte.label = "hoogte van de sokkel"
        self.sokkelhoogte.uri = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Sokkel.sokkelhoogte"
        self.sokkelhoogte.definition = "De totale hoogte van de sokkel wanneer die rechtop staat."
        self.sokkelhoogte.constraints = ""
        self.sokkelhoogte.usagenote = ""
        self.sokkelhoogte.deprecated_version = ""
