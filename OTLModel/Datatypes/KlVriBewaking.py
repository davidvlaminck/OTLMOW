# coding=utf-8
from OTLModel.Datatypes.Keuzelijst import Keuzelijst


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlVriBewaking(Keuzelijst):
    """Keuzelijst met verschillende soorten bewaking of detectie bij een VRI."""

    def __init__(self):
        super().__init__(naam="KlVriBewaking",
                         label="VRI bewaking",
                         uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlVriBewaking",
                         definition="Keuzelijst met verschillende soorten bewaking of detectie bij een VRI.",
                         usagenote="",
                         deprecated_version="",
                         codelist="https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlVriBewaking")

        self.add_option("bewaakt-primair-alarm", "bewaakt primair alarm", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVriBewaking/bewaakt-primair-alarm")
        self.add_option("bewaakt-secundair-alarm", "bewaakt secundair alarm", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVriBewaking/bewaakt-secundair-alarm")
        self.add_option("bewaakt-zonder-alarm", "bewaakt zonder alarm", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVriBewaking/bewaakt-zonder-alarm")
        self.add_option("niet-bewaakt", "niet bewaakt", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVriBewaking/niet-bewaakt")
