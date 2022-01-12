# coding=utf-8
from OTLModel.Datatypes.Keuzelijst import Keuzelijst


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlDekselVergrendeling(Keuzelijst):
    """Manieren waarop het deksel is vergrendeld."""

    def __init__(self):
        super().__init__(naam="KlDekselVergrendeling",
                         label="Dekselvergrendeling",
                         objectUri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlDekselVergrendeling",
                         definition="Manieren waarop het deksel is vergrendeld.",
                         usagenote="",
                         deprecated_version="",
                         codelist="https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlDekselVergrendeling")

        self.add_option("bouten", "bouten", "Het deksel is vergrendeld met inox schroefbouten met zeskantmoer", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlDekselVergrendeling/bouten")
        self.add_option("haken", "haken", "Het deksel is met haken vergrendeld", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlDekselVergrendeling/haken")
        self.add_option("inbus", "inbus", "Het deksel is vergrendeld met inox schroefbouten met inbusmoer", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlDekselVergrendeling/inbus")
