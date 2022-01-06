# coding=utf-8
from OTLModel.Datatypes.Keuzelijst import Keuzelijst


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlBGSchermelementtype(Keuzelijst):
    """Het type bijzonder-schermelement."""

    def __init__(self):
        super().__init__(naam="KlBGSchermelementtype",
                         label="Bijzonder geluidsschermelementtype",
                         uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlBGSchermelementtype",
                         definition="Het type bijzonder-schermelement.",
                         usagenote="",
                         deprecated_version="",
                         codelist="https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlBGSchermelementtype")

        self.add_option("bloembakelement", "bloembakelement", "bloembakelement", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBGSchermelementtype/bloembakelement")
        self.add_option("l-element", "L-element", "L-element", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBGSchermelementtype/l-element")
