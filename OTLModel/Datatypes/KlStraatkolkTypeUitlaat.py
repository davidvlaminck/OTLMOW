# coding=utf-8
from OTLModel.Datatypes.Keuzelijst import Keuzelijst


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlStraatkolkTypeUitlaat(Keuzelijst):
    """Het type van uitlaat van de straatkolk."""

    def __init__(self):
        super().__init__(naam="KlStraatkolkTypeUitlaat",
                         label="straatkolk type uitlaat ",
                         objectUri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlStraatkolkTypeUitlaat",
                         definition="Het type van uitlaat van de straatkolk.",
                         usagenote="",
                         deprecated_version="",
                         codelist="https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlStraatkolkTypeUitlaat")

        self.add_option("kop-uitlaat", "kop uitlaat", "kop uitlaat", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlStraatkolkTypeUitlaat/kop-uitlaat")
        self.add_option("onderuitlaat", "onderuitlaat", "onderuitlaat", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlStraatkolkTypeUitlaat/onderuitlaat")
        self.add_option("zij-uitlaat", "zij uitlaat", "zij uitlaat", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlStraatkolkTypeUitlaat/zij-uitlaat")
