# coding=utf-8
from OTLMOW.PostenMapping.StandaardPost import StandaardPost
from OTLMOW.PostenMapping.StandaardPostMapping import StandaardPostMapping


# Generated with PostenCreator. To modify: extend, do not edit
class Post060190011(StandaardPost):
    def __init__(self):
        super().__init__(
            nummer='0601.90011',
            beschrijving='Reinigen van het oppervlak met water onder hoge druk (minstens 50 bar) volgens 6-2',
            meetstaateenheid='M2',
            mappings=[StandaardPostMapping(
                typeURI='',
                attribuutURI='',
                dotnotatie='',
                defaultWaarde='',
                range='',
                usagenote='',
                isMeetstaatAttr=0,
                isAltijdInTeVullen=0,
                isBasisMapping=1,
                mappingStatus='wordt gemapt 2.0',
                mappingOpmerking='Activiteit [Reinigen] komt niet voor in de OTL',
                standaardpostnummer='0601.90011')])
