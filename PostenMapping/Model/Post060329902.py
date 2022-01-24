# coding=utf-8
from PostenMapping.StandaardPost import StandaardPost
from PostenMapping.StandaardPostMapping import StandaardPostMapping


# Generated with PostenCreator. To modify: extend, do not edit
class Post060329902(StandaardPost):
    def __init__(self):
        super().__init__(
            nummer='0603.29902',
            beschrijving='Voegvulling van mortel, bouwklasse B6-B10 volgens 6-3.3.4.2.E',
            meetstaateenheid='M2',
            mappings=[StandaardPostMapping(
                typeURI='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#BestratingVanMozaiekkei',
                attribuutURI='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Bestrating.voegvulling',
                dotnotatie='voegvulling',
                defaultWaarde='mortel-met-bouwklasse-B6-B10',
                range='',
                usagenote='',
                isMeetstaatAttr=0,
                isAltijdInTeVullen=0,
                isBasisMapping=1,
                mappingStatus='gemapt 2.0',
                mappingOpmerking='',
                standaardpostnummer='0603.29902')
                , StandaardPostMapping(
                typeURI='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#BestratingVanMozaiekkei',
                attribuutURI='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Laag.oppervlakte',
                dotnotatie='oppervlakte',
                defaultWaarde='',
                range='',
                usagenote='m2^^cdt:ucumunit',
                isMeetstaatAttr=1,
                isAltijdInTeVullen=0,
                isBasisMapping=0,
                mappingStatus='gemapt 2.0',
                mappingOpmerking='',
                standaardpostnummer='0603.29902')])
