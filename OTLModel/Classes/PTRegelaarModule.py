from abc import abstractmethod
from OTLModel.Classes.AIMNaamObject import AIMNaamObject
from OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLModel.Datatypes.KlPTRegelaarModuleMerk import KlPTRegelaarModuleMerk
from OTLModel.Datatypes.KlPTRegelaarModuleModelnaam import KlPTRegelaarModuleModelnaam


# Generated with OTLClassCreator
class PTRegelaarModule(AIMNaamObject):
    """Abstracte voor de verschillende modules waaruit het personentransportbeïnvloedingssysteem van de verkeersregelaar opgebouwd is. Hierdoor zal het personentransport een snellere doorstroming aan een verkeerslichtengeregeld kruispunt genieten."""

    typeURI = "https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#PTRegelaarModule"
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    @abstractmethod
    def __init__(self):
        super().__init__()
        self.merk = KeuzelijstField(naam="merk",
                                    label="merk",
                                    lijst=KlPTRegelaarModuleMerk(),
                                    uri="https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#PTRegelaarModule.merk",
                                    definition="Het merk van de PT regelaar module.",
                                    constraints="",
                                    usagenote="",
                                    deprecated_version="")
        """Het merk van de PT regelaar module."""

        self.modelnaam = KeuzelijstField(naam="modelnaam",
                                         label="modelnaam",
                                         lijst=KlPTRegelaarModuleModelnaam(),
                                         uri="https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#PTRegelaarModule.modelnaam",
                                         definition="De modelnaam/product range van de PT regelaar module.",
                                         constraints="",
                                         usagenote="",
                                         deprecated_version="")
        """De modelnaam/product range van de PT regelaar module."""
