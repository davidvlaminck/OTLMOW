from abc import abstractmethod
from OTLModel.Classes.AIMNaamObject import AIMNaamObject
from OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLModel.Datatypes.KlVerkeerslichtMasker import KlVerkeerslichtMasker
from OTLModel.Datatypes.KlVerkeerslichtMerk import KlVerkeerslichtMerk
from OTLModel.Datatypes.KlVerkeerslichtModelnaam import KlVerkeerslichtModelnaam
from OTLModel.Datatypes.KwantWrdInWatt import KwantWrdInWatt


# Generated with OTLClassCreator
class Verkeerslicht(AIMNaamObject):
    """Abstracte voor verkeerslichten. Dit zijn apparaten, opgesteld naast of boven de weg, om weggebruikers visueel te geleiden over een kruispunt door het gebruik van rode, oranje-gele en groene lichten. De bepalingen van de wegcode zijn van toepassing, meer bepaald titel III, hoofdstuk I, artikelen 61 t.e.m. 64."""

    typeURI = "https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Verkeerslicht"
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    @abstractmethod
    def __init__(self):
        super().__init__()
        self.masker = KeuzelijstField(naam="masker",
                                      label="masker",
                                      lijst=KlVerkeerslichtMasker(),
                                      uri="https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Verkeerslicht.masker",
                                      definition="Type masker dat is aangebracht op het verkeerslicht.",
                                      constraints="",
                                      usagenote="",
                                      deprecated_version="")
        """Type masker dat is aangebracht op het verkeerslicht."""

        self.merk = KeuzelijstField(naam="merk",
                                    label="merk",
                                    lijst=KlVerkeerslichtMerk(),
                                    uri="https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Verkeerslicht.merk",
                                    definition="Het merk van het verkeerslicht.",
                                    constraints="",
                                    usagenote="",
                                    deprecated_version="")
        """Het merk van het verkeerslicht."""

        self.modelnaam = KeuzelijstField(naam="modelnaam",
                                         label="modelnaam",
                                         lijst=KlVerkeerslichtModelnaam(),
                                         uri="https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Verkeerslicht.modelnaam",
                                         definition="De modelnaam/product range van het verkeerslicht.",
                                         constraints="",
                                         usagenote="",
                                         deprecated_version="")
        """De modelnaam/product range van het verkeerslicht."""

        self.vermogen = KwantWrdInWatt()
        """Vermogen (Watt) van het verkeerslicht."""
        self.vermogen.naam = "vermogen"
        self.vermogen.label = "vermogen"
        self.vermogen.uri = "https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Verkeerslicht.vermogen"
        self.vermogen.definition = "Vermogen (Watt) van het verkeerslicht."
        self.vermogen.constraints = ""
        self.vermogen.usagenote = ""
        self.vermogen.deprecated_version = ""
