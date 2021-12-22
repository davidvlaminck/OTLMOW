from OTLModel.Datatypes.Keuzelijst import Keuzelijst


# Generated with OTLEnumerationCreator
class KlOverstortMateriaalDrempel(Keuzelijst):
    """De materialen van vervaardiging van de overstort."""

    def __init__(self):
        super().__init__(naam="KlOverstortMateriaalDrempel",
                         label="Overstort materiaal drempel",
                         uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlOverstortMateriaalDrempel",
                         definition="De materialen van vervaardiging van de overstort.",
                         usagenote="",
                         deprecated_version="",
                         codelist="https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlOverstortMateriaalDrempel")

        self.add_option("metselwerk", "metselwerk", "metselwerk", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlOverstortMateriaalDrempel/metselwerk")
        self.add_option("beton", "beton", "beton", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlOverstortMateriaalDrempel/beton")
