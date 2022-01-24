# coding=utf-8
from PostenMapping.StandaardPost import StandaardPost
from PostenMapping.StandaardPostMapping import StandaardPostMapping


# Generated with PostenCreator. To modify: extend, do not edit
class Post050407105(StandaardPost):
    def __init__(self):
        super().__init__(
            nummer='0504.07105',
            beschrijving='Fundering en stut van zandcement voor lijnvormige elementen volgens 5-4.7, volume ≤ 0,125 m³/m',
            meetstaateenheid='M',
            mappings=[StandaardPostMapping(
                typeURI='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Onderbouw',
                attribuutURI='',
                dotnotatie='',
                defaultWaarde='',
                range='',
                usagenote='',
                isMeetstaatAttr=0,
                isAltijdInTeVullen=0,
                isBasisMapping=1,
                mappingStatus='wordt gemapt 2.0',
                mappingOpmerking='Eigenschap [volumePerMeter] is niet aanwezig in de OTL [Onderbouw]',
                standaardpostnummer='0504.07105')
                , StandaardPostMapping(
                typeURI='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Onderbouw',
                attribuutURI='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Laag.laagRol',
                dotnotatie='laagRol',
                defaultWaarde='fundering-voor-lijnvormige-elementen',
                range='',
                usagenote='',
                isMeetstaatAttr=0,
                isAltijdInTeVullen=0,
                isBasisMapping=1,
                mappingStatus='gemapt 2.0',
                mappingOpmerking='',
                standaardpostnummer='0504.07105')
                , StandaardPostMapping(
                typeURI='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Onderbouw',
                attribuutURI='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Laag.lengte',
                dotnotatie='lengte',
                defaultWaarde='',
                range='',
                usagenote='m^^cdt:ucumunit',
                isMeetstaatAttr=1,
                isAltijdInTeVullen=1,
                isBasisMapping=1,
                mappingStatus='gemapt 2.0',
                mappingOpmerking='',
                standaardpostnummer='0504.07105')
                , StandaardPostMapping(
                typeURI='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Onderbouw',
                attribuutURI='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Onderbouw.type',
                dotnotatie='type',
                defaultWaarde='zandcement',
                range='',
                usagenote='',
                isMeetstaatAttr=0,
                isAltijdInTeVullen=0,
                isBasisMapping=1,
                mappingStatus='gemapt 2.0',
                mappingOpmerking='',
                standaardpostnummer='0504.07105')])
