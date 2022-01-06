from OTLModel.Classes.Inloopbehuizing import Inloopbehuizing
from OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLModel.Datatypes.KlCabineAardingsstelsel import KlCabineAardingsstelsel
from OTLModel.Datatypes.KlCabineStandaardtype import KlCabineStandaardtype
from OTLModel.Datatypes.KwantWrdInMeter import KwantWrdInMeter


# Generated with OTLClassCreator. To modify: extend, do not edit
class Cabine(Inloopbehuizing):
    """Een behuizing voornamelijk bestemd voor het beschermen van elektromechanische technieken waarin het omwille van de grootte en toegankelijkheid mogelijk is om rond te lopen."""

    typeURI = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Cabine"
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.aardingsstelsel = KeuzelijstField(naam="aardingsstelsel",
                                               label="aardingsstelsel",
                                               lijst=KlCabineAardingsstelsel(),
                                               uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Cabine.aardingsstelsel",
                                               definition="Keuze tussen verschillende types voor het gebruikte aardingsstelsel.",
                                               constraints="",
                                               usagenote="",
                                               deprecated_version="")
        """Keuze tussen verschillende types voor het gebruikte aardingsstelsel."""

        self.kelderdiepte = KwantWrdInMeter()
        """Binnenhoogte in meter van de kabelkelder onder de cabine."""
        self.kelderdiepte.naam = "kelderdiepte"
        self.kelderdiepte.label = "kelderdiepte"
        self.kelderdiepte.uri = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Cabine.kelderdiepte"
        self.kelderdiepte.definition = "Binnenhoogte in meter van de kabelkelder onder de cabine."
        self.kelderdiepte.constraints = ""
        self.kelderdiepte.usagenote = ""
        self.kelderdiepte.deprecated_version = ""

        self.standaardtype = KeuzelijstField(naam="standaardtype",
                                             label="standaardtype",
                                             lijst=KlCabineStandaardtype(),
                                             uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Cabine.standaardtype",
                                             definition="Het type van de cabine volgens de gangbare standaarden.",
                                             constraints="",
                                             usagenote="",
                                             deprecated_version="")
        """Het type van de cabine volgens de gangbare standaarden."""
