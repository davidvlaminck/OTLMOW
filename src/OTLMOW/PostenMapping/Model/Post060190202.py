# coding=utf-8
from OTLMOW.PostenMapping.StandaardPost import StandaardPost
from OTLMOW.PostenMapping.StandaardPostMapping import StandaardPostMapping


# Generated with PostenCreator. To modify: extend, do not edit
class Post060190202(StandaardPost):
    def __init__(self):
        super().__init__(
            nummer='0601.90202',
            beschrijving='Aanbrengen van een langsvoeg tussen een asfaltverharding en de betonverharding volgens 6-1.3.3.3.C',
            meetstaateenheid='M',
            mappings=[StandaardPostMapping(
                typeURI='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Wegdekvoeg',
                attribuutURI='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Wegdekvoeg.lengte',
                dotnotatie='lengte',
                defaultWaarde='',
                range='',
                usagenote='m^^cdt:ucumunit',
                isMeetstaatAttr=1,
                isAltijdInTeVullen=1,
                isBasisMapping=1,
                mappingStatus='gemapt 2.0',
                mappingOpmerking='',
                standaardpostnummer='0601.90202')
                , StandaardPostMapping(
                typeURI='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Wegdekvoeg',
                attribuutURI='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Wegdekvoeg.type',
                dotnotatie='type',
                defaultWaarde='langsvoeg-tussen-asfalt-en-beton',
                range='',
                usagenote='',
                isMeetstaatAttr=0,
                isAltijdInTeVullen=0,
                isBasisMapping=1,
                mappingStatus='gemapt 2.0',
                mappingOpmerking='',
                standaardpostnummer='0601.90202')])
