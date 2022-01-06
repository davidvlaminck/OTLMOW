# coding=utf-8
from OTLModel.Datatypes.Keuzelijst import Keuzelijst


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlLEGCMateriaal(Keuzelijst):
    """Materialen van de geluidswerende constructie."""

    def __init__(self):
        super().__init__(naam="KlLEGCMateriaal",
                         label="Materiaal",
                         uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlLEGCMateriaal",
                         definition="Materialen van de geluidswerende constructie.",
                         usagenote="",
                         deprecated_version="",
                         codelist="https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlLEGCMateriaal")

        self.add_option("metaal---aluminium-en-staal", "metaal - aluminium en staal", "Metaal - aluminium en staal", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLEGCMateriaal/metaal---aluminium-en-staal")
        self.add_option("beton---steenparament", "beton - steenparament", "Beton - steenparament", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLEGCMateriaal/beton---steenparament")
        self.add_option("metaal---aluminium", "metaal - aluminium", "Metaal - aluminium", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLEGCMateriaal/metaal---aluminium")
        self.add_option("tunnelplaat", "tunnelplaat", "tunnelplaat", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLEGCMateriaal/tunnelplaat")
        self.add_option("glas", "glas", "glas", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLEGCMateriaal/glas")
        self.add_option("beton---lichtgewichtbeton", "beton - lichtgewichtbeton", "beton - lichtgewichtbeton", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLEGCMateriaal/beton---lichtgewichtbeton")
        self.add_option("hout", "hout", "hout", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLEGCMateriaal/hout")
        self.add_option("kunststof---PMMA", "kunststof - PMMA", "Kunststof - PMMA", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLEGCMateriaal/kunststof---PMMA")
        self.add_option("kunststof---PVC", "kunststof - PVC", "kunststof - PVC", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLEGCMateriaal/kunststof---PVC")
        self.add_option("stalen-raster-met-beschermnet-in-kunststof", "stalen raster met beschermnet in kunststof", "stalen raster met beschermnet in kunststof", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLEGCMateriaal/stalen-raster-met-beschermnet-in-kunststof")
        self.add_option("kokospanelen", "kokospanelen", "kokospanelen", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLEGCMateriaal/kokospanelen")
        self.add_option("bakstenen", "bakstenen", "bakstenen", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLEGCMateriaal/bakstenen")
        self.add_option("metaal---staal", "metaal - staal", "metaal - staal", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLEGCMateriaal/metaal---staal")
        self.add_option("groenscherm", "groenscherm", "groenscherm", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLEGCMateriaal/groenscherm")
        self.add_option("beton", "beton", "beton", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLEGCMateriaal/beton")
        self.add_option("beton---houtvezelbeton", "beton - houtvezelbeton", "beton - houtvezelbeton", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLEGCMateriaal/beton---houtvezelbeton")
