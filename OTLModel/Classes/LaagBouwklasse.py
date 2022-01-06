# coding=utf-8
from abc import abstractmethod
from OTLModel.Classes.ArtificieleLaag import ArtificieleLaag
from OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLModel.Datatypes.KlAlgBouwklassegroep import KlAlgBouwklassegroep


# Generated with OTLClassCreator. To modify: extend, do not edit
class LaagBouwklasse(ArtificieleLaag):
    """Abstracte waarmee aan een laag het attribuut bouwklasse wordt toegekend."""

    typeURI = "https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#LaagBouwklasse"
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    @abstractmethod
    def __init__(self):
        super().__init__()

        self.bouwklasse = KeuzelijstField(naam="bouwklasse",
                                          label="bouwklasse",
                                          lijst=KlAlgBouwklassegroep(),
                                          uri="https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#LaagBouwklasse.bouwklasse",
                                          definition="Een maat voor de verkeersbelasting over de volledige levensduur van de laag. De laag is ontworpen volgens de aangeduide bouwklasse.",
                                          constraints="",
                                          usagenote="",
                                          deprecated_version="")
        """Een maat voor de verkeersbelasting over de volledige levensduur van de laag. De laag is ontworpen volgens de aangeduide bouwklasse."""
