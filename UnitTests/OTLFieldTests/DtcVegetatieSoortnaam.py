from UnitTests.OTLFieldTests.AttributeInfo import AttributeInfo
from UnitTests.OTLFieldTests.OTLAttribuut import OTLAttribuut
from UnitTests.OTLFieldTests.StringField import StringField
from UnitTests.OTLFieldTests.ComplexField import ComplexField


class DtcVegetatieSoortnaamWaarden(AttributeInfo):
    def __init__(self):
        self._code = OTLAttribuut(field=StringField,
                                  naam="code",
                                  label="code",
                                  objectUri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DtcVegetatieSoortnaam.code",
                                  definition="",
                                  constraints="",
                                  usagenote="De GBIF code is een unieke gestandaardiseerde code uitgegeven door het GBIF (the Global Biodiversity Information Facility - GBIF.org)",
                                  deprecated_version="")

        self._soortnaamNederlands = OTLAttribuut(field=StringField,
                                                 label="soortnaam nederlands",
                                                 objectUri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DtcVegetatieSoortnaam.soortnaamNederlands",
                                                 definition="De Nederlandse soortnaam van de beplanting.",
                                                 constraints="",
                                                 usagenote="",
                                                 deprecated_version="")

        self._soortnaamWetenschappelijk = OTLAttribuut(field=StringField,
                                                       naam="soortnaamWetenschappelijk",
                                                       label="soortnaam wetenschappelijk",
                                                       objectUri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DtcVegetatieSoortnaam.soortnaamWetenschappelijk",
                                                       definition="De wetenschappelijke soortnaam van de beplanting.",
                                                       constraints="",
                                                       usagenote="",
                                                       deprecated_version="")

    @property
    def code(self):
        """De GBIF code is een unieke gestandaardiseerde code uitgegeven door het GBIF (the Global Biodiversity Information Facility - GBIF.org)"""
        return self._code.waarde

    @code.setter
    def code(self, value):
        self._code.set_waarde(value)

    @property
    def soortnaamNederlands(self):
        """Gegevens van de organisatie die de toekenning deed."""
        return self._soortnaamNederlands.waarde

    @soortnaamNederlands.setter
    def soortnaamNederlands(self, value):
        self._soortnaamNederlands.set_waarde(value)

    @property
    def soortnaamWetenschappelijk(self):
        """De wetenschappelijke soortnaam van de beplanting."""
        return self._soortnaamWetenschappelijk.waarde

    @soortnaamWetenschappelijk.setter
    def soortnaamWetenschappelijk(self, value):
        self._soortnaamWetenschappelijk.set_waarde(value)


class DtcVegetatieSoortnaam(ComplexField, AttributeInfo):
    naam = "soort",
    label = "soort",
    objectUri = "https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#BegroeidVoorkomen.soort",
    definition = "Met deze eigenschap worden de Nederlandse soortnaam, wetenschappelijke soortnaam en de soortcode van de meest voorkomende soorten binnen het begroeid oppervlak weergegeven.",
    usagenote = "",
    deprecated_version = ""
    waardeObject = DtcVegetatieSoortnaamWaarden
