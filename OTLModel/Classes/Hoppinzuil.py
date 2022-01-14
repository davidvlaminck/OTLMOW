# coding=utf-8
from abc import abstractmethod
from OTLModel.Classes.AIMObject import AIMObject
from OTLModel.Datatypes.KardinaliteitField import KardinaliteitField
from OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLModel.Datatypes.KlWeergegevenVervoersmodiOpKaart import KlWeergegevenVervoersmodiOpKaart
from OTLModel.Datatypes.StringField import StringField


# Generated with OTLClassCreator. To modify: extend, do not edit
class Hoppinzuil(AIMObject):
    """Abstracte om de gemeenschappelijke eigenschappen van de verschillende hoppinzuilen onder 1 noemer te plaatsen."""

    typeURI = "https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Hoppinzuil"
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    @abstractmethod
    def __init__(self):
        super().__init__()

        weergegevenVervoersmodiOpKaartField = KeuzelijstField(naam="weergegevenVervoersmodiOpKaart",
                                                              label="weergegeven vervoersmodi op kaart",
                                                              lijst=KlWeergegevenVervoersmodiOpKaart(),
                                                              objectUri="https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Hoppinzuil.weergegevenVervoersmodiOpKaart",
                                                              definition="De verschillende beschikbare vervoersmodi die op de bijhorende kaart worden weergegeven.",
                                                              constraints="",
                                                              usagenote="",
                                                              deprecated_version="")
        self.weergegevenVervoersmodiOpKaart = KardinaliteitField(minKardinaliteit="1", maxKardinaliteit="*", fieldToMultiply=weergegevenVervoersmodiOpKaartField)
        """De verschillende beschikbare vervoersmodi die op de bijhorende kaart worden weergegeven."""

        self.zuilnaam = StringField(naam="zuilnaam",
                                    label="zuilnaam",
                                    objectUri="https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Hoppinzuil.zuilnaam",
                                    definition="Naam van het hoppinpunt die verwijst naar een duidelijke en herkenbare plaatsnaam.",
                                    constraints="",
                                    usagenote="",
                                    deprecated_version="")
        """Naam van het hoppinpunt die verwijst naar een duidelijke en herkenbare plaatsnaam."""

        self.zuilnummer = StringField(naam="zuilnummer",
                                      label="zuilnummer",
                                      objectUri="https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Hoppinzuil.zuilnummer",
                                      definition="Uniek identificatienummer dat elke zuil krijgt en dat wordt opgenomen in de hoppinpuntendatabank.",
                                      constraints="",
                                      usagenote="",
                                      deprecated_version="")
        """Uniek identificatienummer dat elke zuil krijgt en dat wordt opgenomen in de hoppinpuntendatabank."""
