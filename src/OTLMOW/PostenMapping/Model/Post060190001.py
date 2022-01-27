# coding=utf-8
from src.OTLMOW.PostenMapping.StandaardPost import StandaardPost
from src.OTLMOW.PostenMapping.StandaardPostMapping import StandaardPostMapping


# Generated with PostenCreator. To modify: extend, do not edit
class Post060190001(StandaardPost):
    def __init__(self):
        super().__init__(
            nummer='0601.90001',
            beschrijving='Ribben van verankeringslandhoofden van doorgaand gewapende cementbetonverhardingen volgens 6-1.3.3.8',
            meetstaateenheid='M',
            mappings=[StandaardPostMapping(
                typeURI='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Verankeringslandhoofd',
                attribuutURI='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Verankeringslandhoofd.lengte',
                dotnotatie='lengte',
                defaultWaarde='',
                range='',
                usagenote='m^^cdt:ucumunit',
                isMeetstaatAttr=1,
                isAltijdInTeVullen=1,
                isBasisMapping=1,
                mappingStatus='wordt gemapt 2.0',
                mappingOpmerking='Expert raadplegen voor mapping [StandaardpostMeetstaateenheid]',
                standaardpostnummer='0601.90001')
                , StandaardPostMapping(
                typeURI='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Verankeringslandhoofd',
                attribuutURI='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Verankeringslandhoofd.breedte',
                dotnotatie='breedte',
                defaultWaarde='',
                range='',
                usagenote='m^^cdt:ucumunit',
                isMeetstaatAttr=1,
                isAltijdInTeVullen=1,
                isBasisMapping=1,
                mappingStatus='wordt gemapt 2.0',
                mappingOpmerking='Expert raadplegen voor mapping [StandaardpostMeetstaateenheid]',
                standaardpostnummer='0601.90001')
                , StandaardPostMapping(
                typeURI='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Verankeringslandhoofd',
                attribuutURI='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Verankeringslandhoofd.ribben',
                dotnotatie='ribben',
                defaultWaarde='integer',
                range='',
                usagenote='',
                isMeetstaatAttr=0,
                isAltijdInTeVullen=1,
                isBasisMapping=1,
                mappingStatus='wordt gemapt 2.0',
                mappingOpmerking='Expert raadplegen voor mapping [ribben]',
                standaardpostnummer='0601.90001')])
