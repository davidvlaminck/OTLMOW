# coding=utf-8
from PostenMapping.StandaardPost import StandaardPost
from PostenMapping.StandaardPostMapping import StandaardPostMapping


# Generated with PostenCreator. To modify: extend, do not edit
class Post060190401(StandaardPost):
    def __init__(self):
        super().__init__(
            nummer='0601.90401',
            beschrijving='Aanbrengen van een niet-geweven geotextiel op een schraal- of walsbetonfundering volgens 6-1.4',
            meetstaateenheid='M2',
            mappings=[StandaardPostMapping(
                typeURI='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Geotextiel',
                attribuutURI='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Geotextiel.type',
                dotnotatie='type',
                defaultWaarde='niet-geweven-geotextiel',
                range='',
                usagenote='',
                isMeetstaatAttr=0,
                isAltijdInTeVullen=0,
                isBasisMapping=1,
                mappingStatus='gemapt 2.0',
                mappingOpmerking='',
                standaardpostnummer='0601.90401')
                , StandaardPostMapping(
                typeURI='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Geotextiel',
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
                standaardpostnummer='0601.90401')])
