# coding=utf-8
from abc import abstractmethod
from OTLModel.Classes.Kantopsluiting import Kantopsluiting
from OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLModel.Datatypes.KlLEKantopsluitingBijkomendeParameter import KlLEKantopsluitingBijkomendeParameter
from OTLModel.Datatypes.KlLEStandaardFabricageLengte import KlLEStandaardFabricageLengte


# Generated with OTLClassCreator. To modify: extend, do not edit
class GestandaardiseerdeKantopsluiting(Kantopsluiting):
    """Abstracte voor een kantopsluiting die voldoet aan een bepaalde standaard."""

    typeURI = "https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#GestandaardiseerdeKantopsluiting"
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    @abstractmethod
    def __init__(self):
        super().__init__()

        self.bijkomendeParameter = KeuzelijstField(naam="bijkomendeParameter",
                                                   label="bijkomende parameter",
                                                   lijst=KlLEKantopsluitingBijkomendeParameter(),
                                                   objectUri="https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#GestandaardiseerdeKantopsluiting.bijkomendeParameter",
                                                   definition="Detail typering van de kantopsluiting.",
                                                   constraints="",
                                                   usagenote="",
                                                   deprecated_version="")
        """Detail typering van de kantopsluiting."""

        self.fabricageLengte = KeuzelijstField(naam="fabricageLengte",
                                               label="fabricagelengte",
                                               lijst=KlLEStandaardFabricageLengte(),
                                               objectUri="https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#GestandaardiseerdeKantopsluiting.fabricageLengte",
                                               definition="De lengte van de individuele kantopsluiting volgens de norm.",
                                               constraints="",
                                               usagenote="",
                                               deprecated_version="")
        """De lengte van de individuele kantopsluiting volgens de norm."""
