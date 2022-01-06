# coding=utf-8
from OTLModel.Datatypes.Keuzelijst import Keuzelijst


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlBVLaagtype(Keuzelijst):
    """Laagtypes van de bitumineuze verharding."""

    def __init__(self):
        super().__init__(naam="KlBVLaagtype",
                         label="BV laagtype",
                         uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlBVLaagtype",
                         definition="Laagtypes van de bitumineuze verharding.",
                         usagenote="",
                         deprecated_version="",
                         codelist="https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlBVLaagtype")

        self.add_option("toplaag-van-asfaltbeton", "toplaag van asfaltbeton", "Bovenste laag van een bitumineuze verharding, die direct in contact komt met het verkeer bestaande uit asfaltbeton.", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBVLaagtype/toplaag-van-asfaltbeton")
        self.add_option("onderlaag", "onderlaag", "Onderliggende laag van een bitumineuze verharding met een constante dikte. ", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBVLaagtype/onderlaag")
        self.add_option("tussenlaag", "tussenlaag", "Bitumineuze laag die aangebracht wordt tussen een betonverharding en de fundering. ", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBVLaagtype/tussenlaag")
        self.add_option("profileerlaag", "profileerlaag", "union type om het laagtype van bitumineuze verharding te bepalen", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBVLaagtype/profileerlaag")
        self.add_option("beschermingslaag", "beschermingslaag", "beschermingslaag", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBVLaagtype/beschermingslaag")
        self.add_option("toplaag-van-gietasfalt", "toplaag van gietasfalt", "union type om het laagtype van bitumineuze verharding te bepalen", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBVLaagtype/toplaag-van-gietasfalt")
        self.add_option("andere-toplagen", "andere toplagen", "union type om het laagtype van bitumineuze verharding te bepalen", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBVLaagtype/andere-toplagen")
