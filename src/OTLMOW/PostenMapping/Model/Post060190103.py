# coding=utf-8
from OTLMOW.PostenMapping.StandaardPost import StandaardPost
from OTLMOW.PostenMapping.StandaardPostMapping import StandaardPostMapping


# Generated with PostenCreator. To modify: extend, do not edit
class Post060190103(StandaardPost):
    def __init__(self):
        super().__init__(
            nummer='0601.90103',
            beschrijving='Meerprijs voor in de massa gekleurde betonverharding volgens 6-1.3.4, kleur bordeaux/bruin',
            meetstaateenheid='M2',
            mappings=[StandaardPostMapping(
                typeURI='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Cementbetonverharding',
                attribuutURI='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DtcSupplementenCBV.kleur',
                dotnotatie='supplementen.kleur',
                defaultWaarde='bordeaux-bruin',
                range='',
                usagenote='',
                isMeetstaatAttr=0,
                isAltijdInTeVullen=0,
                isBasisMapping=1,
                mappingStatus='gemapt 2.0',
                mappingOpmerking='',
                standaardpostnummer='0601.90103')
                , StandaardPostMapping(
                typeURI='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Cementbetonverharding',
                attribuutURI='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DtcSupplementenCBV.type',
                dotnotatie='supplementen.type',
                defaultWaarde='figureren-betonoppervlak-in-de-massa-gekleurd',
                range='',
                usagenote='',
                isMeetstaatAttr=0,
                isAltijdInTeVullen=0,
                isBasisMapping=1,
                mappingStatus='gemapt 2.0',
                mappingOpmerking='',
                standaardpostnummer='0601.90103')
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
                standaardpostnummer='0601.90103')])
