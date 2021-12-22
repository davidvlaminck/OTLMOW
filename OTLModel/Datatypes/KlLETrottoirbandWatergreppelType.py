from OTLModel.Datatypes.Keuzelijst import Keuzelijst


# Generated with OTLEnumerationCreator
class KlLETrottoirbandWatergreppelType(Keuzelijst):
    """De vormen van een trottoirband_watergreppel."""

    def __init__(self):
        super().__init__(naam="KlLETrottoirbandWatergreppelType",
                         label="Trottoirband watergreppel type",
                         uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlLETrottoirbandWatergreppelType",
                         definition="De vormen van een trottoirband_watergreppel.",
                         usagenote="",
                         deprecated_version="",
                         codelist="https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlLETrottoirbandWatergreppelType")

        self.add_option("type-III-A", "type III A", "type III A", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLETrottoirbandWatergreppelType/type-III-A")
        self.add_option("type-III-B", "type III B", "type III B", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLETrottoirbandWatergreppelType/type-III-B")
        self.add_option("type-III-C", "type III C", "type III C", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLETrottoirbandWatergreppelType/type-III-C")
        self.add_option("type-III-D", "type III D", "type III D", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLETrottoirbandWatergreppelType/type-III-D")
        self.add_option("type-III-E", "type III E", "type III E", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLETrottoirbandWatergreppelType/type-III-E")
