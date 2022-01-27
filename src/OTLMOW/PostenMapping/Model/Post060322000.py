# coding=utf-8
from OTLMOW.PostenMapping.StandaardPost import StandaardPost
from OTLMOW.PostenMapping.StandaardPostMapping import StandaardPostMapping


# Generated with PostenCreator. To modify: extend, do not edit
class Post060322000(StandaardPost):
    def __init__(self):
        super().__init__(
            nummer='0603.22000',
            beschrijving='Bestratingen van mozaïekkeien volgens 6-3.3, van het 2de formaat',
            meetstaateenheid='M2',
            mappings=[StandaardPostMapping(
                typeURI='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#BestratingVanMozaiekkei',
                attribuutURI='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#BestratingVanMozaiekkei.formaat',
                dotnotatie='formaat',
                defaultWaarde='bestratingen-van-mozaïekkeien-van-het-2de-formaat',
                range='',
                usagenote='',
                isMeetstaatAttr=0,
                isAltijdInTeVullen=0,
                isBasisMapping=1,
                mappingStatus='gemapt 2.0',
                mappingOpmerking='',
                standaardpostnummer='0603.22000')
                , StandaardPostMapping(
                typeURI='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#BestratingVanMozaiekkei',
                attribuutURI='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Laag.laagRol',
                dotnotatie='laagRol',
                defaultWaarde='straatlaag',
                range='',
                usagenote='',
                isMeetstaatAttr=0,
                isAltijdInTeVullen=0,
                isBasisMapping=1,
                mappingStatus='gemapt 2.0',
                mappingOpmerking='',
                standaardpostnummer='0603.22000')
                , StandaardPostMapping(
                typeURI='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#BestratingVanMozaiekkei',
                attribuutURI='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Laag.oppervlakte',
                dotnotatie='oppervlakte',
                defaultWaarde='',
                range='',
                usagenote='m2^^cdt:ucumunit',
                isMeetstaatAttr=1,
                isAltijdInTeVullen=1,
                isBasisMapping=1,
                mappingStatus='gemapt 2.0',
                mappingOpmerking='',
                standaardpostnummer='0603.22000')])