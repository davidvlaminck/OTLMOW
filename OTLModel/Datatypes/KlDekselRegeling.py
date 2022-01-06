# coding=utf-8
from OTLModel.Datatypes.Keuzelijst import Keuzelijst


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlDekselRegeling(Keuzelijst):
    """Mogelijke regelingen van het deksel."""

    def __init__(self):
        super().__init__(naam="KlDekselRegeling",
                         label="Dekselregeling",
                         uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlDekselRegeling",
                         definition="Mogelijke regelingen van het deksel.",
                         usagenote="",
                         deprecated_version="",
                         codelist="https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlDekselRegeling")

        self.add_option("met-ter-plaatse-gestorte-ringbalk", "met ter plaatse gestorte ringbalk", "met ter plaatse gestorte ringbalk", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlDekselRegeling/met-ter-plaatse-gestorte-ringbalk")
        self.add_option("ingestort-in-de-dakplaat-van-kunstwerken", "ingestort in de dakplaat van kunstwerken", "ingestort in de dakplaat van kunstwerken", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlDekselRegeling/ingestort-in-de-dakplaat-van-kunstwerken")
        self.add_option("geprefabriceerd-of-ter-plaatse-gestorte-regeling", "geprefabriceerd of ter plaatse gestorte regeling", "geprefabriceerd of ter plaatse gestorte regeling", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlDekselRegeling/geprefabriceerd-of-ter-plaatse-gestorte-regeling")
        self.add_option("Traploos-instelbare-afdekkingsinrichting", "Traploos instelbare afdekkingsinrichting", "Traploos instelbare afdekkingsinrichting", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlDekselRegeling/Traploos-instelbare-afdekkingsinrichting")
