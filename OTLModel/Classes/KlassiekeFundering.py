# coding=utf-8
from abc import abstractmethod
from OTLModel.Classes.BetonnenConstructieElement import BetonnenConstructieElement
from OTLModel.Classes.Fundering import Fundering
from OTLModel.Datatypes.DtuAfmetingGrondvlak import DtuAfmetingGrondvlak
from OTLModel.Datatypes.KwantWrdInCentimeter import KwantWrdInCentimeter


# Generated with OTLClassCreator. To modify: extend, do not edit
class KlassiekeFundering(BetonnenConstructieElement, Fundering):
    """Abstracte voor ondiepe en halfdiepe funderingen. Fundering op staal en op putten."""

    typeURI = "https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#KlassiekeFundering"
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    @abstractmethod
    def __init__(self):
        BetonnenConstructieElement.__init__(self)
        Fundering.__init__(self)

        self.funderingshoogte = KwantWrdInCentimeter()
        """De afstand tussen het laagste punt van de onderkant en hoogste punt van de bovenkant van de fundering."""
        self.funderingshoogte.naam = "funderingshoogte"
        self.funderingshoogte.label = "funderingshoogte"
        self.funderingshoogte.uri = "https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#KlassiekeFundering.funderingshoogte"
        self.funderingshoogte.definition = "De afstand tussen het laagste punt van de onderkant en hoogste punt van de bovenkant van de fundering."
        self.funderingshoogte.constraints = ""
        self.funderingshoogte.usagenote = ""
        self.funderingshoogte.deprecated_version = ""

        self.grondvlakAfmeting = DtuAfmetingGrondvlak()
        """De afmetingen van het (grond)vlak, van de bovenkant van de fundering, volgens de vorm."""
        self.grondvlakAfmeting.naam = "grondvlakAfmeting"
        self.grondvlakAfmeting.label = "grondvlakafmeting"
        self.grondvlakAfmeting.uri = "https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#KlassiekeFundering.grondvlakAfmeting"
        self.grondvlakAfmeting.definition = "De afmetingen van het (grond)vlak, van de bovenkant van de fundering, volgens de vorm."
        self.grondvlakAfmeting.constraints = ""
        self.grondvlakAfmeting.usagenote = ""
        self.grondvlakAfmeting.deprecated_version = ""
