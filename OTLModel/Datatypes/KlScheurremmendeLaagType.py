# coding=utf-8
from OTLModel.Datatypes.Keuzelijst import Keuzelijst


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlScheurremmendeLaagType(Keuzelijst):
    """Types van scheurremmende laag."""

    def __init__(self):
        super().__init__(naam="KlScheurremmendeLaagType",
                         label="Scheurremmende laag type",
                         uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlScheurremmendeLaagType",
                         definition="Types van scheurremmende laag.",
                         usagenote="",
                         deprecated_version="",
                         codelist="https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlScheurremmendeLaagType")

        self.add_option("geocomposiet-klasse-c", "geocomposiet klasse C", "geocomposiet klasse C", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlScheurremmendeLaagType/geocomposiet-klasse-c")
        self.add_option("geocomposiet-klasse-cd", "geocomposiet klasse CD", "geocomposiet klasse CD", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlScheurremmendeLaagType/geocomposiet-klasse-cd")
        self.add_option("geocomposiet", "geocomposiet", "geocomposiet", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlScheurremmendeLaagType/geocomposiet")
        self.add_option("geocomposiet-klasse-e-1", "geocomposiet klasse E1", "geocomposiet klasse E1", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlScheurremmendeLaagType/geocomposiet-klasse-e-1")
        self.add_option("grids-klasse-e-2", "grids klasse E2", "grids klasse E2", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlScheurremmendeLaagType/grids-klasse-e-2")
        self.add_option("grids-klasse-c", "grids klasse C", "grids klasse C", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlScheurremmendeLaagType/grids-klasse-c")
        self.add_option("stalen-wapeningsnet-type-1", "stalen wapeningsnet type 1", "stalen wapeningsnet type 1", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlScheurremmendeLaagType/stalen-wapeningsnet-type-1")
        self.add_option("geocomposiet-klasse-e-2", "geocomposiet klasse E2", "geocomposiet klasse E2", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlScheurremmendeLaagType/geocomposiet-klasse-e-2")
        self.add_option("grids-klasse-e-1", "grids klasse E1", "grids klasse E1", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlScheurremmendeLaagType/grids-klasse-e-1")
        self.add_option("grids-klasse-d", "grids klasse D", "grids klasse D", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlScheurremmendeLaagType/grids-klasse-d")
        self.add_option("geocomposiet-klasse-d", "geocomposiet klasse D", "geocomposiet klasse D", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlScheurremmendeLaagType/geocomposiet-klasse-d")
        self.add_option("bitumineus-membraan-(SAMI)", "bitumineus membraan (SAMI)", "bitumineus membraan (SAMI)", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlScheurremmendeLaagType/bitumineus-membraan-(SAMI)")
        self.add_option("stalen-wapeningsnet-type-2", "stalen wapeningsnet type 2", "stalen wapeningsnet type 2", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlScheurremmendeLaagType/stalen-wapeningsnet-type-2")
        self.add_option("grids", "grids", "grids", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlScheurremmendeLaagType/grids")
        self.add_option("grids-klasse-cd", "grids klasse CD", "grids klasse CD", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlScheurremmendeLaagType/grids-klasse-cd")
