# coding=utf-8
from OTLModel.Classes.AIMObject import AIMObject
from OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLModel.Datatypes.KlTypeBeschoeiing import KlTypeBeschoeiing
from OTLModel.Datatypes.KwantWrdInMeter import KwantWrdInMeter


# Generated with OTLClassCreator. To modify: extend, do not edit
class KringsBerliner(AIMObject):
    """Een grond- en/of waterkerende constructie, die bestaat uit een verticaal in de grond geplaatste wand."""

    typeURI = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KringsBerliner"
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.beschoeiingsLengte = KwantWrdInMeter()
        """De totale lengte van de beschoeiing langs de sleuf in lopende meter."""
        self.beschoeiingsLengte.naam = "beschoeiingsLengte"
        self.beschoeiingsLengte.label = "beschoeiingslengte"
        self.beschoeiingsLengte.objectUri = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KringsBerliner.beschoeiingsLengte"
        self.beschoeiingsLengte.definition = "De totale lengte van de beschoeiing langs de sleuf in lopende meter."
        self.beschoeiingsLengte.constraints = ""
        self.beschoeiingsLengte.usagenote = ""
        self.beschoeiingsLengte.deprecated_version = ""

        self.buisdiepte = KwantWrdInMeter()
        """De diepte van de buis."""
        self.buisdiepte.naam = "buisdiepte"
        self.buisdiepte.label = "buisdiepte"
        self.buisdiepte.objectUri = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KringsBerliner.buisdiepte"
        self.buisdiepte.definition = "De diepte van de buis."
        self.buisdiepte.constraints = ""
        self.buisdiepte.usagenote = ""
        self.buisdiepte.deprecated_version = ""

        self.type = KeuzelijstField(naam="type",
                                    label="type",
                                    lijst=KlTypeBeschoeiing(),
                                    objectUri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KringsBerliner.type",
                                    definition="Het type beschoeiing.",
                                    constraints="",
                                    usagenote="",
                                    deprecated_version="")
        """Het type beschoeiing."""
