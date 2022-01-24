# coding=utf-8
from PostenMapping.StandaardPost import StandaardPost
from PostenMapping.StandaardPostMapping import StandaardPostMapping


# Generated with PostenCreator. To modify: extend, do not edit
class Post060351265(StandaardPost):
    def __init__(self):
        super().__init__(
            nummer='0603.51265',
            beschrijving='Bestrating van gebakken straatstenen, standaardkwaliteitsklasse A volgens 6-3.6, dikformaat, hoogte ca. 65 mm',
            meetstaateenheid='M2',
            mappings=[StandaardPostMapping(
                typeURI='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#BestratingVanGebakkenStraatsteen',
                attribuutURI='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#BestratingVanGebakkenStraatsteen.formaatVanBestratingselement',
                dotnotatie='formaatVanBestratingselement',
                defaultWaarde='dikformaat-(ca.-200-x-ca.-65-mm)',
                range='',
                usagenote='',
                isMeetstaatAttr=0,
                isAltijdInTeVullen=0,
                isBasisMapping=1,
                mappingStatus='gemapt 2.0',
                mappingOpmerking='',
                standaardpostnummer='0603.51265')
                , StandaardPostMapping(
                typeURI='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#BestratingVanGebakkenStraatsteen',
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
                standaardpostnummer='0603.51265')
                , StandaardPostMapping(
                typeURI='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#BestratingVanGebakkenStraatsteen',
                attribuutURI='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#BestratingVanGebakkenStraatsteen.standaardkwaliteitsklasse',
                dotnotatie='standaardkwaliteitsklasse',
                defaultWaarde='a',
                range='',
                usagenote='',
                isMeetstaatAttr=0,
                isAltijdInTeVullen=0,
                isBasisMapping=1,
                mappingStatus='gemapt 2.0',
                mappingOpmerking='',
                standaardpostnummer='0603.51265')
                , StandaardPostMapping(
                typeURI='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#BestratingVanGebakkenStraatsteen',
                attribuutURI='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#LaagDikte.dikte',
                dotnotatie='dikte',
                defaultWaarde='6.5',
                range='',
                usagenote='cm^^cdt:ucumunit',
                isMeetstaatAttr=0,
                isAltijdInTeVullen=0,
                isBasisMapping=1,
                mappingStatus='gemapt 2.0',
                mappingOpmerking='',
                standaardpostnummer='0603.51265')
                , StandaardPostMapping(
                typeURI='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#BestratingVanGebakkenStraatsteen',
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
                standaardpostnummer='0603.51265')])
