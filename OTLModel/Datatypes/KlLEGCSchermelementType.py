# coding=utf-8
from OTLModel.Datatypes.Keuzelijst import Keuzelijst


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlLEGCSchermelementType(Keuzelijst):
    """Schermelement types."""

    def __init__(self):
        super().__init__(naam="KlLEGCSchermelementType",
                         label="Schermelement type",
                         uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlLEGCSchermelementType",
                         definition="Schermelement types.",
                         usagenote="Klasse uit gebruik sinds versie 2.0.0",
                         deprecated_version="2.0.0",
                         codelist="https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlLEGCSchermelementType")

        self.add_option("bloembakelement", "bloembakelement", "bloembakelement", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLEGCSchermelementType/bloembakelement")
        self.add_option("voertuigkerend", "voertuigkerend", "voertuigkerend", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLEGCSchermelementType/voertuigkerend")
        self.add_option("l-element", "l-element", "l-element", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLEGCSchermelementType/l-element")
        self.add_option("schermelement-tussen-palen", "schermelement tussen palen", "schermelement tussen palen", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLEGCSchermelementType/schermelement-tussen-palen")
