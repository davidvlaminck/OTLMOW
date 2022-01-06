from abc import abstractmethod
from OTLModel.Classes.AIMObject import AIMObject
from OTLModel.Datatypes.DecimalFloatField import DecimalFloatField
from OTLModel.Datatypes.DtcVegetatieSoortnaam import DtcVegetatieSoortnaam
from OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLModel.Datatypes.KlVegetatieelementHoogte import KlVegetatieelementHoogte


# Generated with OTLClassCreator. To modify: extend, do not edit
class VegetatieElement(AIMObject):
    """Abstracte om alle gemeenschappelijke eigenschappen en relaties van de solitaire plant in de ruimte onder 1 noemer te plaatsen."""

    typeURI = "https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#VegetatieElement"
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    @abstractmethod
    def __init__(self):
        super().__init__()

        self.hoogte = KeuzelijstField(naam="hoogte",
                                      label="hoogte",
                                      lijst=KlVegetatieelementHoogte(),
                                      uri="https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#VegetatieElement.hoogte",
                                      definition="De hoogteklasse van het vegetatie-element.",
                                      constraints="",
                                      usagenote="",
                                      deprecated_version="")
        """De hoogteklasse van het vegetatie-element."""

        self.niveau = DecimalFloatField(naam="niveau",
                                        label="niveau",
                                        uri="https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#VegetatieElement.niveau",
                                        definition="Het niveau waarop het object zich bevindt, relatief ten opzichte van andere objecten. Negatieve waarden worden geassocieerd met ondergronds en positieve waarden met bovengronds. Nul wordt beschouwd als een absolute waarde om het maaiveld aan te duiden.",
                                        constraints="",
                                        usagenote="",
                                        deprecated_version="")
        """Het niveau waarop het object zich bevindt, relatief ten opzichte van andere objecten. Negatieve waarden worden geassocieerd met ondergronds en positieve waarden met bovengronds. Nul wordt beschouwd als een absolute waarde om het maaiveld aan te duiden."""

        self.soortnaam = DtcVegetatieSoortnaam()
        """Met deze eigenschap worden de Nederlandse soortnaam, wetenschappelijke soortnaam en de soortcode van de plantensoort weergegeven."""
        self.soortnaam.naam = "soortnaam"
        self.soortnaam.label = "soortnaam"
        self.soortnaam.uri = "https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#VegetatieElement.soortnaam"
        self.soortnaam.definition = "Met deze eigenschap worden de Nederlandse soortnaam, wetenschappelijke soortnaam en de soortcode van de plantensoort weergegeven."
        self.soortnaam.constraints = ""
        self.soortnaam.usagenote = ""
        self.soortnaam.deprecated_version = ""
