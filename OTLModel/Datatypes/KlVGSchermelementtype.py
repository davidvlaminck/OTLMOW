# coding=utf-8
from OTLModel.Datatypes.Keuzelijst import Keuzelijst


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlVGSchermelementtype(Keuzelijst):
    """Het type vlak-schermelement."""

    def __init__(self):
        super().__init__(naam="KlVGSchermelementtype",
                         label="Vlak geluidsschermelementtype",
                         uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlVGSchermelementtype",
                         definition="Het type vlak-schermelement.",
                         usagenote="",
                         deprecated_version="",
                         codelist="https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlVGSchermelementtype")

        self.add_option("schermelement-zonder-profielen", "schermelement zonder profielen", "schermelement zonder profielen", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVGSchermelementtype/schermelement-zonder-profielen")
        self.add_option("schermelement-geplaatst-tussen-profielen", "schermelement geplaatst tussen profielen", "schermelement geplaatst tussen profielen", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVGSchermelementtype/schermelement-geplaatst-tussen-profielen")
        self.add_option("schermelement-bevestigd-tegen-de-profielen", "schermelement bevestigd tegen de profielen", "schermelement bevestigd tegen de profielen", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVGSchermelementtype/schermelement-bevestigd-tegen-de-profielen")
