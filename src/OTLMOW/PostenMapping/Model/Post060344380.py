# coding=utf-8
from OTLMOW.PostenMapping.StandaardPost import StandaardPost
from OTLMOW.PostenMapping.StandaardPostMapping import StandaardPostMapping


# Generated with PostenCreator. To modify: extend, do not edit
class Post060344380(StandaardPost):
    def __init__(self):
        super().__init__(
            nummer='0603.44380',
            beschrijving='Gestaalstraalde waterdoorlatende betonstraatstenen, gekleurd met kleurondersteunende granulaten volgens 6-3.5, met verbrede voeg, 100 mm',
            meetstaateenheid='M2',
            mappings=[StandaardPostMapping(
                typeURI='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#WaterdoorlatendeBestrating',
                attribuutURI='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#WaterdoorlatendeBestrating.aard',
                dotnotatie='aard',
                defaultWaarde='met-verbrede-voegen',
                range='',
                usagenote='',
                isMeetstaatAttr=0,
                isAltijdInTeVullen=0,
                isBasisMapping=1,
                mappingStatus='gemapt 2.0',
                mappingOpmerking='',
                standaardpostnummer='0603.44380')
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
                standaardpostnummer='0603.44380')
                , StandaardPostMapping(
                typeURI='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#WaterdoorlatendeBestrating',
                attribuutURI='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#WaterdoorlatendeBestrating.type',
                dotnotatie='type',
                defaultWaarde='gekleurde-met-kleurondersteunende-granulaten',
                range='',
                usagenote='',
                isMeetstaatAttr=0,
                isAltijdInTeVullen=0,
                isBasisMapping=1,
                mappingStatus='gemapt 2.0',
                mappingOpmerking='',
                standaardpostnummer='0603.44380')
                , StandaardPostMapping(
                typeURI='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#WaterdoorlatendeBestrating',
                attribuutURI='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#WaterdoorlatendeBestrating.afwerking',
                dotnotatie='afwerking',
                defaultWaarde='gestaaldstraald',
                range='',
                usagenote='',
                isMeetstaatAttr=0,
                isAltijdInTeVullen=0,
                isBasisMapping=1,
                mappingStatus='gemapt 2.0',
                mappingOpmerking='',
                standaardpostnummer='0603.44380')
                , StandaardPostMapping(
                typeURI='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#WaterdoorlatendeBestrating',
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
                standaardpostnummer='0603.44380')
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
                standaardpostnummer='0603.44380')])
