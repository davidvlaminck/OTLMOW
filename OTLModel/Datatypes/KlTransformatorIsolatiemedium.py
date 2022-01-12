# coding=utf-8
from OTLModel.Datatypes.Keuzelijst import Keuzelijst


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlTransformatorIsolatiemedium(Keuzelijst):
    """Wijze van onderdompeling van de magnetische kring en van de wikkelingen van de transformator."""

    def __init__(self):
        super().__init__(naam="KlTransformatorIsolatiemedium",
                         label="Transformator isolatiemedium",
                         objectUri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlTransformatorIsolatiemedium",
                         definition="Wijze van onderdompeling van de magnetische kring en van de wikkelingen van de transformator.",
                         usagenote="",
                         deprecated_version="",
                         codelist="https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlTransformatorIsolatiemedium")

        self.add_option("droog", "droog", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlTransformatorIsolatiemedium/droog")
        self.add_option("esterolie", "esterolie", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlTransformatorIsolatiemedium/esterolie")
        self.add_option("giethars", "giethars", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlTransformatorIsolatiemedium/giethars")
        self.add_option("minerale-olie", "minerale olie", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlTransformatorIsolatiemedium/minerale-olie")
        self.add_option("siliconenvloeistof", "siliconenvloeistof", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlTransformatorIsolatiemedium/siliconenvloeistof")
        self.add_option("vegetale-olie", "vegetale olie", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlTransformatorIsolatiemedium/vegetale-olie")
