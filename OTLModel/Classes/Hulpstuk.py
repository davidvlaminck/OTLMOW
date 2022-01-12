# coding=utf-8
from OTLModel.Classes.LinkendElement import LinkendElement
from OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLModel.Datatypes.KlAansluitstukMateriaal import KlAansluitstukMateriaal
from OTLModel.Datatypes.KlHulpstukType import KlHulpstukType
from OTLModel.Datatypes.KwantWrdInMillimeter import KwantWrdInMillimeter


# Generated with OTLClassCreator. To modify: extend, do not edit
class Hulpstuk(LinkendElement):
    """Stukken die zorgen voor verbindingen tussen rechte buizen om bv. van richting te veranderen, te verlengen, te verlopen van diameter, meerdere buizen op mekaar aan te sluiten,..."""

    typeURI = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Hulpstuk"
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.inwendigeDiameter = KwantWrdInMillimeter()
        """De diameter van de binnenzijde van het hulpstuk in millimeter."""
        self.inwendigeDiameter.naam = "inwendigeDiameter"
        self.inwendigeDiameter.label = "inwendige diameter"
        self.inwendigeDiameter.objectUri = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Hulpstuk.inwendigeDiameter"
        self.inwendigeDiameter.definition = "De diameter van de binnenzijde van het hulpstuk in millimeter."
        self.inwendigeDiameter.constraints = ""
        self.inwendigeDiameter.usagenote = ""
        self.inwendigeDiameter.deprecated_version = ""

        self.materiaal = KeuzelijstField(naam="materiaal",
                                         label="materiaal",
                                         lijst=KlAansluitstukMateriaal(),
                                         objectUri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Hulpstuk.materiaal",
                                         definition="Het materiaal waaruit het hulpstuk vervaardigd is.",
                                         constraints="",
                                         usagenote="",
                                         deprecated_version="")
        """Het materiaal waaruit het hulpstuk vervaardigd is."""

        self.type = KeuzelijstField(naam="type",
                                    label="type",
                                    lijst=KlHulpstukType(),
                                    objectUri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Hulpstuk.type",
                                    definition="Het type van het hulpstuk.",
                                    constraints="",
                                    usagenote="",
                                    deprecated_version="")
        """Het type van het hulpstuk."""

        self.uitwendigeDiameter = KwantWrdInMillimeter()
        """De diameter van de buitenzijde van het hulpstuk in millimeter."""
        self.uitwendigeDiameter.naam = "uitwendigeDiameter"
        self.uitwendigeDiameter.label = "uitwendige diameter"
        self.uitwendigeDiameter.objectUri = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Hulpstuk.uitwendigeDiameter"
        self.uitwendigeDiameter.definition = "De diameter van de buitenzijde van het hulpstuk in millimeter."
        self.uitwendigeDiameter.constraints = ""
        self.uitwendigeDiameter.usagenote = ""
        self.uitwendigeDiameter.deprecated_version = ""
