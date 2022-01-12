# coding=utf-8
from OTLModel.Datatypes.ComplexField import ComplexField
from OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLModel.Datatypes.KlLETrottoirbandVorm import KlLETrottoirbandVorm
from OTLModel.Datatypes.KwantWrdInCentimeter import KwantWrdInCentimeter


# Generated with OTLComplexDatatypeCreator. To modify: extend, do not edit
class DtcTrottoirbandVorm(ComplexField):
    """Complex datatype voor de vorm van een trotoirband."""

    def __init__(self):
        super().__init__(naam="DtcTrottoirbandVorm",
                         label="Trottoirband vorm",
                         objectUri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DtcTrottoirbandVorm",
                         definition="Complex datatype voor de vorm van een trotoirband.",
                         usagenote="",
                         deprecated_version="")

        self.waarde.breedte = KwantWrdInCentimeter()
        """De breedte van de trottoirband."""
        self.waarde.breedte.naam = "breedte"
        self.waarde.breedte.label = "breedte"
        self.waarde.breedte.objectUri = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DtcTrottoirbandVorm.breedte"
        self.waarde.breedte.definition = "De breedte van de trottoirband."
        self.waarde.breedte.constraints = ""
        self.waarde.breedte.usagenote = ""
        self.waarde.breedte.deprecated_version = ""
        self.breedte = self.waarde.breedte

        self.waarde.dikte = KwantWrdInCentimeter()
        """De dikte van de trottoirband."""
        self.waarde.dikte.naam = "dikte"
        self.waarde.dikte.label = "dikte"
        self.waarde.dikte.objectUri = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DtcTrottoirbandVorm.dikte"
        self.waarde.dikte.definition = "De dikte van de trottoirband."
        self.waarde.dikte.constraints = ""
        self.waarde.dikte.usagenote = ""
        self.waarde.dikte.deprecated_version = ""
        self.dikte = self.waarde.dikte

        self.waarde.vorm = KeuzelijstField(naam="vorm",
                                           label="vorm",
                                           lijst=KlLETrottoirbandVorm(),
                                           objectUri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DtcTrottoirbandVorm.vorm",
                                           definition="De vorm van de trottoirband.",
                                           constraints="",
                                           usagenote="",
                                           deprecated_version="")
        self.vorm = self.waarde.vorm
        """De vorm van de trottoirband."""
