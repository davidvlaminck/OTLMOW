# coding=utf-8
from OTLModel.Classes.Fundering import Fundering
from OTLModel.Datatypes.BooleanField import BooleanField
from OTLModel.Datatypes.DtuAfmetingGrondvlak import DtuAfmetingGrondvlak
from OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLModel.Datatypes.KlAlgMateriaal import KlAlgMateriaal
from OTLModel.Datatypes.KwantWrdInCentimeter import KwantWrdInCentimeter
from OTLModel.Datatypes.KwantWrdInKubiekeMeter import KwantWrdInKubiekeMeter


# Generated with OTLClassCreator. To modify: extend, do not edit
class Funderingsmassief(Fundering):
    """Een fundering waarop een klein(er) object geplaatst wordt of er (in principe) onlosmakelijk in vastgezet wordt (vb.: een paal/een steun, een kleine sokkel,...) Als het grotere constructie-elementen betreft (vb.: een pijler, een gebouw,...), moeten andere onderdelen van fundering gebruikt worden."""

    typeURI = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Funderingsmassief"
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.afmetingGrondvlak = DtuAfmetingGrondvlak()
        """De afmetingen van het grondvlak van de fundering volgens zijn vorm."""
        self.afmetingGrondvlak.naam = "afmetingGrondvlak"
        self.afmetingGrondvlak.label = "afmeting grondvlak"
        self.afmetingGrondvlak.objectUri = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Funderingsmassief.afmetingGrondvlak"
        self.afmetingGrondvlak.definition = "De afmetingen van het grondvlak van de fundering volgens zijn vorm."
        self.afmetingGrondvlak.constraints = ""
        self.afmetingGrondvlak.usagenote = ""
        self.afmetingGrondvlak.deprecated_version = ""

        self.funderingshoogte = KwantWrdInCentimeter()
        """De afstand tussen het laagste punt van de onderkant en hoogste punt van de bovenkant van de fundering."""
        self.funderingshoogte.naam = "funderingshoogte"
        self.funderingshoogte.label = "funderingshoogte"
        self.funderingshoogte.objectUri = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Funderingsmassief.funderingshoogte"
        self.funderingshoogte.definition = "De afstand tussen het laagste punt van de onderkant en hoogste punt van de bovenkant van de fundering."
        self.funderingshoogte.constraints = ""
        self.funderingshoogte.usagenote = ""
        self.funderingshoogte.deprecated_version = ""

        self.isPermanent = BooleanField(naam="isPermanent",
                                        label="is permanent",
                                        objectUri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Funderingsmassief.isPermanent",
                                        definition="Bepaalt of de fundering (en het gefundeerd object) blijvend is.",
                                        constraints="",
                                        usagenote="",
                                        deprecated_version="")
        """Bepaalt of de fundering (en het gefundeerd object) blijvend is."""

        self.isPrefab = BooleanField(naam="isPrefab",
                                     label="is prefab",
                                     objectUri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Funderingsmassief.isPrefab",
                                     definition="Bepaalt of de fundering ter plaatse gestort is of als geprefabriceerd element aangevoerd.",
                                     constraints="",
                                     usagenote="",
                                     deprecated_version="")
        """Bepaalt of de fundering ter plaatse gestort is of als geprefabriceerd element aangevoerd."""

        self.materiaal = KeuzelijstField(naam="materiaal",
                                         label="materiaal",
                                         lijst=KlAlgMateriaal(),
                                         objectUri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Funderingsmassief.materiaal",
                                         definition="De grondstof waaruit het funderingsmassief gemaakt is. ",
                                         constraints="",
                                         usagenote="",
                                         deprecated_version="")
        """De grondstof waaruit het funderingsmassief gemaakt is. """

        self.volume = KwantWrdInKubiekeMeter()
        """Het volume in kubieke meter van het funderingsmassief."""
        self.volume.naam = "volume"
        self.volume.label = "volume"
        self.volume.objectUri = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Funderingsmassief.volume"
        self.volume.definition = "Het volume in kubieke meter van het funderingsmassief."
        self.volume.constraints = ""
        self.volume.usagenote = ""
        self.volume.deprecated_version = ""
