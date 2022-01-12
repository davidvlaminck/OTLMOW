# coding=utf-8
from abc import abstractmethod
from OTLModel.Classes.ConstructieElement import ConstructieElement
from OTLModel.Datatypes.KwantWrdInCentimeter import KwantWrdInCentimeter
from OTLModel.Datatypes.KwantWrdInMeterTAW import KwantWrdInMeterTAW


# Generated with OTLClassCreator. To modify: extend, do not edit
class Fundering(ConstructieElement):
    """Abstracte voor verschillende manieren om er voor te zorgen dat het eigen gewicht van het object dat de fundering krijgt en de krachten uitgeoefend op dat object, zoals nuttige belasting, sneeuw, winddruk, enzovoorts, worden overgedragen op de draagkrachtige ondergrond. Een fundering zit hoofdzakelijk onder het maaiveld en heeft tot doel het stabiliseren van een ander object."""

    typeURI = "https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Fundering"
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    @abstractmethod
    def __init__(self):
        super().__init__()

        self.aanzetpeil = KwantWrdInMeterTAW()
        """De hoogte van het laagste punt van de onderkant van een element, ten opzichte van gemiddeld laagwaterpeil te Oostende (TAWpeil)."""
        self.aanzetpeil.naam = "aanzetpeil"
        self.aanzetpeil.label = "aanzetpeil"
        self.aanzetpeil.objectUri = "https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Fundering.aanzetpeil"
        self.aanzetpeil.definition = "De hoogte van het laagste punt van de onderkant van een element, ten opzichte van gemiddeld laagwaterpeil te Oostende (TAWpeil)."
        self.aanzetpeil.constraints = ""
        self.aanzetpeil.usagenote = ""
        self.aanzetpeil.deprecated_version = ""
