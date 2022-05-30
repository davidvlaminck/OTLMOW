# coding=utf-8
from OTLMOW.PostenMapping.StandaardPost import StandaardPost
from OTLMOW.PostenMapping.StandaardPostMapping import StandaardPostMapping


# Generated with PostenCreator. To modify: extend, do not edit
class Post060457115(StandaardPost):
    def __init__(self):
        super().__init__(
            nummer='0604.57115',
            beschrijving='Verharding van gepenetreerd asfalt volgens 6-4.5, met ZOAP-B1, dikte E = 5 cm',
            meetstaateenheid='M2',
            mappings=[StandaardPostMapping(
                typeURI='',
                attribuutURI='',
                dotnotation='',
                defaultWaarde='',
                range='',
                usagenote='',
                isMeetstaatAttr=0,
                isAltijdInTeVullen=0,
                isBasisMapping=1,
                mappingStatus='wordt gemapt 2.0',
                mappingOpmerking='[Gepenetreerd asfalt] is niet aanwezig in de OTL',
                standaardpostnummer='0604.57115')
                , StandaardPostMapping(
                typeURI='',
                attribuutURI='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Laag.laagRol',
                dotnotation='laagRol',
                defaultWaarde='verharding',
                range='',
                usagenote='',
                isMeetstaatAttr=0,
                isAltijdInTeVullen=0,
                isBasisMapping=1,
                mappingStatus='wordt gemapt 2.0',
                mappingOpmerking='[Gepenetreerd asfalt] is niet aanwezig in de OTL',
                standaardpostnummer='0604.57115')
                , StandaardPostMapping(
                typeURI='',
                attribuutURI='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#LaagDikte.dikte',
                dotnotation='dikte',
                defaultWaarde='5',
                range='',
                usagenote='cm^^cdt:ucumunit',
                isMeetstaatAttr=0,
                isAltijdInTeVullen=0,
                isBasisMapping=1,
                mappingStatus='wordt gemapt 2.0',
                mappingOpmerking='[Gepenetreerd asfalt] is niet aanwezig in de OTL',
                standaardpostnummer='0604.57115')
                , StandaardPostMapping(
                typeURI='',
                attribuutURI='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Laag.oppervlakte',
                dotnotation='oppervlakte',
                defaultWaarde='',
                range='',
                usagenote='m2^^cdt:ucumunit',
                isMeetstaatAttr=1,
                isAltijdInTeVullen=1,
                isBasisMapping=1,
                mappingStatus='wordt gemapt 2.0',
                mappingOpmerking='[Gepenetreerd asfalt] is niet aanwezig in de OTL',
                standaardpostnummer='0604.57115')])
