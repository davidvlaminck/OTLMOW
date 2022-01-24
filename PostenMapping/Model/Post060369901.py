# coding=utf-8
from PostenMapping.StandaardPost import StandaardPost
from PostenMapping.StandaardPostMapping import StandaardPostMapping


# Generated with PostenCreator. To modify: extend, do not edit
class Post060369901(StandaardPost):
    def __init__(self):
        super().__init__(
            nummer='0603.69901',
            beschrijving='Heropvoegen van betontegels volgens 6-3.7',
            meetstaateenheid='M2',
            mappings=[StandaardPostMapping(
                typeURI='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#BestratingVanBetontegel',
                attribuutURI='',
                dotnotatie='',
                defaultWaarde='',
                range='',
                usagenote='',
                isMeetstaatAttr=0,
                isAltijdInTeVullen=0,
                isBasisMapping=1,
                mappingStatus='wordt gemapt 2.0',
                mappingOpmerking='Activiteit [Heropvoegen] komt niet voor in de OTL',
                standaardpostnummer='0603.69901')])
