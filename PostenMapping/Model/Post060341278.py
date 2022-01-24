# coding=utf-8
from PostenMapping.StandaardPost import StandaardPost
from PostenMapping.StandaardPostMapping import StandaardPostMapping


# Generated with PostenCreator. To modify: extend, do not edit
class Post060341278(StandaardPost):
    def __init__(self):
        super().__init__(
            nummer='0603.41278',
            beschrijving='Onbehandelde waterdoorlatende betonstraatstenen, gekleurd met anorganische pigmenten volgens 6-3.5, met drainageopeningen, 80 mm',
            meetstaateenheid='M2',
            mappings=[StandaardPostMapping(
                typeURI='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#WaterdoorlatendeBestrating',
                attribuutURI='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#WaterdoorlatendeBestrating.aard',
                dotnotatie='aard',
                defaultWaarde='met-drainageopeningen',
                range='',
                usagenote='',
                isMeetstaatAttr=0,
                isAltijdInTeVullen=0,
                isBasisMapping=1,
                mappingStatus='gemapt 2.0',
                mappingOpmerking='',
                standaardpostnummer='0603.41278')
                , StandaardPostMapping(
                typeURI='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#WaterdoorlatendeBestrating',
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
                standaardpostnummer='0603.41278')
                , StandaardPostMapping(
                typeURI='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#WaterdoorlatendeBestrating',
                attribuutURI='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#WaterdoorlatendeBestrating.type',
                dotnotatie='type',
                defaultWaarde='gekleurde-met-anorganische-pigmenten',
                range='',
                usagenote='',
                isMeetstaatAttr=0,
                isAltijdInTeVullen=0,
                isBasisMapping=1,
                mappingStatus='gemapt 2.0',
                mappingOpmerking='',
                standaardpostnummer='0603.41278')
                , StandaardPostMapping(
                typeURI='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#WaterdoorlatendeBestrating',
                attribuutURI='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#WaterdoorlatendeBestrating.afwerking',
                dotnotatie='afwerking',
                defaultWaarde='onbehandeld',
                range='',
                usagenote='',
                isMeetstaatAttr=0,
                isAltijdInTeVullen=0,
                isBasisMapping=1,
                mappingStatus='gemapt 2.0',
                mappingOpmerking='',
                standaardpostnummer='0603.41278')
                , StandaardPostMapping(
                typeURI='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#WaterdoorlatendeBestrating',
                attribuutURI='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#LaagDikte.dikte',
                dotnotatie='dikte',
                defaultWaarde='8',
                range='',
                usagenote='cm^^cdt:ucumunit',
                isMeetstaatAttr=0,
                isAltijdInTeVullen=0,
                isBasisMapping=1,
                mappingStatus='gemapt 2.0',
                mappingOpmerking='',
                standaardpostnummer='0603.41278')
                , StandaardPostMapping(
                typeURI='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#WaterdoorlatendeBestrating',
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
                standaardpostnummer='0603.41278')])
