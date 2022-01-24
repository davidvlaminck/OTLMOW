# coding=utf-8
from PostenMapping.StandaardPost import StandaardPost
from PostenMapping.StandaardPostMapping import StandaardPostMapping


# Generated with PostenCreator. To modify: extend, do not edit
class Post060349901(StandaardPost):
    def __init__(self):
        super().__init__(
            nummer='0603.49901',
            beschrijving='Heropvoegen van waterdoorlatende betonstraatstenen volgens 6-3.5',
            meetstaateenheid='M2',
            mappings=[StandaardPostMapping(
                typeURI='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#WaterdoorlatendeBestrating',
                attribuutURI='',
                dotnotatie='',
                defaultWaarde='',
                range='',
                usagenote='',
                isMeetstaatAttr=0,
                isAltijdInTeVullen=1,
                isBasisMapping=1,
                mappingStatus='wordt gemapt 2.0',
                mappingOpmerking='Activiteit [Heropvoegen] komt niet voor in de OTL',
                standaardpostnummer='0603.49901')])
