from abc import abstractmethod
from OTLModel.Classes.AIMNaamObject import AIMNaamObject
from OTLModel.Datatypes.BooleanField import BooleanField
from OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLModel.Datatypes.KlLantaarnVormgeving import KlLantaarnVormgeving
from OTLModel.Datatypes.KlSeinlantaarnDiameter import KlSeinlantaarnDiameter
from OTLModel.Datatypes.KlSeinlantaarnMerk import KlSeinlantaarnMerk
from OTLModel.Datatypes.KlSeinlantaarnModelnaam import KlSeinlantaarnModelnaam


# Generated with OTLClassCreator. To modify: extend, do not edit
class Seinlantaarn(AIMNaamObject):
    """Abstracte voor het geheel van één of meerdere verkeerslichten die boven elkaar worden opgesteld en worden bevestigd op een steun,teneinde de beweging van een weggebruiker die een bepaald traject volgt,te verhinderen of toe te laten."""

    typeURI = "https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Seinlantaarn"
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    @abstractmethod
    def __init__(self):
        super().__init__()

        self.diameter = KeuzelijstField(naam="diameter",
                                        label="diameter",
                                        lijst=KlSeinlantaarnDiameter(),
                                        uri="https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Seinlantaarn.diameter",
                                        definition="Diameter (in mm) van de lens van de verkeerslichten waaruit de lantaarn is samengesteld.",
                                        constraints="",
                                        usagenote="",
                                        deprecated_version="")
        """Diameter (in mm) van de lens van de verkeerslichten waaruit de lantaarn is samengesteld."""

        self.heeftContrastscherm = BooleanField(naam="heeftContrastscherm",
                                                label="heeft contrastscherm aanwezig",
                                                uri="https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Seinlantaarn.heeftContrastscherm",
                                                definition="Aanduiding of er een contrastscherm aanwezig is op de lantaarn.",
                                                constraints="",
                                                usagenote="",
                                                deprecated_version="")
        """Aanduiding of er een contrastscherm aanwezig is op de lantaarn."""

        self.merk = KeuzelijstField(naam="merk",
                                    label="merk",
                                    lijst=KlSeinlantaarnMerk(),
                                    uri="https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Seinlantaarn.merk",
                                    definition="Het merk van een de seinlantaarn.",
                                    constraints="",
                                    usagenote="",
                                    deprecated_version="")
        """Het merk van een de seinlantaarn."""

        self.modelnaam = KeuzelijstField(naam="modelnaam",
                                         label="modelnaam",
                                         lijst=KlSeinlantaarnModelnaam(),
                                         uri="https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Seinlantaarn.modelnaam",
                                         definition="De modelnaam/product range van de seinlantaarn.",
                                         constraints="",
                                         usagenote="",
                                         deprecated_version="")
        """De modelnaam/product range van de seinlantaarn."""

        self.vormgeving = KeuzelijstField(naam="vormgeving",
                                          label="vormgeving",
                                          lijst=KlLantaarnVormgeving(),
                                          uri="https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Seinlantaarn.vormgeving",
                                          definition="Type vormgeving van de seinlantaarn.",
                                          constraints="",
                                          usagenote="",
                                          deprecated_version="")
        """Type vormgeving van de seinlantaarn."""
