# coding=utf-8
from OTLModel.Datatypes.Keuzelijst import Keuzelijst


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlGeotextielType(Keuzelijst):
    """Types van geotextiel."""

    def __init__(self):
        super().__init__(naam="KlGeotextielType",
                         label="Geotextiel type",
                         uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlGeotextielType",
                         definition="Types van geotextiel.",
                         usagenote="",
                         deprecated_version="",
                         codelist="https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlGeotextielType")

        self.add_option("erosiewerend", "erosiewerend", "erosiewerend", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlGeotextielType/erosiewerend")
        self.add_option("bescherming", "bescherming", "bescherming/wapening", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlGeotextielType/bescherming")
        self.add_option("niet-geweven-geotextiel", "niet-geweven geotextiel", "niet-geweven geotextiel", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlGeotextielType/niet-geweven-geotextiel")
        self.add_option("anti-vraatdoek", "anti-vraatdoek", "anti-vraatdoek", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlGeotextielType/anti-vraatdoek")
        self.add_option("wapening", "wapening", "bescherming/wapening", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlGeotextielType/wapening")
