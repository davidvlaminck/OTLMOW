# coding=utf-8
from OTLMOW.PostenMapping.StandaardPost import StandaardPost
from OTLMOW.PostenMapping.StandaardPostMapping import StandaardPostMapping


# Generated with PostenCreator. To modify: extend, do not edit
class Post060390201(StandaardPost):
    def __init__(self):
        super().__init__(
            nummer='0603.90201',
            beschrijving='Ander bodemverbeteringsmiddel dan GFT- of groencompost volgens 3-62.3',
            meetstaateenheid='M2',
            mappings=[StandaardPostMapping(
                typeURI='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#VerhardingGrasKunststofplaat',
                attribuutURI='',
                dotnotatie='',
                defaultWaarde='',
                range='',
                usagenote='',
                isMeetstaatAttr=0,
                isAltijdInTeVullen=0,
                isBasisMapping=1,
                mappingStatus='wordt gemapt 2.0',
                mappingOpmerking='Eigenschap [bodemverbeteraar] is niet aanwezig in de OTL [VerhardingGrasKunststofplaat]',
                standaardpostnummer='0603.90201')])
