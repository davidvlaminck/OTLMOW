# coding=utf-8
from src.OTLMOW.PostenMapping.StandaardPost import StandaardPost
from src.OTLMOW.PostenMapping.StandaardPostMapping import StandaardPostMapping


# Generated with PostenCreator. To modify: extend, do not edit
class Post050304003(StandaardPost):
    def __init__(self):
        super().__init__(
            nummer='0503.04003',
            beschrijving='Bindmiddel voor onderfundering type III indien geen vooronderzoek is uitgevoerd volgens 5-3.4.1.2.A, cement',
            meetstaateenheid='TON',
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
                mappingOpmerking='[Bindmiddel] is niet aanwezig in de OTL',
                standaardpostnummer='0503.04003')])
