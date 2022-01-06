# coding=utf-8
from OTLModel.Datatypes.Keuzelijst import Keuzelijst


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlSchanskorfVorm(Keuzelijst):
    """Vormen van schanskorven."""

    def __init__(self):
        super().__init__(naam="KlSchanskorfVorm",
                         label="Schanskorf vorm",
                         uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlSchanskorfVorm",
                         definition="Vormen van schanskorven.",
                         usagenote="",
                         deprecated_version="",
                         codelist="https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlSchanskorfVorm")

        self.add_option("in-blokvorm", "in blokvorm", "in blokvorm", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlSchanskorfVorm/in-blokvorm")
        self.add_option("in-matrasvorm", "in matrasvorm", "in matrasvorm", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlSchanskorfVorm/in-matrasvorm")
