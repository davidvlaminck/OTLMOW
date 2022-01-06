# coding=utf-8
from OTLModel.Datatypes.Keuzelijst import Keuzelijst


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlSelLusVerbinding(Keuzelijst):
    """Keuzelijst met soorten verbindingen voor selectieve lussen."""

    def __init__(self):
        super().__init__(naam="KlSelLusVerbinding",
                         label="Selectieve lus verbinding",
                         uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlSelLusVerbinding",
                         definition="Keuzelijst met soorten verbindingen voor selectieve lussen.",
                         usagenote="",
                         deprecated_version="",
                         codelist="https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlSelLusVerbinding")

        self.add_option("contact", "contact", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlSelLusVerbinding/contact")
        self.add_option("serieel", "serieel", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlSelLusVerbinding/serieel")
