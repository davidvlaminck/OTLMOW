# coding=utf-8
from OTLModel.Datatypes.ComplexField import ComplexField
from OTLModel.Datatypes.StringField import StringField


# Generated with OTLComplexDatatypeCreator. To modify: extend, do not edit
class DtcVegetatieSoortnaam(ComplexField):
    """Complex datatype voor de soortnaam en code van een begroeiing."""

    def __init__(self):
        super().__init__(naam="DtcVegetatieSoortnaam",
                         label="Vegetatie soortnaam",
                         objectUri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DtcVegetatieSoortnaam",
                         definition="Complex datatype voor de soortnaam en code van een begroeiing.",
                         usagenote="",
                         deprecated_version="")

        self.waarde.code = StringField(naam="code",
                                       label="code",
                                       objectUri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DtcVegetatieSoortnaam.code",
                                       definition="De unieke identificator voor de soort van het vegetatie-element.",
                                       constraints="",
                                       usagenote="De GBIF code is een unieke gestandaardiseerde code uitgegeven door het GBIF (the Global Biodiversity Information Facility - GBIF.org)",
                                       deprecated_version="")
        self.code = self.waarde.code
        """De unieke identificator voor de soort van het vegetatie-element."""

        self.waarde.soortnaamNederlands = StringField(naam="soortnaamNederlands",
                                                      label="soortnaam nederlands",
                                                      objectUri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DtcVegetatieSoortnaam.soortnaamNederlands",
                                                      definition="De Nederlandse soortnaam van de beplanting.",
                                                      constraints="",
                                                      usagenote="",
                                                      deprecated_version="")
        self.soortnaamNederlands = self.waarde.soortnaamNederlands
        """De Nederlandse soortnaam van de beplanting."""

        self.waarde.soortnaamWetenschappelijk = StringField(naam="soortnaamWetenschappelijk",
                                                            label="soortnaam wetenschappelijk",
                                                            objectUri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DtcVegetatieSoortnaam.soortnaamWetenschappelijk",
                                                            definition="De wetenschappelijke soortnaam van de beplanting.",
                                                            constraints="",
                                                            usagenote="",
                                                            deprecated_version="")
        self.soortnaamWetenschappelijk = self.waarde.soortnaamWetenschappelijk
        """De wetenschappelijke soortnaam van de beplanting."""
