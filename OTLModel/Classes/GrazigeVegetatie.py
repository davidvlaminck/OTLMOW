from abc import abstractmethod
from OTLModel.Classes.BegroeidVoorkomen import BegroeidVoorkomen
from OTLModel.Datatypes.BooleanField import BooleanField
from OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLModel.Datatypes.KlGrazigeVegetatieAanleg import KlGrazigeVegetatieAanleg


# Generated with OTLClassCreator
class GrazigeVegetatie(BegroeidVoorkomen):
    """Begroeiingen die uit grassen en (bloeiende) kruiden bestaan."""

    typeURI = "https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#GrazigeVegetatie"
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    @abstractmethod
    def __init__(self):
        super().__init__()
        self.aanleg = KeuzelijstField(naam="aanleg",
                                      label="aanleg",
                                      lijst=KlGrazigeVegetatieAanleg(),
                                      uri="https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#GrazigeVegetatie.aanleg",
                                      definition="De wijze van aanleg/aanplanting van de grazige vegetatie.",
                                      constraints="",
                                      usagenote="",
                                      deprecated_version="")
        """De wijze van aanleg/aanplanting van de grazige vegetatie."""

        self.heeftBolgewassen = BooleanField(naam="heeftBolgewassen",
                                             label="heeft bolgewassen",
                                             uri="https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#GrazigeVegetatie.heeftBolgewassen",
                                             definition="Grasland met bol- en knolgewassen die in het voorjaar bloeien.",
                                             constraints="",
                                             usagenote="",
                                             deprecated_version="")
        """Grasland met bol- en knolgewassen die in het voorjaar bloeien."""

        self.isOvergroeienRandVerharding = BooleanField(naam="isOvergroeienRandVerharding",
                                                        label="is overgroeien rand verharding",
                                                        uri="https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#GrazigeVegetatie.isOvergroeienRandVerharding",
                                                        definition="Geeft aan of de rand van de verharding al dan niet wordt overgroeid door de grazige vegetatie.",
                                                        constraints="",
                                                        usagenote="",
                                                        deprecated_version="")
        """Geeft aan of de rand van de verharding al dan niet wordt overgroeid door de grazige vegetatie."""
