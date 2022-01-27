# coding=utf-8
from OTLMOW.PostenMapping.StandaardPost import StandaardPost
from OTLMOW.PostenMapping.StandaardPostMapping import StandaardPostMapping


# Generated with PostenCreator. To modify: extend, do not edit
class Post050406000(StandaardPost):
    def __init__(self):
        super().__init__(
            nummer='0504.06000',
            beschrijving='Fundering van ternair mengsel volgens 5-4.6, plaatselijke uitvoering',
            meetstaateenheid='M3',
            mappings=[StandaardPostMapping(
                typeURI='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Onderbouw',
                attribuutURI='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Laag.laagRol',
                dotnotatie='laagRol',
                defaultWaarde='fundering',
                range='',
                usagenote='',
                isMeetstaatAttr=0,
                isAltijdInTeVullen=0,
                isBasisMapping=1,
                mappingStatus='gemapt 2.0',
                mappingOpmerking='',
                standaardpostnummer='0504.06000')
                , StandaardPostMapping(
                typeURI='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Onderbouw',
                attribuutURI='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Onderbouw.type',
                dotnotatie='type',
                defaultWaarde='ternair-mengsel',
                range='',
                usagenote='',
                isMeetstaatAttr=0,
                isAltijdInTeVullen=0,
                isBasisMapping=1,
                mappingStatus='gemapt 2.0',
                mappingOpmerking='',
                standaardpostnummer='0504.06000')
                , StandaardPostMapping(
                typeURI='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Onderbouw',
                attribuutURI='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Onderbouw.volume',
                dotnotatie='volume',
                defaultWaarde='',
                range='',
                usagenote='m3^^cdt:ucumunit',
                isMeetstaatAttr=1,
                isAltijdInTeVullen=1,
                isBasisMapping=1,
                mappingStatus='gemapt 2.0',
                mappingOpmerking='',
                standaardpostnummer='0504.06000')])
