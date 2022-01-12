# coding=utf-8
from OTLModel.Datatypes.Keuzelijst import Keuzelijst


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlTypeSchanskorf(Keuzelijst):
    """Keuzelijst met de verschillende types schanskorven."""

    def __init__(self):
        super().__init__(naam="KlTypeSchanskorf",
                         label="Type schanskorf",
                         objectUri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlTypeSchanskorf",
                         definition="Keuzelijst met de verschillende types schanskorven.",
                         usagenote="",
                         deprecated_version="",
                         codelist="https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlTypeSchanskorf")

        self.add_option("5-x-7", "5 x 7", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlTypeSchanskorf/5-x-7")
        self.add_option("6-x-8", "6 x 8", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlTypeSchanskorf/6-x-8")
