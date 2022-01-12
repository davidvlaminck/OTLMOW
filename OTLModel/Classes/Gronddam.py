# coding=utf-8
from OTLModel.Classes.AIMObject import AIMObject
from OTLModel.Datatypes.DecimalFloatField import DecimalFloatField
from OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLModel.Datatypes.KlHelling import KlHelling
from OTLModel.Datatypes.KwantWrdInMeter import KwantWrdInMeter


# Generated with OTLClassCreator. To modify: extend, do not edit
class Gronddam(AIMObject):
    """Gronddammen zijn trapeziumvormige constructies bestaande uit zand, grond of steenachtige materialen.
De onderkant van de gronddam wordt direct op het bestaand maaiveld aangebracht of op een vooraf aangebrachte grondverbetering.
Een gronddam kan volgende functies vervullen: geluidswering, geleiding van dieren, veiligheid en lichtwering."""

    typeURI = "https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Gronddam"
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.basisbreedte = KwantWrdInMeter()
        """De breedte van de basis van de gronddam in meter."""
        self.basisbreedte.naam = "basisbreedte"
        self.basisbreedte.label = "basisbreedte"
        self.basisbreedte.objectUri = "https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Gronddam.basisbreedte"
        self.basisbreedte.definition = "De breedte van de basis van de gronddam in meter."
        self.basisbreedte.constraints = ""
        self.basisbreedte.usagenote = ""
        self.basisbreedte.deprecated_version = ""

        self.gronddichtheid = DecimalFloatField(naam="gronddichtheid",
                                                label="gronddichtheid",
                                                objectUri="https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Gronddam.gronddichtheid",
                                                definition="De gronddichtheid van de gronddam.",
                                                constraints="",
                                                usagenote="",
                                                deprecated_version="")
        """De gronddichtheid van de gronddam."""

        self.hellingAchterzijde = KeuzelijstField(naam="hellingAchterzijde",
                                                  label="helling achterzijde",
                                                  lijst=KlHelling(),
                                                  objectUri="https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Gronddam.hellingAchterzijde",
                                                  definition="De hellingsgraad van de achterzijde gronddam in kwarten.",
                                                  constraints="",
                                                  usagenote="",
                                                  deprecated_version="")
        """De hellingsgraad van de achterzijde gronddam in kwarten."""

        self.hellingVoorzijde = KeuzelijstField(naam="hellingVoorzijde",
                                                label="helling voorzijde",
                                                lijst=KlHelling(),
                                                objectUri="https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Gronddam.hellingVoorzijde",
                                                definition="De hellingsgraad van de voorzijde van de gronddam in kwarten.",
                                                constraints="",
                                                usagenote="",
                                                deprecated_version="")
        """De hellingsgraad van de voorzijde van de gronddam in kwarten."""

        self.hoogte = KwantWrdInMeter()
        """De hoogte van de gronddam in meter."""
        self.hoogte.naam = "hoogte"
        self.hoogte.label = "hoogte"
        self.hoogte.objectUri = "https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Gronddam.hoogte"
        self.hoogte.definition = "De hoogte van de gronddam in meter."
        self.hoogte.constraints = ""
        self.hoogte.usagenote = ""
        self.hoogte.deprecated_version = ""

        self.kruinbreedte = KwantWrdInMeter()
        """De breedte van de kruin van de gronddam in meter."""
        self.kruinbreedte.naam = "kruinbreedte"
        self.kruinbreedte.label = "kruinbreedte"
        self.kruinbreedte.objectUri = "https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Gronddam.kruinbreedte"
        self.kruinbreedte.definition = "De breedte van de kruin van de gronddam in meter."
        self.kruinbreedte.constraints = ""
        self.kruinbreedte.usagenote = ""
        self.kruinbreedte.deprecated_version = ""
