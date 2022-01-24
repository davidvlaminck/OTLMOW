# coding=utf-8
from PostenMapping.StandaardPost import StandaardPost
from PostenMapping.StandaardPostMapping import StandaardPostMapping


# Generated with PostenCreator. To modify: extend, do not edit
class Post060419101(StandaardPost):
    def __init__(self):
        super().__init__(
            nummer='0604.19101',
            beschrijving='Behandeling met calciumchloride volgens 6-4.1.4.3',
            meetstaateenheid='M2',
            mappings=[StandaardPostMapping(
                typeURI='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Dolomietverharding',
                attribuutURI='',
                dotnotatie='',
                defaultWaarde='',
                range='',
                usagenote='',
                isMeetstaatAttr=0,
                isAltijdInTeVullen=0,
                isBasisMapping=1,
                mappingStatus='wordt gemapt 2.0',
                mappingOpmerking='Eigenschap [behandelingswijze] is niet aanwezig in de OTL [Dolomietverharding]',
                standaardpostnummer='0604.19101')
                , StandaardPostMapping(
                typeURI='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Dolomietverharding',
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
                standaardpostnummer='0604.19101')])
