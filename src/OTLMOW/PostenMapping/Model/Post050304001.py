# coding=utf-8
from src.OTLMOW.PostenMapping.StandaardPost import StandaardPost
from src.OTLMOW.PostenMapping.StandaardPostMapping import StandaardPostMapping


# Generated with PostenCreator. To modify: extend, do not edit
class Post050304001(StandaardPost):
    def __init__(self):
        super().__init__(
            nummer='0503.04001',
            beschrijving='Vooronderzoek van de grond en studie naar de bindmiddeldosering volgens 5-3.4.1.2.A',
            meetstaateenheid='STUK',
            mappings=[StandaardPostMapping(
                typeURI='https://wegenenverkeer.data.vlaanderen.be/ns/proefenmeting#ProefBindmiddeldosering',
                attribuutURI='',
                dotnotatie='',
                defaultWaarde='',
                range='',
                usagenote='',
                isMeetstaatAttr=1,
                isAltijdInTeVullen=0,
                isBasisMapping=1,
                mappingStatus='gemapt 2.0',
                mappingOpmerking='Meetstaateenheid STUK vloeit verder uit geïnstantieerde objecten',
                standaardpostnummer='0503.04001')])
