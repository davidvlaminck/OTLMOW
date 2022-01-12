# coding=utf-8
from OTLModel.Datatypes.Keuzelijst import Keuzelijst


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlRasterMazen(Keuzelijst):
    """Types van de mazen in het ecoraster."""

    def __init__(self):
        super().__init__(naam="KlRasterMazen",
                         label="Rastermazen",
                         objectUri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlRasterMazen",
                         definition="Types van de mazen in het ecoraster.",
                         usagenote="",
                         deprecated_version="",
                         codelist="https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlRasterMazen")

        self.add_option("fijnmazig", "fijnmazig", "Een fijnmazig raster.", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlRasterMazen/fijnmazig")
        self.add_option("grofmazig", "grofmazig", "Een grofmazig raster.", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlRasterMazen/grofmazig")
