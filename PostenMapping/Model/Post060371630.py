# coding=utf-8
from PostenMapping.StandaardPost import StandaardPost
from PostenMapping.StandaardPostMapping import StandaardPostMapping


# Generated with PostenCreator. To modify: extend, do not edit
class Post060371630(StandaardPost):
    def __init__(self):
        super().__init__(
            nummer='0603.71630',
            beschrijving='Gezaagde natuursteentegels, gebruiksklasse 6 volgens 6-3.8, 300 x 300, 100 mm',
            meetstaateenheid='M2',
            mappings=[StandaardPostMapping(
                typeURI='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#BestratingVanNatuursteentegel',
                attribuutURI='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#BestratingVanNatuursteentegel.afwerking',
                dotnotatie='afwerking',
                defaultWaarde='gezaagd',
                range='',
                usagenote='',
                isMeetstaatAttr=0,
                isAltijdInTeVullen=0,
                isBasisMapping=1,
                mappingStatus='gemapt 2.0',
                mappingOpmerking='',
                standaardpostnummer='0603.71630')
                , StandaardPostMapping(
                typeURI='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#BestratingVanNatuursteentegel',
                attribuutURI='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#BestratingVanNatuursteentegel.afmetingVanBestratingselementLxB',
                dotnotatie='afmetingVanBestratingselementLxB',
                defaultWaarde='300-x-300',
                range='',
                usagenote='',
                isMeetstaatAttr=0,
                isAltijdInTeVullen=0,
                isBasisMapping=1,
                mappingStatus='gemapt 2.0',
                mappingOpmerking='',
                standaardpostnummer='0603.71630')
                , StandaardPostMapping(
                typeURI='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#BestratingVanNatuursteentegel',
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
                standaardpostnummer='0603.71630')
                , StandaardPostMapping(
                typeURI='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#BestratingVanNatuursteentegel',
                attribuutURI='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#BestratingVanNatuursteentegel.gebruiksklasse',
                dotnotatie='gebruiksklasse',
                defaultWaarde='6',
                range='',
                usagenote='',
                isMeetstaatAttr=0,
                isAltijdInTeVullen=0,
                isBasisMapping=1,
                mappingStatus='gemapt 2.0',
                mappingOpmerking='',
                standaardpostnummer='0603.71630')
                , StandaardPostMapping(
                typeURI='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#BestratingVanNatuursteentegel',
                attribuutURI='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#LaagDikte.dikte',
                dotnotatie='dikte',
                defaultWaarde='10',
                range='',
                usagenote='cm^^cdt:ucumunit',
                isMeetstaatAttr=0,
                isAltijdInTeVullen=0,
                isBasisMapping=1,
                mappingStatus='gemapt 2.0',
                mappingOpmerking='',
                standaardpostnummer='0603.71630')
                , StandaardPostMapping(
                typeURI='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#BestratingVanNatuursteentegel',
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
                standaardpostnummer='0603.71630')])
