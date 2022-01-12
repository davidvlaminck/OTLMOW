# coding=utf-8
from OTLModel.Classes.AIMObject import AIMObject
from OTLModel.Datatypes.KwantWrdInMeter import KwantWrdInMeter


# Generated with OTLClassCreator. To modify: extend, do not edit
class PiezometrischeBuis(AIMObject):
    """Een al dan niet permanente buis om waterstanden bij grondverlaging te meten."""

    typeURI = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#PiezometrischeBuis"
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.diepte = KwantWrdInMeter()
        """De diepte vanaf maaiveld tot de onderkant van de piezometrische buis in meter."""
        self.diepte.naam = "diepte"
        self.diepte.label = "diepte"
        self.diepte.objectUri = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#PiezometrischeBuis.diepte"
        self.diepte.definition = "De diepte vanaf maaiveld tot de onderkant van de piezometrische buis in meter."
        self.diepte.constraints = ""
        self.diepte.usagenote = ""
        self.diepte.deprecated_version = ""
