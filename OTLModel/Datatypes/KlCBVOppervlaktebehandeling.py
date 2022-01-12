# coding=utf-8
from OTLModel.Datatypes.Keuzelijst import Keuzelijst


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlCBVOppervlaktebehandeling(Keuzelijst):
    """Oppervalktebehandelingen van de cement/beton verharding."""

    def __init__(self):
        super().__init__(naam="KlCBVOppervlaktebehandeling",
                         label="CBV oppervlaktebehandeling",
                         objectUri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlCBVOppervlaktebehandeling",
                         definition="Oppervalktebehandelingen van de cement/beton verharding.",
                         usagenote="",
                         deprecated_version="",
                         codelist="https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlCBVOppervlaktebehandeling")

        self.add_option("Reinigen-met-water-onder-hoge-druk-(minstens-50-bar)-", "Reinigen met water onder hoge druk (minstens 50 bar) ", "Reinigen met water onder hoge druk (minstens 50 bar) ", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlCBVOppervlaktebehandeling/Reinigen-met-water-onder-hoge-druk-(minstens-50-bar)-")
        self.add_option("bezemen", "bezemen", "Bezemen", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlCBVOppervlaktebehandeling/bezemen")
        self.add_option("eenvoudig-dwars-bezemen", "eenvoudig dwars bezemen", "Eenvoudig dwars bezemen", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlCBVOppervlaktebehandeling/eenvoudig-dwars-bezemen")
        self.add_option("eenvoudig-langs-bezemen", "eenvoudig langs bezemen", "Eenvoudig langs bezemen", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlCBVOppervlaktebehandeling/eenvoudig-langs-bezemen")
        self.add_option("figureren", "figureren", "Figureren", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlCBVOppervlaktebehandeling/figureren")
        self.add_option("uitwassen-van-het-steenslagskelet", "uitwassen van het steenslagskelet", "Uitwassen van het steenslagskelet", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlCBVOppervlaktebehandeling/uitwassen-van-het-steenslagskelet")
