# coding=utf-8
from OTLModel.Datatypes.Keuzelijst import Keuzelijst


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlOnderbouwType(Keuzelijst):
    """Types van onderbouw."""

    def __init__(self):
        super().__init__(naam="KlOnderbouwType",
                         label="Onderbouw type",
                         uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlOnderbouwType",
                         definition="Types van onderbouw.",
                         usagenote="",
                         deprecated_version="",
                         codelist="https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlOnderbouwType")

        self.add_option("onderfundering-type-I", "onderfundering type I", "onderfundering type I", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlOnderbouwType/onderfundering-type-I")
        self.add_option("onderfundering-type-II", "onderfundering type II", "onderfundering type II", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlOnderbouwType/onderfundering-type-II")
        self.add_option("onderfundering-type-III", "onderfundering type III", "onderfundering type III", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlOnderbouwType/onderfundering-type-III")
        self.add_option("wortelruimte---bomenzand", "wortelruimte - bomenzand", "Fundering wortelruimte - bomenzand", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlOnderbouwType/wortelruimte---bomenzand")
        self.add_option("wortelruimte---bomengranulaat", "wortelruimte - bomengranulaat", "Fundering wortelruimte - bomengranulaat", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlOnderbouwType/wortelruimte---bomengranulaat")
        self.add_option("wortelruimte---groeiplaatsconstructie", "wortelruimte - groeiplaatsconstructie", "Fundering wortelruimte - groeiplaatsconstructie", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlOnderbouwType/wortelruimte---groeiplaatsconstructie")
        self.add_option("steenslag-met-niet-continue-korrelverdeling", "steenslag met niet-continue korrelverdeling", "Fundering van steenslagfundering met niet-continue korrelverdeling", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlOnderbouwType/steenslag-met-niet-continue-korrelverdeling")
        self.add_option("steenslag-met-continue-korrelverdeling-zonder-toevoegsel---type-I", "steenslag met continue korrelverdeling zonder toevoegsel - type I", "Fundering van steenslag met continue korrelverdeling zonder toevoegsel - type I", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlOnderbouwType/steenslag-met-continue-korrelverdeling-zonder-toevoegsel---type-I")
        self.add_option("met-toevoegsel-behandelde-steenslag-met-continue-korrelverdeling---type-IA", "met toevoegsel behandelde steenslag met continue korrelverdeling - type IA", "Fundering van met toevoegsel behandelde steenslag met continue korrelverdeling - type IA", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlOnderbouwType/met-toevoegsel-behandelde-steenslag-met-continue-korrelverdeling---type-IA")
        self.add_option("teerhoudend-asfaltgranulaatcement", "teerhoudend asfaltgranulaatcement", "Fundering in teerhoudend asfaltgranulaatcement", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlOnderbouwType/teerhoudend-asfaltgranulaatcement")
        self.add_option("ternair-mengsel", "ternair mengsel", "Fundering van ternair mengsel", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlOnderbouwType/ternair-mengsel")
        self.add_option("stabiliseren-van-de-bestaande-verharding-met-cement-(recycling-in-situ)", "stabiliseren van de bestaande verharding met cement (recycling in situ)", "Fundering door het stabiliseren van de bestaande verharding met cement (recycling in situ)", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlOnderbouwType/stabiliseren-van-de-bestaande-verharding-met-cement-(recycling-in-situ)")
        self.add_option("schraal-beton", "schraal beton", "Fundering van schraal beton.", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlOnderbouwType/schraal-beton")
        self.add_option("drainerend-schraal-beton", "drainerend schraal beton", "Fundering van drainerend schraal beton", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlOnderbouwType/drainerend-schraal-beton")
        self.add_option("walsbeton", "walsbeton", "Fundering van walsbeton.", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlOnderbouwType/walsbeton")
        self.add_option("schraal-asfalt", "schraal asfalt", "Fundering van schraal asfalt", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlOnderbouwType/schraal-asfalt")
        self.add_option("waterdoorlatende-steenslagfundering", "waterdoorlatende steenslagfundering", "Fundering van waterdoorlatende steenslagfundering", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlOnderbouwType/waterdoorlatende-steenslagfundering")
        self.add_option("zand", "zand", "Fundering van zand", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlOnderbouwType/zand")
        self.add_option("zandcement", "zandcement", "Fundering van zandcement", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlOnderbouwType/zandcement")
        self.add_option("granulaatmengsel-0-4", "granulaatmengsel 0-4", "Fundering van granulaatmengsel 0/4", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlOnderbouwType/granulaatmengsel-0-4")
        self.add_option("granulaatmengsel-0-6.3", "granulaatmengsel 0-6.3", "Fudnering van granulaatmengsel 0/6.3", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlOnderbouwType/granulaatmengsel-0-6.3")
        self.add_option("mortel", "mortel", "Fundering van mortel", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlOnderbouwType/mortel")
        self.add_option("steenslag-2-6.3", "steenslag 2-6.3", "Fundering van steenslag 2/6.3", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlOnderbouwType/steenslag-2-6.3")
        self.add_option("bodemsubstraat-met-zand", "bodemsubstraat met zand", "Fundering van bodemsubstraat met zand", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlOnderbouwType/bodemsubstraat-met-zand")
        self.add_option("bodemsubstraat-met-steenslag", "bodemsubstraat met steenslag", "Fundering van bodemsubstraat met steenslag", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlOnderbouwType/bodemsubstraat-met-steenslag")
        self.add_option("bodemsubstraat", "bodemsubstraat", "Fundering van bodemsubstraat", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlOnderbouwType/bodemsubstraat")
        self.add_option("tijdelijke-steenslag-miv-verwijdering", "tijdelijke steenslag miv verwijdering", "Fundering van tijdelijke steenslag miv verwijdering", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlOnderbouwType/tijdelijke-steenslag-miv-verwijdering")
        self.add_option("skeletbodems", "skeletbodems", "Fundering van skeletbodems.", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlOnderbouwType/skeletbodems")
        self.add_option("vliegas-kalkmengsel", "vliegas kalkmengsel", "Fundering van vliesgas-kalkmengsel", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlOnderbouwType/vliegas-kalkmengsel")
        self.add_option("vliegas-cementmengsel", "vliegas cementmengsel", "Fundering van vliesgas-cementmengsel.", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlOnderbouwType/vliegas-cementmengsel")
        self.add_option("zandcement-met-stut", "zandcement met stut", "Fundering van zandcement met stut", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlOnderbouwType/zandcement-met-stut")
        self.add_option("schraalbeton-met-stut", "schraalbeton met stut", "Fundering van schraalbeton met stut", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlOnderbouwType/schraalbeton-met-stut")
        self.add_option("met-toevoegsel-behandelde-steenslag-met-continue-korrelverdeling---type-IB", "met toevoegsel behandelde steenslag met continue korrelverdeling - type IB", "Fundering van met toevoegsel behandelde steenslag met continue korrelverdeling - type IB", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlOnderbouwType/met-toevoegsel-behandelde-steenslag-met-continue-korrelverdeling---type-IB")
        self.add_option("met-toevoegsel-behandelde-steenslag-met-continue-korrelverdeling---type-IIA", "met toevoegsel behandelde steenslag met continue korrelverdeling - type IIA", "Fundering van met toevoegsel behandelde steenslag met continue korrelverdeling - type IIA", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlOnderbouwType/met-toevoegsel-behandelde-steenslag-met-continue-korrelverdeling---type-IIA")
        self.add_option("met-toevoegsel-behandelde-steenslag-met-continue-korrelverdeling---type-IIB", "met toevoegsel behandelde steenslag met continue korrelverdeling - type IIB", "Fundering van met toevoegsel behandelde steenslag met continue korrelverdeling - type IIB", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlOnderbouwType/met-toevoegsel-behandelde-steenslag-met-continue-korrelverdeling---type-IIB")
        self.add_option("steenslag-met-continue-korrelverdeling-zonder-toevoegsel---type-II", "steenslag met continue korrelverdeling zonder toevoegsel - type II", "Fundering van steenslag met continue korrelverdeling zonder toevoegsel - type II", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlOnderbouwType/steenslag-met-continue-korrelverdeling-zonder-toevoegsel---type-II")
        self.add_option("steenslag-2-4", "steenslag 2-4", "Fundering van steenslag 2/4", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlOnderbouwType/steenslag-2-4")
        self.add_option("drainerend-zandcement", "drainerend zandcement", "Fundering van drainerend zandcement.", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlOnderbouwType/drainerend-zandcement")
        self.add_option("geschikt-gemaakt-aanvullingsmateriaal", "geschikt gemaakt aanvullingsmateriaal", "Fundering van geschikt gemaakt aanvullingsmateriaal", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlOnderbouwType/geschikt-gemaakt-aanvullingsmateriaal")
        self.add_option("draineerzand", "draineerzand", "Fundering van draineerzand.", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlOnderbouwType/draineerzand")
        self.add_option("steenslag-of-rolgrind", "steenslag of rolgrind", "Fundering van steenslag of rolgrind.", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlOnderbouwType/steenslag-of-rolgrind")
        self.add_option("granulaatcement", "granulaatcement", "granulaatcement", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlOnderbouwType/granulaatcement")
