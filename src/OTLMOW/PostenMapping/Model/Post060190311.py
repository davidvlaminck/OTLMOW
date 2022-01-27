# coding=utf-8
from src.OTLMOW.PostenMapping.StandaardPost import StandaardPost
from src.OTLMOW.PostenMapping.StandaardPostMapping import StandaardPostMapping


# Generated with PostenCreator. To modify: extend, do not edit
class Post060190311(StandaardPost):
    def __init__(self):
        super().__init__(
            nummer='0601.90311',
            beschrijving='Behandeling met impregneermiddel volgens 6-1.4.17',
            meetstaateenheid='M2',
            mappings=[StandaardPostMapping(
                typeURI='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Cementbetonverharding',
                attribuutURI='',
                dotnotatie='',
                defaultWaarde='',
                range='',
                usagenote='',
                isMeetstaatAttr=0,
                isAltijdInTeVullen=0,
                isBasisMapping=1,
                mappingStatus='wordt gemapt 2.0',
                mappingOpmerking='Expert raadplegen voor mapping [impregneermiddel]',
                standaardpostnummer='0601.90311')
                , StandaardPostMapping(
                typeURI='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Cementbetonverharding',
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
                standaardpostnummer='0601.90311')])
