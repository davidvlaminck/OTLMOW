# coding=utf-8
from OTLMOW.PostenMapping.StandaardPost import StandaardPost
from OTLMOW.PostenMapping.StandaardPostMapping import StandaardPostMapping


# Generated with PostenCreator. To modify: extend, do not edit
class Post050303199(StandaardPost):
    def __init__(self):
        super().__init__(
            nummer='0503.03199',
            beschrijving='Aanleg van een tijdelijke onderfundering type II t.h.v. opritten, inclusief instandhouden en terug opbreken en afvoeren volgens 5-3.3',
            meetstaateenheid='STUK',
            mappings=[StandaardPostMapping(
                typeURI='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Onderbouw',
                attribuutURI='',
                dotnotation='',
                defaultWaarde='',
                range='',
                usagenote='',
                isMeetstaatAttr=1,
                isAltijdInTeVullen=0,
                isBasisMapping=1,
                mappingStatus='gemapt 2.0',
                mappingOpmerking='Meetstaateenheid STUK vloeit verder uit geïnstantieerde objecten',
                standaardpostnummer='0503.03199')
                , StandaardPostMapping(
                typeURI='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Onderbouw',
                attribuutURI='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Laag.laagRol',
                dotnotation='laagRol',
                defaultWaarde='onderfundering',
                range='',
                usagenote='',
                isMeetstaatAttr=0,
                isAltijdInTeVullen=0,
                isBasisMapping=1,
                mappingStatus='gemapt 2.0',
                mappingOpmerking='Tijdelijke asset',
                standaardpostnummer='0503.03199')
                , StandaardPostMapping(
                typeURI='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Onderbouw',
                attribuutURI='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Onderbouw.type',
                dotnotation='type',
                defaultWaarde='onderfundering-type-II',
                range='',
                usagenote='',
                isMeetstaatAttr=0,
                isAltijdInTeVullen=0,
                isBasisMapping=1,
                mappingStatus='gemapt 2.0',
                mappingOpmerking='Tijdelijke asset',
                standaardpostnummer='0503.03199')])
