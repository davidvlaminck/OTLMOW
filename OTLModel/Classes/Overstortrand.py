# coding=utf-8
from OTLModel.Classes.AIMObject import AIMObject
from OTLModel.Datatypes.DtcDocument import DtcDocument
from OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLModel.Datatypes.KlOverstortrandMateriaal import KlOverstortrandMateriaal
from OTLModel.Datatypes.KlVariabelDeelType import KlVariabelDeelType
from OTLModel.Datatypes.KwantWrdInMillimeter import KwantWrdInMillimeter


# Generated with OTLClassCreator. To modify: extend, do not edit
class Overstortrand(AIMObject):
    """Een overstortrand heeft als doel het afvoeren van (pieken in) overtollig rioolwater vanuit de gemengde riolering naar het oppervlaktewater."""

    typeURI = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Overstortrand"
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.breedte = KwantWrdInMillimeter()
        """De afstand tussen de uiterste zijden van de overstortrand in millimeter."""
        self.breedte.naam = "breedte"
        self.breedte.label = "breedte"
        self.breedte.uri = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Overstortrand.breedte"
        self.breedte.definition = "De afstand tussen de uiterste zijden van de overstortrand in millimeter."
        self.breedte.constraints = ""
        self.breedte.usagenote = ""
        self.breedte.deprecated_version = ""

        self.hoogte = KwantWrdInMillimeter()
        """De afstand tussen de vaste drempel en het hoogste punt van de overstortrand in millimeter."""
        self.hoogte.naam = "hoogte"
        self.hoogte.label = "hoogte"
        self.hoogte.uri = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Overstortrand.hoogte"
        self.hoogte.definition = "De afstand tussen de vaste drempel en het hoogste punt van de overstortrand in millimeter."
        self.hoogte.constraints = ""
        self.hoogte.usagenote = ""
        self.hoogte.deprecated_version = ""

        self.materiaal = KeuzelijstField(naam="materiaal",
                                         label="materiaal",
                                         lijst=KlOverstortrandMateriaal(),
                                         uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Overstortrand.materiaal",
                                         definition="Het materiaal waaruit de overstortrand vervaardigd is.",
                                         constraints="",
                                         usagenote="",
                                         deprecated_version="")
        """Het materiaal waaruit de overstortrand vervaardigd is."""

        self.technischeFiche = DtcDocument()
        """De technische fiche van de de overstortrand."""
        self.technischeFiche.naam = "technischeFiche"
        self.technischeFiche.label = "technische fiche"
        self.technischeFiche.uri = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Overstortrand.technischeFiche"
        self.technischeFiche.definition = "De technische fiche van de de overstortrand."
        self.technischeFiche.constraints = ""
        self.technischeFiche.usagenote = ""
        self.technischeFiche.deprecated_version = ""

        self.variabelDeelType = KeuzelijstField(naam="variabelDeelType",
                                                label="variabel deel type",
                                                lijst=KlVariabelDeelType(),
                                                uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Overstortrand.variabelDeelType",
                                                definition="Bepaalt het type van het variabel deel van de overstortrand.",
                                                constraints="",
                                                usagenote="",
                                                deprecated_version="")
        """Bepaalt het type van het variabel deel van de overstortrand."""

        self.wanddikte = KwantWrdInMillimeter()
        """De wanddikte van de overstortrand in millimeter."""
        self.wanddikte.naam = "wanddikte"
        self.wanddikte.label = "wanddikte"
        self.wanddikte.uri = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Overstortrand.wanddikte"
        self.wanddikte.definition = "De wanddikte van de overstortrand in millimeter."
        self.wanddikte.constraints = ""
        self.wanddikte.usagenote = ""
        self.wanddikte.deprecated_version = ""
