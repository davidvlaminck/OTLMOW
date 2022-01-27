# coding=utf-8
from src.OTLMOW.PostenMapping.StandaardPost import StandaardPost
from src.OTLMOW.PostenMapping.StandaardPostMapping import StandaardPostMapping


# Generated with PostenCreator. To modify: extend, do not edit
class Post060111022(StandaardPost):
    def __init__(self):
        super().__init__(
            nummer='0601.11022',
            beschrijving='Ongewapende cementbetonverharding, bouwklassegroep B1-B5 volgens 6-1, dikte E = 22 cm',
            meetstaateenheid='M2',
            mappings=[StandaardPostMapping(
                typeURI='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Cementbetonverharding',
                attribuutURI='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Laag.laagRol',
                dotnotatie='laagRol',
                defaultWaarde='verharding',
                range='',
                usagenote='',
                isMeetstaatAttr=0,
                isAltijdInTeVullen=0,
                isBasisMapping=1,
                mappingStatus='gemapt 2.0',
                mappingOpmerking='',
                standaardpostnummer='0601.11022')
                , StandaardPostMapping(
                typeURI='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Cementbetonverharding',
                attribuutURI='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Cementbetonverharding.aardVerharding',
                dotnotatie='aardVerharding',
                defaultWaarde='ongewapend-beton',
                range='',
                usagenote='',
                isMeetstaatAttr=0,
                isAltijdInTeVullen=0,
                isBasisMapping=1,
                mappingStatus='gemapt 2.0',
                mappingOpmerking='',
                standaardpostnummer='0601.11022')
                , StandaardPostMapping(
                typeURI='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Cementbetonverharding',
                attribuutURI='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#LaagBouwklasse.bouwklasse',
                dotnotatie='bouwklasse',
                defaultWaarde='',
                range='B1|B2|B3|B4|B5',
                usagenote='',
                isMeetstaatAttr=0,
                isAltijdInTeVullen=1,
                isBasisMapping=1,
                mappingStatus='gemapt 2.0',
                mappingOpmerking='',
                standaardpostnummer='0601.11022')
                , StandaardPostMapping(
                typeURI='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Cementbetonverharding',
                attribuutURI='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Cementbetonverharding.laagtype',
                dotnotatie='laagtype',
                defaultWaarde='eenlaagse-betonverharding',
                range='',
                usagenote='',
                isMeetstaatAttr=0,
                isAltijdInTeVullen=0,
                isBasisMapping=1,
                mappingStatus='gemapt 2.0',
                mappingOpmerking='',
                standaardpostnummer='0601.11022')
                , StandaardPostMapping(
                typeURI='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Cementbetonverharding',
                attribuutURI='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#LaagDikte.dikte',
                dotnotatie='dikte',
                defaultWaarde='22',
                range='',
                usagenote='cm^^cdt:ucumunit',
                isMeetstaatAttr=0,
                isAltijdInTeVullen=0,
                isBasisMapping=1,
                mappingStatus='gemapt 2.0',
                mappingOpmerking='',
                standaardpostnummer='0601.11022')
                , StandaardPostMapping(
                typeURI='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Cementbetonverharding',
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
                standaardpostnummer='0601.11022')])
