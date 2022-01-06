# coding=utf-8
from OTLModel.Datatypes.Keuzelijst import Keuzelijst


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlRoosterIndeling(Keuzelijst):
    """Deze keuzelijst geeft aan hoe het rooster ingedeeld is: met zijdelingse opvang of dat er sprake is van een 1-delig of 2-delig rooster."""

    def __init__(self):
        super().__init__(naam="KlRoosterIndeling",
                         label="Rooster indeling",
                         uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlRoosterIndeling",
                         definition="Deze keuzelijst geeft aan hoe het rooster ingedeeld is: met zijdelingse opvang of dat er sprake is van een 1-delig of 2-delig rooster.",
                         usagenote="",
                         deprecated_version="",
                         codelist="https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlRoosterIndeling")

        self.add_option("1-delig", "1-delig", "1-delig", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlRoosterIndeling/1-delig")
        self.add_option("2-delig", "2-delig", "2-delig", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlRoosterIndeling/2-delig")
        self.add_option("zijdelingse-opvang", "zijdelingse opvang", "zijdelingse opvang", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlRoosterIndeling/zijdelingse-opvang")
