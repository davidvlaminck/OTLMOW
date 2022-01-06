from abc import abstractmethod
from OTLModel.Classes.Kast import Kast
from OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLModel.Datatypes.KlAlgIngressProtectionCode import KlAlgIngressProtectionCode
from OTLModel.Datatypes.KlBuitenkastVerfraaid import KlBuitenkastVerfraaid
from OTLModel.Datatypes.KwantWrdInJaar import KwantWrdInJaar


# Generated with OTLClassCreator. To modify: extend, do not edit
class Buitenkast(Kast):
    """Abstracte voor kasten die typisch buiten staan en daarom bestand moeten zijn tegen de elementen en verfraaiing kunnen krijgen."""

    typeURI = "https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Buitenkast"
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    @abstractmethod
    def __init__(self):
        super().__init__()

        self.ipKlasse = KeuzelijstField(naam="ipKlasse",
                                        label="ingress protection klasse",
                                        lijst=KlAlgIngressProtectionCode(),
                                        uri="https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Buitenkast.ipKlasse",
                                        definition="De IP-codering als een aanduiding voor de mate van beveiliging van de constructie van elektrische of elektronische apparatuur tegen eigen schade door gebruik in \"vijandige omgevingen\" en tegen eventueel gevaar voor de gebruiker volgens IEC 60529.",
                                        constraints="",
                                        usagenote="",
                                        deprecated_version="")
        """De IP-codering als een aanduiding voor de mate van beveiliging van de constructie van elektrische of elektronische apparatuur tegen eigen schade door gebruik in \"vijandige omgevingen\" en tegen eventueel gevaar voor de gebruiker volgens IEC 60529."""

        self.keuringsfrequentie = KwantWrdInJaar()
        """Frequentie (in jaar) waarmee de kast moet onderworpen worden aan een periodieke keuring door een externe dienst voor technische controle."""
        self.keuringsfrequentie.naam = "keuringsfrequentie"
        self.keuringsfrequentie.label = "keuringsfrequentie"
        self.keuringsfrequentie.uri = "https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Buitenkast.keuringsfrequentie"
        self.keuringsfrequentie.definition = "Frequentie (in jaar) waarmee de kast moet onderworpen worden aan een periodieke keuring door een externe dienst voor technische controle."
        self.keuringsfrequentie.constraints = ""
        self.keuringsfrequentie.usagenote = ""
        self.keuringsfrequentie.deprecated_version = ""

        self.verfraaid = KeuzelijstField(naam="verfraaid",
                                         label="verfraaid",
                                         lijst=KlBuitenkastVerfraaid(),
                                         uri="https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Buitenkast.verfraaid",
                                         definition="Geeft aan of de wegkantkast voorzien van verfraaiing en of die al dan niet vergund is.",
                                         constraints="",
                                         usagenote="",
                                         deprecated_version="")
        """Geeft aan of de wegkantkast voorzien van verfraaiing en of die al dan niet vergund is."""
