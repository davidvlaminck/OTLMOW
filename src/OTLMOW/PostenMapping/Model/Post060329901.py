# coding=utf-8
from OTLMOW.PostenMapping.StandaardPost import StandaardPost
from OTLMOW.PostenMapping.StandaardPostMapping import StandaardPostMapping


# Generated with PostenCreator. To modify: extend, do not edit
class Post060329901(StandaardPost):
    def __init__(self):
        super().__init__(
            nummer='0603.29901',
            beschrijving='Heropvoegen van mozaïekkeien volgens 6-3.3',
            meetstaateenheid='M2',
            mappings=[StandaardPostMapping(
                typeURI='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#BestratingVanMozaiekkei',
                attribuutURI='',
                dotnotation='',
                defaultWaarde='',
                range='',
                usagenote='',
                isMeetstaatAttr=0,
                isAltijdInTeVullen=1,
                isBasisMapping=1,
                mappingStatus='wordt gemapt 2.0',
                mappingOpmerking='Activiteit [Heropvoegen] komt niet voor in de OTL',
                standaardpostnummer='0603.29901')])
