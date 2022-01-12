# coding=utf-8
from OTLModel.Datatypes.Keuzelijst import Keuzelijst


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlAlgRijrichting(Keuzelijst):
    """De mogelijke rijrichtingen."""

    def __init__(self):
        super().__init__(naam="KlAlgRijrichting",
                         label="Rijrichting",
                         objectUri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlAlgRijrichting",
                         definition="De mogelijke rijrichtingen.",
                         usagenote="",
                         deprecated_version="",
                         codelist="https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlAlgRijrichting")

        self.add_option("aflopend", "aflopend", "Aflopende rijrichting.", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAlgRijrichting/aflopend")
        self.add_option("oplopend", "oplopend", "Oplopende rijrichting.", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAlgRijrichting/oplopend")
