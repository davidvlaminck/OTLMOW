# coding=utf-8
from OTLModel.Classes.AIMObject import AIMObject
from OTLModel.Datatypes.KwantWrdInWatt import KwantWrdInWatt


# Generated with OTLClassCreator. To modify: extend, do not edit
class Verwarmingslint(AIMObject):
    """Verwarmbare omwikkeling voor onderdelen die moeten beschermd worden tegen bevriezing."""

    typeURI = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Verwarmingslint"
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.vermogen = KwantWrdInWatt()
        """Het vereiste vermogen in watt voor de correcte werking van het verwarmingslint."""
        self.vermogen.naam = "vermogen"
        self.vermogen.label = "vermogen"
        self.vermogen.uri = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Verwarmingslint.vermogen"
        self.vermogen.definition = "Het vereiste vermogen in watt voor de correcte werking van het verwarmingslint."
        self.vermogen.constraints = ""
        self.vermogen.usagenote = ""
        self.vermogen.deprecated_version = ""
