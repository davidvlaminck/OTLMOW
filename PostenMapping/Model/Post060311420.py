# coding=utf-8
from PostenMapping.StandaardPost import StandaardPost
from PostenMapping.StandaardPostMapping import StandaardPostMapping


# Generated with PostenCreator. To modify: extend, do not edit
class Post060311420(StandaardPost):
    def __init__(self):
        super().__init__(
            nummer='0603.11420',
            beschrijving='Bestrating van in rijen te leggen kasseien volgens 6-3.2, langwerpige kasseien 14 x 20 cm',
            meetstaateenheid='M2',
            mappings=[StandaardPostMapping(
                typeURI='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#BestratingVanKassei',
                attribuutURI='https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcAfmetingBxlInCm.breedte',
                dotnotatie='afmetingVanBestratingselementBxl.breedte',
                defaultWaarde='14',
                range='',
                usagenote='cm^^cdt:ucumunit',
                isMeetstaatAttr=0,
                isAltijdInTeVullen=0,
                isBasisMapping=1,
                mappingStatus='gemapt 2.0',
                mappingOpmerking='',
                standaardpostnummer='0603.11420')
                , StandaardPostMapping(
                typeURI='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#BestratingVanKassei',
                attribuutURI='https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcAfmetingBxlInCm.lengte',
                dotnotatie='afmetingVanBestratingselementBxl.lengte',
                defaultWaarde='20',
                range='',
                usagenote='cm^^cdt:ucumunit',
                isMeetstaatAttr=0,
                isAltijdInTeVullen=0,
                isBasisMapping=1,
                mappingStatus='gemapt 2.0',
                mappingOpmerking='',
                standaardpostnummer='0603.11420')
                , StandaardPostMapping(
                typeURI='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#BestratingVanKassei',
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
                standaardpostnummer='0603.11420')
                , StandaardPostMapping(
                typeURI='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#BestratingVanKassei',
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
                standaardpostnummer='0603.11420')])
