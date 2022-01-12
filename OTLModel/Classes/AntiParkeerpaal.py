# coding=utf-8
from OTLModel.Classes.Straatmeubilair import Straatmeubilair
from OTLModel.Datatypes.AntiParkeerpaalType import AntiParkeerpaalType
from OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLModel.Datatypes.KlAntiparkeerpaalMateriaal import KlAntiparkeerpaalMateriaal
from OTLModel.Datatypes.KlPlaatsingswijze import KlPlaatsingswijze


# Generated with OTLClassCreator. To modify: extend, do not edit
class AntiParkeerpaal(Straatmeubilair):
    """Een paal met als doel het parkeren te verhinderen."""

    typeURI = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#AntiParkeerpaal"
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.materiaal = KeuzelijstField(naam="materiaal",
                                         label="materiaal",
                                         lijst=KlAntiparkeerpaalMateriaal(),
                                         objectUri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#AntiParkeerpaal.materiaal",
                                         definition="Het materiaal van de Amsterdammer.",
                                         constraints="",
                                         usagenote="",
                                         deprecated_version="")
        """Het materiaal van de Amsterdammer."""

        self.plaatsingswijze = KeuzelijstField(naam="plaatsingswijze",
                                               label="plaatsingswijze",
                                               lijst=KlPlaatsingswijze(),
                                               objectUri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#AntiParkeerpaal.plaatsingswijze",
                                               definition="Aanduiding of de anti-parkeerpaal eenvoudig wegneembaar is.",
                                               constraints="",
                                               usagenote="",
                                               deprecated_version="")
        """Aanduiding of de anti-parkeerpaal eenvoudig wegneembaar is."""

        self.type = KeuzelijstField(naam="type",
                                    label="type",
                                    lijst=AntiParkeerpaalType(),
                                    objectUri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#AntiParkeerpaal.type",
                                    definition="Vorm van de anti-parkeerpaal.",
                                    constraints="",
                                    usagenote="",
                                    deprecated_version="")
        """Vorm van de anti-parkeerpaal."""
